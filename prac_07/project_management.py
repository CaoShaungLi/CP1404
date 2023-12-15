"""
Project Management - client program
Estimated time: 4 hours
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


def main():
    print(MENU)
    projects = []
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file_name_to_load = "projects.txt"
            # file_name_to_load = input("Enter file name to load project: ")
            in_file = open(file_name_to_load, 'r')
            in_file.readline()
            for line in in_file:
                parts = line.strip().split("\t")
                # print(parts)
                date = datetime.strptime(parts[1], "%d/%m/%Y").date()
                project = Project(parts[0], date, parts[2], float(parts[3]), int(parts[4]))
                projects.append(project)
            in_file.close()
            for project in projects:
                print(project)

        elif choice == "S":
            if not projects:
                print("No file to save.")
            else:
                file_name_to_save = input("Enter file name to save project: ")
                out_file = open(file_name_to_save, 'w')
                for each_project in projects:
                    information = f"{each_project.project}\t{each_project.start_date}\t{each_project.cost_estimate}\t" \
                                  f"{each_project.priority}\t{each_project.completion_percentage}"
                    print(information, file=out_file)
                out_file.close()

        elif choice == "D":
            projects.sort()
            if not projects:
                print("No project yet.")
            else:
                for project in projects:
                    print(project.completion_percentage)
                print("Incomplete Projects: ")
                for project in projects:
                    if project.completion_percentage != 100:
                        print(project)
                print("Complete Projects: ")
                for project in projects:
                    if project.completion_percentage == 100:
                        print(project)
        elif choice == "F":
            input_date_string = input("Show projects that start after date (dd/mm/yy): ")
            input_date = datetime.strptime(input_date_string, "%d/%m/%Y").date()
            for project in projects:
                if project.start_date > input_date:
                    print(project)

        elif choice == "A":
            print("Let's add new project")
            project_name = input("Name: ")
            date_string = input("Date (d/m/yyyy): ")
            date = datetime.strptime(date_string, "%d/%m/%Y").date()
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            percent_complete = int(input("Percent complete: "))
            project = Project(project_name, date, priority, cost_estimate, percent_complete)
            projects.append(project)
            for project in projects:
                print(project)
        elif choice == "U":
            for number, project in enumerate(projects):
                print(number, project)
            project_choice = int(input("Project choice: "))
            for number, project in enumerate(projects):
                if project_choice == number:
                    # print(project)
                    new_percentage = int(input("New Percentage: "))
                    new_priority = int(input("New Priority: "))
                    project.completion_percentage = new_percentage
                    project.priority = new_priority
                    print(project)

        # else:
        #     pass
        print(MENU)
        choice = input(">>> ").upper()


print("Thank you for using custom-built project management software.")

main()
