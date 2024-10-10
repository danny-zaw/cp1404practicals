"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_subject_data()
    print_subject_details(subject_data)


def load_subject_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts)
    input_file.close()
    return subject_data

def print_subject_details(subject_data):
    """Print subject details with subject code, lecturer and number of students."""
    for data in subject_data:
        print("{} is taught by {} and has {} students.".format(*data))

main()