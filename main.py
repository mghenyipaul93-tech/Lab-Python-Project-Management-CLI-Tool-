
import argparse
from models import User, Project, Task
from file_io import save_data, load_data
from tabulate import tabulate

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

users = load_data(USERS_FILE)
projects = load_data(PROJECTS_FILE)
tasks = load_data(TASKS_FILE)

parser = argparse.ArgumentParser(description="Simple Project Management CLI")
subparsers = parser.add_subparsers(dest="command")

# add user
add_user = subparsers.add_parser("add-user")
add_user.add_argument("--name", required=True)
add_user.add_argument("--email", required=True)

# list projects
list_projects = subparsers.add_parser("list-projects")
list_projects.add_argument("--user_id", type=int, required=True)

# add project
add_project = subparsers.add_parser("add-project")
add_project.add_argument("--title", required=True)
add_project.add_argument("--description", default="")
add_project.add_argument("--due_date", default="")
add_project.add_argument("--user_id", type=int, required=True)

# add task
add_task = subparsers.add_parser("add-task")
add_task.add_argument("--title", required=True)
add_task.add_argument("--project_id", type=int, required=True)

# complete task
complete_task = subparsers.add_parser("complete-task")
complete_task.add_argument("--task_id", type=int, required=True)


args = parser.parse_args()

if args.command == "add-user":
    user = User(args.name, args.email)
    users.append(user.to_dict())
    save_data(users, USERS_FILE)
    print("User added successfully.")

elif args.command == "list-projects":
    user_projects = [p for p in projects if p["user_id"] == args.user_id]
    if not user_projects:
        print("No projects found.")
    else:
        print(tabulate(user_projects, headers="keys"))

elif args.command == "add-project":
    project = Project(args.title, args.description, args.due_date, args.user_id)
    projects.append(project.to_dict())
    save_data(projects, PROJECTS_FILE)
    print("Project added successfully.")

elif args.command == "add-task":
    task = Task(args.title)
    tasks.append(task.to_dict())
    save_data(tasks, TASKS_FILE)
    print("Task added successfully.")

elif args.command == "complete-task":
    for task in tasks:
        if task["id"] == args.task_id:
            task["status"] = "Completed"
    save_data(tasks, TASKS_FILE)
    print("Task marked as completed.")

else:
    parser.print_help()