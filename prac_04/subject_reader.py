"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject data from file and print subject details."""
    records = load_subject_data()
    print_subject_details(records)


def load_subject_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    records = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        records.append(parts)
    input_file.close()
    return records

def print_subject_details(records):
    """Print subject details with subject code, lecturer and number of students."""
    for record in records:
        print("{} is taught by {} and has {} students.".format(*record))

main()