"""Student Marks Analyzer using NumPy.

Day 01 project for the 90 Days AI/ML Engineer Roadmap.
The goal is to practice arrays, vectorized calculations, and simple summaries.
"""

import numpy as np


def print_student_summary(student_names, subject_names, marks):
    """Print total, average, highest, and lowest marks for each student."""
    totals = np.sum(marks, axis=1)
    averages = np.mean(marks, axis=1)
    highest_marks = np.max(marks, axis=1)
    lowest_marks = np.min(marks, axis=1)

    print("Student Performance Summary")
    print("-" * 60)

    for index, name in enumerate(student_names):
        subject_marks = {
            str(subject): int(mark)
            for subject, mark in zip(subject_names, marks[index])
        }

        print(f"Student: {name}")
        print(f"Marks: {subject_marks}")
        print(f"Total Marks: {totals[index]}")
        print(f"Average Marks: {averages[index]:.2f}")
        print(f"Highest Mark: {highest_marks[index]}")
        print(f"Lowest Mark: {lowest_marks[index]}")
        print("-" * 60)


def print_class_summary(subject_names, marks):
    """Print class-level averages for each subject and the full class."""
    subject_averages = np.mean(marks, axis=0)
    overall_average = np.mean(marks)

    print("Class Summary")
    print("-" * 60)

    for subject, average in zip(subject_names, subject_averages):
        print(f"{subject} Average: {average:.2f}")

    print(f"Overall Class Average: {overall_average:.2f}")


def main():
    student_names = np.array(["Ali", "Sara", "Ahmed", "Fatima"])
    subject_names = np.array(["Math", "Python", "Statistics"])

    # Rows represent students. Columns represent subjects.
    marks = np.array(
        [
            [78, 85, 90],
            [88, 92, 80],
            [70, 75, 82],
            [95, 89, 91],
        ]
    )

    print_student_summary(student_names, subject_names, marks)
    print_class_summary(subject_names, marks)


if __name__ == "__main__":
    main()
