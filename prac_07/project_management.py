"""
Project Management
Estimate: 60 minutes
Actual:
"""
import datetime
from operator import attrgetter
from prac_07.project import Project

FILENAME = 'projects.txt'
MENU = ('- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n'
        '- (A)dd new project\n- (U)pdate project\n- (Q)uit')
DATE_FORMAT = '%d/%m/%Y'

def main():
    """Menu-driven project management software with options to load, save, display, filter, add, and update projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print()
        print(MENU)
        choice = input(">>> ").strip().upper()
        if choice == 'Q':
            break
        elif choice == 'L':
            load_new_projects(projects)
        elif choice == 'S':
            proceed_saving_task(projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects(projects)
        elif choice == 'A':
            add_project(projects)
        elif choice == 'U':
            update_projects(projects)
        else:
            print("Invalid menu choice")

    save_choice = input("Would you like to save changes to projects.txt? (Y/N): ").strip().upper()
    if save_choice == 'Y':
        save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects

def save_projects(projects, filename):
    """Save projects to a file."""
    header = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n"
    lines = [header]
    for project in projects:
        line = (f"{project.name}\t{project.start_date}\t{project.priority}\t"
                f"{project.cost_estimate}\t{project.completion_percentage}\n")
        lines.append(line)
    with open(filename, 'w') as out_file:
        out_file.writelines(lines)
    print(f"Saved {len(projects)} projects to {filename}")

def load_new_projects(projects):
    """Prompt the user for a filename, load additional projects from it, and append them to the existing list."""
    while True:
        try:
            filename = input("Filename to load: ")
            new_projects = load_projects(filename)
            break
        except FileNotFoundError:
            print("File not found, please enter a valid filename.")
    projects += new_projects
    print(f"Loaded {len(new_projects)} projects from {filename}, total {len(projects)} projects now.")

def proceed_saving_task(projects):
    """Save projects to a file."""
    filename = input("Filename to save: ")
    save_projects(projects, filename)