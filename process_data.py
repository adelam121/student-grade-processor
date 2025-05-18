import csv
from utils import calculate_average, assign_grade

def process_grades(input_file):
    students = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name, math, science, english = row
            average = calculate_average([int(math), int(science), int(english)])
            grade = assign_grade(average)
            students.append([name, average, grade])

    with open('student_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Average', 'Grade'])
        writer.writerows(students)

    print("Results saved to student_results.csv")
