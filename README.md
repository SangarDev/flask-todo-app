# Flask To-Do App

Description:
A simple Python Flask web application for managing personal tasks. 
Users can add, edit, delete, and track the status of tasks (Pending/Completed). 

Features:
- Add new tasks with a title and optional description
- Edit existing tasks and update their status
- Delete tasks
- View all tasks in a clean, responsive interface

Tech Stack:
- Python 3.x
- Flask web framework
- SQLite database
- HTML/CSS for front-end templates

Installation & Setup:
1. Clone the repository:
   git clone  git remote add origin https://github.com/SangarDev/flask-todo-app.git
2. Navigate into the project folder:
   cd flask-todo-app
3. Create a virtual environment (optional but recommended):
   python -m venv venv
4. Activate the virtual environment:
   - Windows: venv\Scripts\Activate
   - Linux/Mac: source venv/bin/activate
5. Install dependencies:
   python -m pip install -r requirements.txt
6. Run the application:
   python app.py
7. Open your browser and go to:
   http://127.0.0.1:5000/

Usage:
- Use the "Add New Task" link to create tasks
- Edit or delete tasks using the respective buttons
- Track task status (Pending or Completed)

Notes:
- The SQLite database (database.db) will be created automatically when you first run the app.
- Do not include `database.db` in GitHub; it is included in `.gitignore`.

Author:
- Your Name

License:
- MIT License (if applicable)
