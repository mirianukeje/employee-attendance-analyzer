# Overview

As a software engineer, I am learning how to use Python and data analysis libraries to work with real-world data. For this project, I created an Employee Attendance Analyzer that reads attendance records, cleans the data, analyzes the results, and presents the findings in a graph.

The dataset contains employee attendance records for February 2026. It includes employee IDs, dates, time in, time out, hours worked, and attendance status. I obtained the dataset from a free public GitHub repository:

https://github.com/LibaMariyamK/powerquery-project-hr-analytics

The purpose of writing this software is to practice using Python and Pandas to analyze a real dataset and answer questions based on the data. The program cleans inconsistent data, converts hours worked into numbers, groups and sorts employee records, counts attendance statuses, and creates a graph to make the results easier to understand.

# Data Analysis Results

### Question 1: Which employee worked the most total hours?

The program converted the Hours Worked values into numbers and grouped the records by employee. It then added the total hours for each employee and sorted the results from highest to lowest.

**Answer:** EMP022 worked the most total hours with **155.5 hours**.

### Question 2: What was the most common attendance status?

The program cleaned the different versions of the attendance statuses and counted how many times each status appeared.

**Answer:** **Present** was the most common attendance status with **671 records**.

The program also creates a bar graph showing the top 10 employees by total hours worked.

# Development Environment

I developed this software using:

* Visual Studio Code
* Python
* Git
* GitHub

The programming language used was **Python**. I used the following libraries:

* **Pandas** for reading, cleaning, converting, grouping, sorting, and analyzing the attendance data.
* **Matplotlib** for creating the bar graph.

# Useful Websites

* [GitHub Dataset](https://github.com/LibaMariyamK/powerquery-project-hr-analytics)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib Documentation](https://matplotlib.org/stable/)
* [Python Documentation](https://docs.python.org/3/)

# Future Work

* Add more analysis questions to provide additional information about employee attendance.
* Add more graphs to compare attendance statuses and employee performance.
* Add date-based analysis to compare attendance across different days or weeks.
* Improve the handling of missing attendance data.