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
LOWEST_PRIORITY = 1
HIGHEST_PRIORITY = 9
MINIMUM_PERCENTAGE = 0
MAXIMUM_PERCENTAGE = 100
MINIMUM_COST = 0.0
MAXIMUM_COST = 999999999.9

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

def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    if not projects:
        print("No projects to display")
        return

    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.is_completed():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)

    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects: ")
    if not incomplete_projects:
            print("  All projects have been completed.")
    else:
            for project in sorted(incomplete_projects):
                    print(f'  {project}')

    print("Completed projects: ")
    if not completed_projects:
            print("  No project has been completed yet.")
    else:
            for project in sorted(completed_projects):
                    print(f'  {project}')

def filter_projects(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date."""
    if not projects:
        print("No projects to filter")
    else:
        date_string = get_valid_date("Show projects that start after date (dd/mm/yy): ")
        date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()

        filtered_projects = [project for project in projects
                             if datetime.datetime.strptime(project.start_date, DATE_FORMAT).date() >= date]

        if not filtered_projects:
            print(f"No project starts after {date_string}")
        else:
            for filtered_project in filtered_projects:
                filtered_project.start_date = (
                    datetime.datetime.strptime(filtered_project.start_date, DATE_FORMAT).date())
            filtered_projects.sort(key=attrgetter('start_date'))

            for filtered_project in filtered_projects:
                filtered_project.start_date = filtered_project.start_date.strftime(DATE_FORMAT)
                print(filtered_project)

def get_valid_date(prompt):
    """Get valid dat."""
    while True:
        try:
            date_string = input(prompt)
            datetime.datetime.strptime(date_string, DATE_FORMAT).date()
            break
        except ValueError:
            print("Invalid date format")
    return date_string

def add_project(projects):
    """Ask the user for the inputs and add a new project to memory."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ", int, LOWEST_PRIORITY, HIGHEST_PRIORITY)
    cost_estimate = get_valid_number("Cost estimate: $", float, MINIMUM_COST, MAXIMUM_COST)
    completion_percentage = get_valid_number("Percent complete: ", int, MINIMUM_PERCENTAGE, MAXIMUM_PERCENTAGE)
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
