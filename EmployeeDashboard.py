import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Employee Dashboard", layout="wide")

# Custom CSS for styling and animations
st.markdown("""
<style>
/* Import Google Font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

/* Global styles */
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: #ffffff;
}

/* Main container */
.main {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    margin: 10px;
    animation: fadeIn 1s ease-in;
}

/* Sidebar styling */
.css-1lcbmhc {  /* Streamlit sidebar class */
    background: rgba(0, 0, 0, 0.7);
    border-right: 1px solid rgba(255, 255, 255, 0.2);
}

/* Card styling for KPIs and charts */
.stMetric, .plotly-chart {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.stMetric:hover, .plotly-chart:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

/* Button styling */
.stButton > button {
    background: #ff6f61;
    color: white;
    border: none;
    border-radius: 25px;
    padding: 10px 20px;
    font-size: 16px;
    transition: background 0.3s ease, transform 0.2s ease;
}
.stButton > button:hover {
    background: #ff8a75;
    transform: scale(1.05);
}

/* Data table styling */
.stDataFrame {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    overflow: hidden;
}
.stDataFrame tr:hover {
    background: rgba(255, 255, 255, 0.2);
    transition: background 0.2s ease;
}

/* Slider styling */
.stSlider > div > div > div {
    background: #ff6f61;
}
.stSlider > div > div > div > div {
    background: white;
}

/* Fade-in animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Title animation */
h1 {
    animation: fadeIn 1.2s ease-in;
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Warning and error messages */
.stAlert {
    background: rgba(255, 255, 255, 0.2);
    color: #ffffff;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("Employee Data Dashboard")

# Load your CSV file
csv_path = 'employee_data.csv'  # Update with your CSV file name/path
try:
    df = pd.read_csv(csv_path, encoding='utf-8')
except FileNotFoundError:
    st.error(f"CSV file '{csv_path}' not found. Please check the file path.")
    st.stop()
except UnicodeDecodeError:
    try:
        df = pd.read_csv(csv_path, encoding='latin1')
    except Exception as e:
        st.error(f"Error reading CSV file: {e}. Try specifying the correct encoding.")
        st.stop()
except Exception as e:
    st.error(f"Error loading CSV file: {e}")
    st.stop()

# Display column names and sample data for debugging
st.write("Columns in your CSV:", df.columns.tolist())
st.write("Sample data (first 5 rows):", df.head())

# Additional debugging: Show unique values for Exit Date and Annual Salary
if 'Exit Date' in df.columns:
    st.write("Unique 'Exit Date' values (sample of 10):", df['Exit Date'].dropna().unique()[:10])
if 'Annual Salary' in df.columns:
    st.write("Unique 'Annual Salary' values (sample of 10):", df['Annual Salary'].dropna().unique()[:10])

# Convert date columns to datetime
if 'Hire Date' in df.columns:
    df['Hire Date'] = pd.to_datetime(df['Hire Date'], errors='coerce')
    if df['Hire Date'].isna().all():
        st.warning("All 'Hire Date' values are invalid. Hiring trend chart will be skipped.")
else:
    st.warning("Column 'Hire Date' not found in CSV. Hiring trend chart will be skipped.")

if 'Exit Date' in df.columns:
    # Replace common invalid values with NA
    invalid_date_values = ['N/A', 'Unknown', 'None', '', 'TBD', 'Pending', 'Not Applicable']
    df['Exit Date'] = df['Exit Date'].replace(invalid_date_values, pd.NA)
    # Try multiple date formats
    date_formats = ['%m/%d/%Y', '%d-%m-%Y', '%Y-%m-%d', '%m-%d-%Y', '%d/%m/%Y']
    for fmt in date_formats:
        try:
            df['Exit Date'] = pd.to_datetime(df['Exit Date'], errors='coerce', format=fmt)
            break
        except ValueError:
            continue
    if df['Exit Date'].isna().all():
        st.warning("All 'Exit Date' values are invalid. Exit trend chart will be skipped.")
    else:
        invalid_dates = df['Exit Date'].isna().sum()
        if invalid_dates > 0:
            st.warning(f"{invalid_dates} invalid 'Exit Date' values found. These will be excluded from the Exit Trend chart.")
else:
    st.warning("Column 'Exit Date' not found in CSV. Exit trend chart will be skipped.")

# Clean Annual Salary column
if 'Annual Salary' in df.columns:
    # Replace common invalid values with NA
    invalid_salary_values = ['N/A', 'Unknown', 'None', '', 'Confidential', 'Negotiable']
    df['Annual Salary'] = df['Annual Salary'].replace(invalid_salary_values, pd.NA)
    # Clean currency symbols, commas, and other characters
    df['Annual Salary'] = df['Annual Salary'].replace(r'[\$,]', '', regex=True)
    df['Annual Salary'] = pd.to_numeric(df['Annual Salary'], errors='coerce')
    if df['Annual Salary'].isna().all():
        st.warning("No valid numeric data in 'Annual Salary' column. Salary-related charts will be skipped.")
    else:
        invalid_salaries = df['Annual Salary'].isna().sum()
        if invalid_salaries > 0:
            st.warning(f"{invalid_salaries} invalid 'Annual Salary' values found. These will be excluded from salary charts.")
else:
    st.warning("Column 'Annual Salary' not found in CSV. Salary-related charts will be skipped.")

# Sidebar for filters
st.sidebar.header("Filters")

# Department filter
if 'Department' in df.columns:
    departments = st.sidebar.multiselect(
        "Select Department",
        options=df['Department'].dropna().unique(),
        default=df['Department'].dropna().unique()
    )
else:
    departments = None
    st.warning("Column 'Department' not found in CSV.")

# Age filter
if 'Age' in df.columns:
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    if df['Age'].notna().any():
        age_range = st.sidebar.slider(
            "Age Range",
            min_value=int(df['Age'].min()),
            max_value=int(df['Age'].max()),
            value=(int(df['Age'].min()), int(df['Age'].max()))
        )
    else:
        age_range = None
        st.warning("No valid numeric data in 'Age' column.")
else:
    age_range = None
    st.warning("Column 'Age' not found in CSV.")

# Annual Salary filter
if 'Annual Salary' in df.columns and df['Annual Salary'].notna().any():
    salary_range = st.sidebar.slider(
        "Salary Range",
        min_value=int(df['Annual Salary'].min()),
        max_value=int(df['Annual Salary'].max()),
        value=(int(df['Annual Salary'].min()), int(df['Annual Salary'].max()))
    )
else:
    salary_range = None
    if 'Annual Salary' in df.columns:
        st.warning("No valid numeric data in 'Annual Salary' column for filtering.")
    else:
        st.warning("Column 'Annual Salary' not found in CSV.")

# Filter data
filtered_df = df.copy()
if departments:
    filtered_df = filtered_df[filtered_df['Department'].isin(departments)]
if age_range and 'Age' in filtered_df.columns:
    filtered_df = filtered_df[filtered_df['Age'].between(age_range[0], age_range[1])]
if salary_range and 'Annual Salary' in filtered_df.columns:
    filtered_df = filtered_df[filtered_df['Annual Salary'].between(salary_range[0], salary_range[1])]

# Layout
col1, col2 = st.columns(2)

# KPI Metrics
with col1:
    st.subheader("Key Metrics")
    st.metric("Total Employees", len(filtered_df))
    if 'Annual Salary' in filtered_df.columns:
        avg_salary = filtered_df['Annual Salary'].mean()
        if pd.notna(avg_salary):
            st.metric("Average Salary", f"${avg_salary:,.2f}")
    if 'Age' in filtered_df.columns:
        avg_age = filtered_df['Age'].mean()
        if pd.notna(avg_age):
            st.metric("Average Age", f"{avg_age:,.1f}")

# Department Distribution (Pie Chart)
if 'Department' in filtered_df.columns:
    with col2:
        st.subheader("Department Distribution")
        dept_counts = filtered_df['Department'].value_counts().reset_index()
        dept_counts.columns = ['Department', 'Count']
        fig1 = px.pie(dept_counts, names='Department', values='Count', title="Employees by Department")
        fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
        st.plotly_chart(fig1, use_container_width=True)

# Salary Distribution (Histogram)
if 'Annual Salary' in filtered_df.columns and filtered_df['Annual Salary'].notna().any():
    st.subheader("Salary Distribution")
    fig2 = px.histogram(filtered_df, x='Annual Salary', nbins=20, title="Salary Distribution")
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig2, use_container_width=True)

# Age vs Salary Scatter
if 'Age' in filtered_df.columns and 'Annual Salary' in filtered_df.columns and filtered_df['Annual Salary'].notna().any():
    st.subheader("Age vs Salary")
    fig3 = px.scatter(
        filtered_df,
        x='Age',
        y='Annual Salary',
        color='Department' if 'Department' in filtered_df.columns else None,
        hover_data=['Name'] if 'Name' in filtered_df.columns else None,
        title="Age vs Salary by Department"
    )
    fig3.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig3, use_container_width=True)

# Hire Date Trend (Line Chart)
if 'Hire Date' in filtered_df.columns and filtered_df['Hire Date'].notna().any():
    st.subheader("Hiring Trend")
    filtered_df['Hire Year'] = filtered_df['Hire Date'].dt.year
    hire_counts = filtered_df['Hire Year'].value_counts().sort_index().reset_index()
    hire_counts.columns = ['Year', 'Count']
    fig4 = px.line(hire_counts, x='Year', y='Count', title="Hires per Year")
    fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig4, use_container_width=True)

# Exit Date Trend (Line Chart)
if 'Exit Date' in filtered_df.columns and filtered_df['Exit Date'].notna().any():
    st.subheader("Exit Trend")
    filtered_df['Exit Year'] = filtered_df['Exit Date'].dt.year
    exit_counts = filtered_df['Exit Year'].value_counts().sort_index().reset_index()
    exit_counts.columns = ['Year', 'Count']
    fig5 = px.line(exit_counts, x='Year', y='Count', title="Exits per Year")
    fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig5, use_container_width=True)

# Data Table
st.subheader("Employee Data")
st.dataframe(filtered_df, use_container_width=True)

# Download filtered data
csv = filtered_df.to_csv(index=False)
st.download_button("Download Filtered Data", csv, "filtered_employee_data.csv", "text/csv")