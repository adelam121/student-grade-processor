import sys
from process_data import process_grades

if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    else:
        input_file = 'students.csv'
    process_grades(input_file)
