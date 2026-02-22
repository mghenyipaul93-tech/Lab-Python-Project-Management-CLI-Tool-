# Python Project Management CLI Tool

This is a simple command-line tool to manage users, projects, and tasks. 
You can add users, add projects to users, add tasks to projects, mark tasks complete, and list projects/tasks. 
Data is saved in JSON files.

## Prerequisites

- Python 3.10+  
- pip  
- Virtual environment (recommended)

## Setup

```bash
# Clone the repo
git clone <your-github-link>
cd project_cli

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add a user
python main.py add-user --name "Alex" --email "alex@email.com"

# Add a project for the user
python main.py add-project --title "CLI Tool" --description "Test project" --due_date "2026-03-01" --user_id 1

# Add a task to the project
python main.py add-task --title "Write code" --project_id 1

# Mark a task as complete
python main.py complete-task --task_id 1

# List projects for a user
python main.py list-projects --user_id 1

