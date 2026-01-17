import pandas as pd
import numpy as np

# 1. Data Creation & Loading

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Ali", "Sara", "Usman", "Ayesha", "Bilal", "Hina", "Hamza", "Zara"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [70000, 65000, None, 80000, None, 75000, 90000, 60000],
    "Years_Experience": [6, 4, 8, 10, 3, 7, 12, 5]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# 2. Data Cleaning

# Identify missing salary values
print("\nMissing Salary Values:\n")
print(df["Salary"].isna())

# Replace missing salaries with median salary
median_salary = df["Salary"].median()
df["Salary"].fillna(median_salary, inplace=True)

# Set Emp_ID as index
df.set_index("Emp_ID", inplace=True)

print("\nCleaned DataFrame:\n")
print(df)

# -------------------------------
# 3. Data Analysis & Filtering
# -------------------------------

# Employees with more than 5 years of experience
experienced_employees = df[df["Years_Experience"] > 5]

print("\nEmployees with More Than 5 Years Experience:\n")
print(experienced_employees)

# Department-wise total salary and average experience
department_analysis = df.groupby("Department").agg(
    Total_Salary_Expense=("Salary", "sum"),
    Average_Experience=("Years_Experience", "mean")
)

print("\nDepartment-wise Analysis:\n")
print(department_analysis)

# Sort employees by salary (descending)
sorted_by_salary = df.sort_values(by="Salary", ascending=False)

print("\nEmployees Sorted by Salary (Descending):\n")
print(sorted_by_salary)
# -------------------------------
# 4. Exporting Results
# -------------------------------

sorted_by_salary.to_csv("Processed_Employee_Data.csv")

print("\nFile 'Processed_Employee_Data.csv' has been saved successfully.")
