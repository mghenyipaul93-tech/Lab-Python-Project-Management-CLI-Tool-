
class Person:
    
    def __init__(self, name):
        self.name = name


class User(Person):

    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name)
        self.id = User.id_counter
        User.id_counter += 1
        self.email = email
        self.projects = [] 

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": self.projects
        }

    def __str__(self):
        return f"User {self.id}: {self.name} ({self.email})"


class Project:

    id_counter = 1

    def __init__(self, title, description, due_date, user_id):
        self.id = Project.id_counter
        Project.id_counter += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_id = user_id
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_id": self.user_id,
            "tasks": self.tasks
        }

    def __str__(self):
        return f"Project {self.id}: {self.title}"


class Task:

    id_counter = 1

    def __init__(self, title, assigned_to=None):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    def __str__(self):
        return f"Task {self.id}: {self.title} ({self.status})"
