# Employee Attendance Analyzer

## Overview

The Employee Attendance Analyzer is a Python program that analyzes employee attendance data. The program uses Pandas to clean and analyze the data and Matplotlib to create a graph.

The program answers two questions:

1. Which employee worked the most total hours?
2. What was the most common attendance status?

The program also creates a bar graph showing the top 10 employees by total hours worked.

## Dataset

The dataset contains employee attendance records for February 2026. It includes employee IDs, dates, time in, time out, hours worked, and attendance status.

The dataset was obtained from a free public GitHub dataset.

The program cleans some of the data before analyzing it. Employee IDs are converted to a consistent format, values such as "8 hrs" are converted to numbers, and different spellings of attendance statuses are grouped into the same category.

## Analysis Questions

### Question 1: Which employee worked the most total hours?

The program converts the Hours Worked column into numbers and groups the records by EmployeeID. It then adds the hours for each employee and sorts the results from highest to lowest.

The result shows that **EMP022 worked the most total hours with 155.5 hours**.

This analysis uses data conversion, aggregation, and sorting.

### Question 2: What was the most common attendance status?

The program cleans the Status column so that different versions of the same status are counted together. It then counts the number of records for each status.

The result shows that **Present was the most common attendance status with 671 records**.

This analysis uses data conversion and counting.

## Graph

The program creates a bar graph showing the top 10 employees by total hours worked. The graph makes it easier to compare the employees with the highest total hours.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Visual Studio Code

## How to Run the Program

1. Make sure Python is installed.
2. Install the required libraries:

py -m pip install pandas matplotlib


3. Place `attendance.csv` in the same folder as `main.py`.
4. Open the project folder in Visual Studio Code.
5. Open the terminal.
6. Run:


py main.py


The program will display the analysis results in the terminal and open the graph.

## Project Files

* `main.py` - Contains the Python program and analysis functions.
* `attendance.csv` - Contains the employee attendance dataset.
* `README.md` - Contains information about the project and how to use it.