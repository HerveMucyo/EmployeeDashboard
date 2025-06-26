
# 📊 Employee Data Dashboard

**A Streamlit-based web application for visualizing and filtering employee data.**

---

## 🧾 Overview

The **Employee Data Dashboard** provides an interactive, visually appealing interface for exploring employee data from a CSV file (`employee_data.csv`). It features:

### 🔑 Key Metrics:

* Total Employees
* Average Salary
* Average Age

### 📈 Charts:

* Pie chart: Department Distribution
* Histogram: Salary Distribution
* Scatter Plot: Age vs. Salary
* Line Charts: Hiring & Exit Trends

### 🧰 Filters:

* Department
* Age Range
* Salary Range

### 📋 Data Table:

* Displays filtered employee data

### ⬇️ Download Option:

* Export filtered data as CSV

---

## 🎨 Modern UI Features

* Blue gradient background
* Glassmorphism cards
* Poppins font
* Fade-in animations
* Hover effects: card lift, button scale, row highlight

---

## ⚙️ Prerequisites

* **Python:** 3.8 or higher
* **Virtual Environment:** Recommended
* **Git:** For cloning the repository
* **Streamlit Cloud Account:** For optional deployment

---

## 🛠 Installation

### 🔧 Local Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/HerveMucyo/EmployeeDashboard.git
   cd EmployeeDashboard
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   ```

   * On **Windows**:
     `.\.venv\Scripts\Activate.ps1`
   * On **macOS/Linux**:
     `source .venv/bin/activate`

3. **Install Dependencies**
   Make sure `requirements.txt` is present in the root folder.

   ```txt
   streamlit==1.38.0
   pandas==2.2.3
   plotly==6.1.2
   openpyxl==3.1.5
   numpy==2.3.1
   ```

   Then run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Check CSV File**
   Ensure `employee_data.csv` is in the root directory.
   Required columns:

   ```
   ID, Name, Department, Annual Salary, Age, Hire Date, Exit Date
   ```

   Update the path in `EmployeeDashboard.py` if stored in a subfolder (e.g., `data/employee_data.csv`).

5. **Run the Dashboard**

   ```bash
   streamlit run EmployeeDashboard.py
   ```

   Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ Streamlit Cloud Deployment

1. **Push to GitHub**
   Ensure the following files are in the repository:

   ```
   EmployeeDashboard.py
   employee_data.csv
   requirements.txt
   ```

   Then:

   ```bash
   git add EmployeeDashboard.py employee_data.csv requirements.txt
   git commit -m "Update project files"
   git push
   ```

2. **Deploy via Streamlit Cloud**

   * Go to [Streamlit Cloud](https://streamlit.io/cloud)
   * Connect to your GitHub repository (`HerveMucyo/EmployeeDashboard`)
   * Set the **main script** as `EmployeeDashboard.py`
   * Deploy the app
   * Check logs (Manage app > Logs) for issues

---

## ▶️ Usage

* **Filters:** Use the sidebar for department, age, or salary filtering.
* **Visualizations:** Interactive pie, histogram, scatter, and line charts.
* **Data Table:** View filtered employee records.
* **Download:** Export filtered data as CSV.
* **Styling:** Modern design with animations and Poppins font.

---

## 📂 Data Requirements

The file `employee_data.csv` must include:

| Column        | Format Example              |
| ------------- | --------------------------- |
| ID            | 123                         |
| Name          | Jane Doe                    |
| Department    | Sales                       |
| Annual Salary | \$55,000 or 55000           |
| Age           | 34                          |
| Hire Date     | 2020-01-15 (or similar)     |
| Exit Date     | 2023-06-01, N/A, or Unknown |

### Known Issues:

* **Exit Date:** \~915 invalid values are ignored in exit trend chart.
* **Salary Parsing:** May return `None` if malformed or mismatched column names.
* Run locally and check debug output for insights:

  * Column structure
  * Sample data
  * Unique values
  * Warnings

---

## 🧰 Troubleshooting

### ❌ `ModuleNotFoundError: plotly.express`

* Ensure `plotly==6.1.2` is in `requirements.txt`
* Reinstall or redeploy if needed

### ⚠️ Invalid Data

Check output in dashboard logs:

* CSV column names
* Sample data
* Unique 'Exit Date' and 'Annual Salary' values
* Debugging warnings

Adjust parsing or preprocessing in `EmployeeDashboard.py` as needed.

### 🎨 Styling Issues

* Use a modern browser (Chrome, Firefox, Edge) for best CSS support

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```
4. Push the branch:

   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request on GitHub

---

## 📜 License

**MIT License** – see `LICENSE` file for full details.

---

## 📬 Contact

For issues or suggestions:

* [Open an issue on GitHub](https://github.com/HerveMucyo/EmployeeDashboard/issues)
* Contact the repository owner directly.

---

Would you like this as a downloadable PDF or formatted for a specific platform (e.g., GitHub README, Word, Google Docs)?
