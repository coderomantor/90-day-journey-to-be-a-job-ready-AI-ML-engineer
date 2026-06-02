import numpy as np

marks = np.array([78, 85, 90, 67, 88])

print("Student Marks Analyzer")
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Total:", np.sum(marks))
def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def analyze_student_marks(students):
    for name, marks in students.items():
        total = calculate_total(marks)
        average = calculate_average(marks)
        highest = max(marks)
        lowest = min(marks)

        print(f"Student: {name}")
        print(f"Marks: {marks}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Highest Mark: {highest}")
        print(f"Lowest Mark: {lowest}")
        print("-" * 30)


students = {
    "Ali": [78, 85, 90],
    "Sara": [88, 92, 80],
    "Ahmed": [70, 75, 82],
}

analyze_student_marks(students)
