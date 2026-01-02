from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"

# Initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT,
                  status TEXT NOT NULL DEFAULT 'Pending')''')
    conn.commit()
    conn.close()

init_db()

# Home page: list tasks
@app.route("/")
def index():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

# Add new task
@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("add_task.html")

# Edit task
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        status = request.form["status"]
        c.execute("UPDATE tasks SET title=?, description=?, status=? WHERE id=?", (title, description, status, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = c.fetchone()
    conn.close()
    return render_template("edit_task.html", task=task)

# Delete task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
