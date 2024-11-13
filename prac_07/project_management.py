"""
CP1404 - Practical 7
Program: Project Management

Estimated : 1 hour
Actual    :
"""

import datetime
from prac_07.project import Project

FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")


    print_menu()
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            load_projects()
        elif choice == "S":
            save_projects()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects()
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid menu choice")
    print("Thank you for using custom-built project management software.")

def print_menu():
    """Display menu of choices to user."""
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
          "- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def load_projects():
    """Load a list of projects from a file."""

    projects = []
    FILENAME = input("Enter file name: ")

    try:
        with open(FILENAME, "r") as in_file:

            in_file.readline()
            for line in in_file:
                name, start_date_string, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
                project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
                projects.append(project)

        print(f"Loaded {len(projects)} projects from {FILENAME}")
        return projects

    except FileNotFoundError:
        print("File not found.")

def save_projects(projects):
    """Save a list of projects to file."""

    FILENAME = input("Enter file name: ")

    with open(FILENAME, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {FILENAME}")

def display_projects(projects):
    """Display a list of projects."""
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")

def filter_projects(projects):
    """Filter a list of projects by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.start_date > date]

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
        print(f"{i}. {project.name}")

    project_index = int(input("Project choice: ")) - 1
    project_to_update = projects[project_index]

    new_percentage = int(input("New percentage: "))
    new_priority = int(input("New priority: "))

    project_to_update.completion_percentage = new_percentage
    project_to_update.priority = new_priority

main()




