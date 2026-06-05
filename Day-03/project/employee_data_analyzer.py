"""Employee Data Analyzer using Pandas.

Day 03 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to practice missing values, data cleaning, filtering, and summaries.
"""

import pandas as pd


SALARY_FILTER_AMOUNT = 55000


def build_employee_dataframe():
    """Create a small employee dataset with missing and duplicate values."""
    employee_data = {
        "Employee": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman", "Sara"],
        "Department": ["IT", "HR", "Finance", "IT", "Marketing", "HR"],
        "Age": [24, None, 29, 31, None, None],
        "Salary": [50000, 62000, None, 58000, 54000, 62000],
        "Experience": [2, 4, 5, 6, 3, 4],
    }

    return pd.DataFrame(employee_data)


def clean_employee_data(df):
    """Fill missing numeric values with column averages."""
    cleaned_df = df.copy()

    average_age = cleaned_df["Age"].mean()
    average_salary = cleaned_df["Salary"].mean()

    cleaned_df["Age"] = cleaned_df["Age"].fillna(average_age)
    cleaned_df["Salary"] = cleaned_df["Salary"].fillna(average_salary)

    return cleaned_df


def print_dataset_overview(df):
    """Print the original dataset and basic quality checks."""
    print("Original Employee Dataset")
    print("=" * 60)
    print(df.to_string(index=False))

    print("\nMissing Values")
    print("-" * 60)
    print(df.isnull().sum().to_string())

    print("\nData Types")
    print("-" * 60)
    print(df.dtypes.to_string())

    print("\nDuplicate Rows")
    print("-" * 60)
    print(f"Duplicate row count: {df.duplicated().sum()}")


def print_cleaning_results(cleaned_df):
    """Print the cleaned dataset and category counts."""
    print("\nCleaned Employee Dataset")
    print("=" * 60)
    print(cleaned_df.to_string(index=False))

    print("\nMissing Values After Cleaning")
    print("-" * 60)
    print(cleaned_df.isnull().sum().to_string())

    print("\nDepartment Counts")
    print("-" * 60)
    print(cleaned_df["Department"].value_counts().to_string())


def print_employee_insights(cleaned_df):
    """Print filtered, grouped, and sorted employee insights."""
    high_salary_employees = cleaned_df[
        cleaned_df["Salary"] > SALARY_FILTER_AMOUNT
    ]
    department_salary_summary = cleaned_df.groupby("Department")["Salary"].mean()
    sorted_by_salary = cleaned_df.sort_values("Salary", ascending=False)

    print(f"\nEmployees With Salary Greater Than {SALARY_FILTER_AMOUNT}")
    print("-" * 60)
    print(high_salary_employees.to_string(index=False))

    print("\nAverage Salary By Department")
    print("-" * 60)
    print(department_salary_summary.to_string())

    print("\nEmployees Sorted By Salary")
    print("-" * 60)
    print(sorted_by_salary.to_string(index=False))


def main():
    employee_df = build_employee_dataframe()

    print_dataset_overview(employee_df)

    cleaned_employee_df = clean_employee_data(employee_df)

    print_cleaning_results(cleaned_employee_df)
    print_employee_insights(cleaned_employee_df)


if __name__ == "__main__":
    main()
