"""
CP1404 - Project exercice
Time estimate: 40 mins
Actual time: 3 days
"""
from Practical_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- " \
       "(U)pdate project\n- (Q)uit"
WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
VALID_CHOICES = ['L', 'S', 'D', 'F', 'A', 'U', 'Q']


def main():
    print(WELCOME_MESSAGE)
    projects = load_data(FILENAME)
    print(f"Loaded {len(projects)} projects.")
    choice = get_valid_menu_choice(">>> ")
    while choice.upper() != "Q":
        if choice == "L":
            file_name = input("Enter filename: ")
            try:
                projects = load_data(file_name)
            except FileNotFoundError:
                print("File could not be found")

        elif choice == "S":
            file_name = input("What file to save to?: ")
            write_data(projects, file_name)
            print(f"Saved {len(projects)} projects to {file_name}.")

        elif choice == "D":
            finished_projects, unfinished_projects = check_completion(projects)
            print()
            print("Finished projects")
            [print(f"{i + 1}: {project}") for i, project in enumerate(sorted(finished_projects))]
            print()
            print("Unfinished projects")
            [print(f"{i + 1}: {project}") for i, project in enumerate(sorted(unfinished_projects))]
            print()

        elif choice == "F":
            filter_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filtered_projects = filter_projects(filter_date, projects)
            sorted_projects = sorted(filtered_projects)
            for project in sorted_projects:
                print(project)

        elif choice == "A":
            print("Let's add a new project")
            get_new_project(projects)

        elif choice == "U":
            print("Update project")
            display_projects_with_indices(projects)
            project_index = get_valid_project_index(len(projects))
            new_completion = get_valid_number("Enter new completion percentage: ")
            projects[project_index].new_percentage(new_completion)
            new_priority = int(get_valid_number("Enter new priority: "))
            projects[project_index].update_priority(new_priority)
            print("Project updated successfully.")
        choice = get_valid_menu_choice(">>> ")


def display_projects_with_indices(projects):
    """Displays enumerated projects"""
    for i, project in enumerate(projects):
        print(f"{i + 1}: {project}")


def get_valid_project_index(max_index):
    """Get a valid index for project selection"""
    while True:
        try:
            project_number = int(input(f"Enter project number: "))
            if 1 <= project_number <= max_index:
                return project_number - 1  # converts project number back to an index
            else:
                print(f"Invalid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def filter_projects(filter_date, projects):
    """Filters out projects to be completed before a user specified date"""
    filtered_objects = []
    for project in projects:
        if project.compare_date(filter_date):
            filtered_objects.append(project)
    return filtered_objects


def get_new_project(projects):
    """Prompts the user for new project details"""
    name = input("Project name: ")
    start_date = get_valid_date("Project start date format(dd/mm/yyy): ")
    priority = int(get_valid_number("Priority level: "))
    estimate_cost = float(get_valid_number("Estimate cost: "))
    completion = float(get_valid_number("Completion percentage: "))
    project = Project(name, start_date, priority, estimate_cost, completion)
    projects.append(project)


def load_data(filename):
    """Loads data from a user specified file"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # reads the header line to skip it
        for line in in_file:
            parts = line.strip().split("\t")  # Data in this file is split using tabs
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            estimate_cost = float(parts[3])
            completion = int(parts[4])
            project = Project(name, start_date, priority, estimate_cost, completion)
            projects.append(project)
    return projects


def write_data(projects, file_name):
    """Exports data to a user specified file as tab separated values"""
    with open(file_name, "w") as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.estimate_cost}\t"
                f"{project.completion_percentage}\n")


def get_valid_menu_choice(prompt):
    """Re prompts the user for a valid menu choice"""
    print(MENU)
    while True:
        choice = input(prompt).upper()
        if len(choice) == 1 and choice in VALID_CHOICES:  # valid inputs are 1 letter and in the valid list
            return choice
        else:
            print("This is not a valid choice")


def get_valid_date(prompt):
    """Checks if th inputted date is stored in the correct format"""
    valid_format = False
    while not valid_format:
        project_date = input(prompt)
        try:
            datetime.strptime(project_date, "%d/%m/%Y")  # if it can be converted the date format is valid
            valid_format = True
        except ValueError:
            print("Invalid date")
    return project_date


def get_valid_number(prompt):
    """Ensures the value entered is a number and is above 0"""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:  # prevents the use of non-valid numbers
                return number
            else:
                print("Number must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def check_completion(projects):
    """Sorts projects into complete and incomplete categories"""
    finished_projects = []
    unfinished_project = []
    for project in projects:
        if project.completion_percentage == 100:
            finished_projects.append(project)
        else:
            unfinished_project.append(project)
    return finished_projects, unfinished_project


main()
