Employee Data Dashboard
Overview
The Employee Data Dashboard is a Streamlit-based web application that visualizes employee data from a CSV file (employee_data.csv). It provides interactive charts and metrics, including:

Key Metrics: Total employees, average salary, and average age.
Charts:
Pie chart for department distribution.
Histogram for salary distribution.
Scatter plot for age vs. salary.
Line charts for hiring and exit trends.


Filters: Department, age range, and salary range.
Data Table: Displays filtered employee data.
Download Option: Export filtered data as CSV.

The dashboard features a modern UI with a gradient background, glassmorphism cards, Poppins font, fade-in animations, and hover effects (cards lift, buttons scale, table rows highlight).
Prerequisites

Python: Version 3.8 or higher.
Virtual Environment: Recommended for dependency management.
Git: For cloning the repository.
Streamlit Cloud Account: For deployment (optional).

Installation
Local Setup

Clone the Repository:
git clone https://github.com/HerveMucyo/EmployeeDashboard.git
cd EmployeeDashboard


Create a Virtual Environment:
python -m venv .venv


On Windows:.\.venv\Scripts\Activate.ps1


On macOS/Linux:source .venv/bin/activate




Install Dependencies:Ensure requirements.txt is in the project root:
streamlit==1.38.0
pandas==2.2.3
plotly==6.1.2
openpyxl==3.1.5
numpy==2.3.1

Install them:
pip install -r requirements.txt


Verify CSV File:Ensure employee_data.csv is in the project root. Expected columns:

ID, Name, Department, Annual Salary, Age, Hire Date, Exit DateUpdate csv_path in EmployeeDashboard.py if the CSV is in a subdirectory (e.g., data/employee_data.csv).


Run the Dashboard:
streamlit run EmployeeDashboard.py

Open http://localhost:8501 in a browser.


Streamlit Cloud Deployment

Push to GitHub:Ensure the repository contains:

EmployeeDashboard.py
employee_data.csv
requirements.txt

git add EmployeeDashboard.py employee_data.csv requirements.txt
git commit -m "Update project files"
git push


Deploy on Streamlit Cloud:

Go to Streamlit Cloud.
Connect your GitHub repository (HerveMucyo/EmployeeDashboard).
Set the main script to EmployeeDashboard.py.
Deploy and check logs (Manage app > Logs) for errors.



Usage

Filters: Use the sidebar to filter by department, age range, or salary range.
Visualizations: View interactive charts (pie, histogram, scatter, line).
Data Table: Browse filtered employee data.
Download: Click "Download Filtered Data" to export as CSV.
Styling: Enjoy a modern UI with a blue gradient background, glassmorphism cards, Poppins font, and animations (fade-in, hover effects).

Data Requirements
The employee_data.csv should include:

Columns: ID, Name, Department, Annual Salary, Age, Hire Date, Exit Date.
Formats:
Annual Salary: Numeric or cleanable (e.g., $50,000).
Hire Date, Exit Date: Dates (e.g., MM/DD/YYYY, DD-MM-YYYY, YYYY-MM-DD).


Known Issues:
915 invalid Exit Date values (e.g., N/A, Unknown) are excluded from the exit trend chart.
Annual Salary may show as None due to invalid values or column name mismatches.
Run locally and check debugging output (Columns in your CSV, Sample data, Unique values, Warnings) to resolve.



Troubleshooting

ModuleNotFoundError: plotly.express:
Ensure plotly==6.1.2 is in requirements.txt.
Redeploy on Streamlit Cloud and check logs.


Invalid Data:
Check debugging output in the dashboard:
Columns in your CSV
Sample data
Unique 'Exit Date' values and Unique 'Annual Salary' values
Warnings


Update EmployeeDashboard.py to handle specific invalid values or date formats.


Styling Issues:
Use a modern browser (Chrome, Firefox, Edge) for full CSS support.



Contributing

Fork the repository.
Create a branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
MIT License. See LICENSE for details.
Contact
For issues or suggestions, open an issue on GitHub or contact the repository owner.
