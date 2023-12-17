"""
Project Management - client program
Estimated time: 4 hours
Actual time: 5 hours
"""
from datetime import datetime
from prac_07.project import Project

MENU = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""
COMPLETE_PROJECT_PERCENTAGE = 100


def main():
    """Get file name for user to load, save, display, add, filter, and update projects"""
    print(MENU)
    projects = []
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # file_name_to_load = "projects.txt"
            file_name_to_load = input("Enter file name to load project: ")
            try:
                load_projects_from_file(file_name_to_load, projects)
                for project in projects:
                    print(project)
            except FileNotFoundError:
                print("File not found")

        elif choice == "S":
            if not projects:
                print("No file to save.")
            else:
                file_name_to_save = input("Enter file name to save project: ")
                save_file(file_name_to_save, projects)

        elif choice == "D":
            projects.sort()
            if not projects:
                print("No project yet.")
            else:
                display_incomplete_project(projects)
                display_complete_project(projects)

        elif choice == "F":
            try:
                input_date_string = input("Show projects that start after date (dd/mm/yy): ")
                input_date = datetime.strptime(input_date_string, "%d/%m/%Y").date()
                display_filtered_project(input_date, projects)
            except ValueError:
                print("Invalid input")

        elif choice == "A":
            print("Let's add new project")
            try:
                add_new_project(projects)
                for project in projects:
                    print(project)
            except ValueError:
                print("Invalid input")

        elif choice == "U":
            if not projects:
                print("No projects yet")
            else:
                for number, project in enumerate(projects):
                    print(number, project)
                project_choice = int(input("Project choice: "))
                for number, project in enumerate(projects):
                    if project_choice == number:
                        new_percentage = input("New Percentage: ")
                        new_priority = input("New Priority: ")
                        if new_percentage and new_priority != "":
                            display_updated_project(new_percentage, new_priority, project)
                        else:
                            print(project)

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


print("Thank you for using custom-built project management software.")


def add_new_project(projects):
    """Add new project to projects"""
    project_name = input("Name: ")
    date_string = input("Date (d/m/yyyy): ")
    date = datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    project = Project(project_name, date, priority, cost_estimate, percent_complete)
    projects.append(project)


def display_filtered_project(input_date, projects):
    """Display filtered project by date"""
    for project in projects:
        if project.is_greater(input_date):
            print(project)


def display_updated_project(new_percentage, new_priority, project):
    """Display updated project with new percentage and new priority"""
    project.completion_percentage = int(new_percentage)
    project.priority = int(new_priority)
    print(project)


def load_projects_from_file(file_name_to_load, projects):
    """Load projects from text file"""
    in_file = open(file_name_to_load, 'r')
    in_file.readline()
    for project_line in in_file:
        parts = project_line.strip().split("\t")
        date = datetime.strptime(parts[1], "%d/%m/%Y").date()
        project = Project(parts[0], date, parts[2], float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()


def display_complete_project(projects):
    """Display complete projects"""
    print("Complete Projects: ")
    for project in projects:
        if project.completion_percentage == COMPLETE_PROJECT_PERCENTAGE:
            print(project)


def display_incomplete_project(projects):
    """Display incomplete projects"""
    print("Incomplete Projects: ")
    for project in projects:
        if project.completion_percentage != COMPLETE_PROJECT_PERCENTAGE:
            print(project)


def save_file(file_name_to_save, projects):
    """Save projects to text file"""
    out_file = open(file_name_to_save, 'w')
    for each_project in projects:
        information = f"{each_project.project}\t{each_project.start_date}\t{each_project.cost_estimate}\t" \
                      f"{each_project.priority}\t{each_project.completion_percentage}"
        print(information, file=out_file)
    out_file.close()


main()
