# Day 03: Pandas Data Cleaning and Filtering

## Goal

Learn how to clean and explore tabular data using Pandas before moving deeper into machine learning.

Day 01 focused on NumPy arrays. Day 02 introduced Pandas DataFrames. Day 03 builds on that by handling common real-world data problems such as missing values, duplicate rows, data types, filtering, sorting, and grouped summaries.

## Learning Objectives

- Detect missing values in a DataFrame
- Fill missing numeric values using mean values
- Inspect column data types
- Detect duplicate rows
- Count values in a category column
- Filter rows using conditions
- Group data by a category
- Sort data for easier analysis

## Concepts Learned

### Missing Values

Missing values are empty or unknown values in a dataset. In Pandas, they often appear as `NaN`.

```python
df.isnull().sum()
```

This checks how many missing values exist in each column.

### Data Cleaning

Data cleaning means preparing raw data so it becomes more useful and reliable.

In this project:

- Missing `Age` values are filled with the average age.
- Missing `Salary` values are filled with the average salary.
- Duplicate rows are detected before analysis.

### Data Types

Data types show what kind of values each column contains.

```python
df.dtypes
```

This matters because numeric columns can be used for calculations, while text columns are usually used for categories or labels.

### Filtering Data

Filtering means selecting rows that match a condition.

```python
df[df["Salary"] > 55000]
```

This returns only employees with a salary greater than `55000`.

### Duplicate Detection

Duplicate rows can make analysis misleading because the same record may be counted more than once.

```python
df.duplicated().sum()
```

This counts how many duplicate rows exist.

### Value Counts

Value counts show how often each category appears.

```python
df["Department"].value_counts()
```

This is useful for quickly understanding category distribution.

### GroupBy

GroupBy is used to summarize data by category.

```python
df.groupby("Department")["Salary"].mean()
```

This calculates the average salary for each department.

### Sorting

Sorting helps organize data from highest to lowest or lowest to highest.

```python
df.sort_values("Salary", ascending=False)
```

This sorts employees by salary from highest to lowest.

## Mini Project: Employee Data Analyzer

The project creates a small employee dataset with missing values and duplicate records, then cleans and analyzes it using Pandas.

The project includes:

- Employee DataFrame creation
- Missing value detection
- Missing value filling
- Data type inspection
- Duplicate row detection
- Department value counts
- Salary filtering
- Department-wise salary analysis
- Salary-based sorting

## Project Structure

```text
Day-03/
├── README.md
├── resources.md
├── project/
│   ├── employee_data_analyzer.py
│   └── requirements.txt
└── screenshots/
```

## How To Run

From the `Day-03/project/` folder:

```bash
pip install -r requirements.txt
python employee_data_analyzer.py
```

## Output

The project prints the original employee dataset, missing value summary, data types, duplicate count, cleaned dataset, filtered employees, department counts, grouped salary summary, and sorted employees in the terminal.

After running the project, save a terminal screenshot in the `screenshots/` folder.

## Skills Demonstrated

- Creating Pandas DataFrames
- Inspecting dataset quality
- Cleaning missing numeric values
- Reading and understanding data types
- Filtering rows with conditions
- Detecting duplicate records
- Counting category values
- Grouping and summarizing data
- Sorting tabular data
- Writing readable beginner-friendly Python code

## Real-World Applications

These skills are used in real AI/ML work before model training.

Examples:

- Cleaning employee, customer, sales, or student datasets
- Preparing data for dashboards
- Checking whether a dataset is reliable
- Finding missing or duplicated records
- Creating simple summaries for business decisions
- Preparing clean features for machine learning models

## Key Takeaways

- Clean data is more important than complex code.
- Missing values should be detected before analysis.
- Data types help decide which operations are possible.
- Filtering, grouping, and sorting are core Pandas skills.
- Data cleaning is one of the first professional habits in ML projects.

## Reflection

Today I learned how to move from simply creating a DataFrame to preparing a dataset for real analysis. Missing values, duplicates, and unclear categories can affect results, so it is important to inspect and clean data before drawing conclusions.

This project helped me understand that machine learning starts before model training. A good AI/ML engineer first checks the data, cleans it, and makes sure the analysis is based on reliable information.

## Next Steps

- Add more employee records for extra practice.
- Save the cleaned data to a CSV file.
- Add a screenshot of the terminal output.
- Continue to Day 04 and visualize the cleaned employee data with Matplotlib.
