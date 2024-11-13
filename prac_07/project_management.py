"""
CP1404 - Practical 7
Program: Project Management

Estimated : 1 hour
Actual    : 3 days
"""

import datetime
from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"

def main():
    """Print welcome message, load file and print menu."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    print_menu()
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter the filename to load projects from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Enter the filename to save projects to: ").strip()
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print_menu()
        choice = input(">>> ").strip().upper()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().upper()
    if save_choice == 'YES':
        save_projects(projects, DEFAULT_FILENAME)
    print("Thank you for using custom-built project management software.")

def print_menu():
    """Display menu of choices to user."""
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
          "- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def load_projects(filename):
    """Load a list of projects from a file."""
    projects = []
    try:
        with open(filename, "r") as in_file:
            in_file.readline()

            for line in in_file:
                name, start_date_string, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                projects.append(project)

            return projects

    except FileNotFoundError:
        print("File not found.")

def save_projects(projects, filename):
    """Save a list of projects to file."""

    with open(filename, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    """Display a list of projects."""

    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]

    print("Incomplete projects: ")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects: ")
    for project in sorted(completed_projects):
        print(f"  {project}")

def filter_projects(projects):
    """Filter a list of projects by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.start_date >= date]

    for project in filtered_projects:
        print(project)

def add_project(projects):
    """Add a new project to the list of projects."""
    print("Let's add a new project")

    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    """Update a project from the list of projects."""
    for i, project in enumerate(projects, 1):
        print(f"{i}. {project}")

    project_index = int(input("Project choice: ")) - 1
    project_to_update = projects[project_index]

    new_percentage = input("New percentage: ")
    new_priority = input("New priority: ")

    if new_percentage != "":
        project_to_update.completion_percentage = int(new_percentage)

    if new_priority != "":
        project_to_update.priority = int(new_priority)

main()




