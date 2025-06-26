Employee Data Dashboard
Overview
The Employee Data Dashboard is a Streamlit-based web application that visualizes employee data from a CSV file (employee_data.csv). It provides interactive charts and metrics, including:
•	Key Metrics: Total employees, average salary, and average age.
•	Charts:
o	Pie chart for department distribution.
o	Histogram for salary distribution.
o	Scatter plot for age vs. salary.
o	Line charts for hiring and exit trends.
•	Filters: Department, age range, and salary range.
•	Data Table: Displays filtered employee data.
•	Download Option: Export filtered data as CSV.
The dashboard features a modern UI with a gradient background, glassmorphism cards, Poppins font, fade-in animations, and hover effects (cards lift, buttons scale, table rows highlight).
Prerequisites
•	Python: Version 3.8 or higher.
•	Virtual Environment: Recommended for dependency management.
•	Git: For cloning the repository.
•	Streamlit Cloud Account: For deployment (optional).
Installation
Local Setup
1.	Clone the Repository:
2.	git clone https://github.com/HerveMucyo/EmployeeDashboard.git
3.	cd EmployeeDashboard
4.	Create a Virtual Environment:
5.	python -m venv .venv
o	On Windows:
o	.\.venv\Scripts\Activate.ps1
o	On macOS/Linux:
o	source .venv/bin/activate
6.	Install Dependencies:
Ensure requirements.txt is in the project root:
7.	streamlit==1.38.0
8.	pandas==2.2.3
9.	plotly==6.1.2
10.	openpyxl==3.1.5
11.	numpy==2.3.1
Install them:
pip install -r requirements.txt
12.	Verify CSV File:
Ensure employee_data.csv is in the project root. Expected columns:
o	ID, Name, Department, Annual Salary, Age, Hire Date, Exit Date
Update csv_path in EmployeeDashboard.py if the CSV is in a subdirectory (e.g., data/employee_data.csv).
13.	Run the Dashboard:
14.	streamlit run EmployeeDashboard.py
Open http://localhost:8501 in a browser.
Streamlit Cloud Deployment
1.	Push to GitHub:
Ensure the repository contains:
o	EmployeeDashboard.py
o	employee_data.csv
o	requirements.txt
2.	git add EmployeeDashboard.py employee_data.csv requirements.txt
3.	git commit -m "Update project files"
4.	git push
5.	Deploy on Streamlit Cloud:
o	Go to Streamlit Cloud.
o	Connect your GitHub repository (HerveMucyo/EmployeeDashboard).
o	Set the main script to EmployeeDashboard.py.
o	Deploy and check logs (Manage app > Logs) for errors.
Usage
•	Filters: Use the sidebar to filter by department, age range, or salary range.
•	Visualizations: View interactive charts (pie, histogram, scatter, line).
•	Data Table: Browse filtered employee data.
•	Download: Click "Download Filtered Data" to export as CSV.
•	Styling: Enjoy a modern UI with a blue gradient background, glassmorphism cards, Poppins font, and animations (fade-in, hover effects).
Data Requirements
The employee_data.csv should include:
•	Columns: ID, Name, Department, Annual Salary, Age, Hire Date, Exit Date.
•	Formats:
o	Annual Salary: Numeric or cleanable (e.g., $50,000).
o	Hire Date, Exit Date: Dates (e.g., MM/DD/YYYY, DD-MM-YYYY, YYYY-MM-DD).
•	Known Issues:
o	915 invalid Exit Date values (e.g., N/A, Unknown) are excluded from the exit trend chart.
o	Annual Salary may show as None due to invalid values or column name mismatches.
o	Run locally and check debugging output (Columns in your CSV, Sample data, Unique values, Warnings) to resolve.
Troubleshooting
•	ModuleNotFoundError: plotly.express:
o	Ensure plotly==6.1.2 is in requirements.txt.
o	Redeploy on Streamlit Cloud and check logs.
•	Invalid Data:
o	Check debugging output in the dashboard:
	Columns in your CSV
	Sample data
	Unique 'Exit Date' values and Unique 'Annual Salary' values
	Warnings
o	Update EmployeeDashboard.py to handle specific invalid values or date formats.
•	Styling Issues:
o	Use a modern browser (Chrome, Firefox, Edge) for full CSS support.
Contributing
1.	Fork the repository.
2.	Create a branch (git checkout -b feature/your-feature).
3.	Commit changes (git commit -m "Add your feature").
4.	Push to the branch (git push origin feature/your-feature).
5.	Open a pull request.
License
MIT License. See LICENSE for details.
Contact
For issues or suggestions, open an issue on GitHub or contact the repository owner.

