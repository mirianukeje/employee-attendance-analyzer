import pandas as pd
import matplotlib.pyplot as plt


# Load the attendance dataset
def load_data():
    """Read the attendance CSV file and return the data."""
    data = pd.read_csv("attendance.csv")
    return data


# Clean the employee ID column
def clean_employee_ids(data):
    """Clean employee IDs and remove rows that are not employee records."""
    data["EmployeeID"] = data["EmployeeID"].astype(str).str.strip().str.upper()

    # Keep only rows with a valid employee ID such as EMP001
    data = data[
        data["EmployeeID"].str.match(r"^EMP\d+$", na=False)
    ]

    return data


# Clean the hours worked column
def clean_hours(data):
    """Convert hours worked values into numbers."""
    data["Hours Worked"] = (
        data["Hours Worked"]
        .astype(str)
        .str.replace("hrs", "", regex=False)
        .str.strip()
    )

    data["Hours Worked"] = pd.to_numeric(
        data["Hours Worked"],
        errors="coerce"
    )

    # Missing or invalid hours are treated as zero
    data["Hours Worked"] = data["Hours Worked"].fillna(0)

    return data


# Clean the attendance status column
def clean_status(data):
    """Convert different status spellings into consistent categories."""
    data["Status"] = (
        data["Status"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    data["Status"] = data["Status"].replace({
        "p": "Present",
        "present": "Present",
        "absent": "Absent",
        "a": "Absent",
        "leave": "Leave",
        "on leave": "Leave",
        "half day": "Half Day",
        "hd": "Half Day",
        "ol": "Leave"
    })

    data["Status"] = data["Status"].replace(
        "nan",
        "Unknown"
    )

    return data


# Calculate total hours for each employee
def calculate_employee_hours(data):
    """Add the hours worked by each employee and sort the results."""
    employee_hours = (
        data.groupby("EmployeeID")["Hours Worked"]
        .sum()
        .sort_values(ascending=False)
    )

    return employee_hours


# Count each attendance status
def calculate_status_counts(data):
    """Count how many times each attendance status appears."""
    status_counts = data["Status"].value_counts()

    return status_counts


# Display the answers to the analysis questions
def display_results(employee_hours, status_counts):
    """Display the results of the two analysis questions."""
    print("Employee Attendance Analyzer")
    print("----------------------------")

    print("\nQuestion 1:")
    print("Which employee worked the most total hours?")

    print("\nTotal hours worked by employee:")
    print(employee_hours)

    highest_employee = employee_hours.idxmax()
    highest_hours = employee_hours.max()

    print("\nAnswer:")
    print(
        highest_employee,
        "worked the most total hours with",
        highest_hours,
        "hours."
    )

    print("\nQuestion 2:")
    print("What was the most common attendance status?")

    print("\nAttendance status counts:")
    print(status_counts)

    most_common_status = status_counts.idxmax()
    most_common_count = status_counts.max()

    print("\nAnswer:")
    print(
        most_common_status,
        "was the most common status with",
        most_common_count,
        "records."
    )


# Create a graph showing the top 10 employees
def create_graph(employee_hours):
    """Create a bar graph showing the top 10 employees by total hours."""
    top_employees = employee_hours.head(10)

    plt.figure(figsize=(10, 6))

    plt.bar(
        top_employees.index,
        top_employees.values
    )

    plt.title("Top 10 Employees by Total Hours Worked")
    plt.xlabel("Employee ID")
    plt.ylabel("Total Hours Worked")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Main function that runs the program
def main():
    """Run the employee attendance analysis."""
    data = load_data()

    # Clean the data before performing the analysis
    data = clean_employee_ids(data)
    data = clean_hours(data)
    data = clean_status(data)

    # Perform the two required analyses
    employee_hours = calculate_employee_hours(data)
    status_counts = calculate_status_counts(data)

    # Display the answers
    display_results(employee_hours, status_counts)

    # Display the graph
    create_graph(employee_hours)


# Start the program
if __name__ == "__main__":
    main()