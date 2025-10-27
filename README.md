PROJECT URL: https://roadmap.sh/projects/task-tracker


<h1 align="center">🧭 Task Tracker CLI</h1>

<p align="center">
  <em>A simple, fast, and lightweight Command Line Interface (CLI) to track your daily tasks with ease.</em>  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/CLI-Task%20Manager-success?logo=terminal" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
</p>

---

## 📦 Features

✅ Add new tasks with description and status  
✅ Update existing task descriptions  
✅ Change the status of tasks (`todo`, `in-progress`, `done`)  
✅ Delete tasks by ID  
✅ View all tasks or filter by status  
✅ Persistent local storage in `task.json`

---

## ⚙️ Requirements

- 🐍 **Python 3.8+**
- No external dependencies — uses only Python’s standard library 💪

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-tracker-cli

# Run the Python file
python task_tracker.py
💡 The script automatically creates a task.json file if it doesn’t exist.

🧩 How to Use
When you run the program, you’ll see:

markdown
Copy code
_WELCOME_TO_YOUR_TASK_TRACKER_CLI_

1. Add task
2. Update task
3. Delete task
4. Update task status
5. Display all tasks
6. Display task by status
Follow the on-screen prompts according to your choice.

1️⃣ Add a New Task
java
Copy code
Enter short task description (max 30 words): Finish Python project
Enter your task status (todo, in-progress, done): todo
✅ Output:

arduino
Copy code
Task added successfully (ID: 123e4567-e89b-12d3-a456-426614174000)
2️⃣ Update Task Description
vbnet
Copy code
Enter the task id to be updated: 123e4567-e89b-12d3-a456-426614174000
Enter the new description: Finish Python project with README
✅ Output:

arduino
Copy code
Task updated successfully
3️⃣ Delete a Task
bash
Copy code
Enter the task id to be deleted: 123e4567-e89b-12d3-a456-426614174000
✅ Output:

arduino
Copy code
Task deleted successfully
4️⃣ Update Task Status
bash
Copy code
Enter the task id to be updated: 123e4567-e89b-12d3-a456-426614174000
Enter the new status(todo, in-progress, done): done
✅ Output:

arduino
Copy code
Task status updated successfully
5️⃣ Display All Tasks
json
Copy code
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "description": "Finish Python project with README",
  "status": "done",
  "CreatedAt": "2025-10-27 12:45:32",
  "UpdatedAt": "2025-10-27 13:10:45"
}
6️⃣ Display Tasks by Status
bash
Copy code
Enter task status you wish to print (todo, in-progress, done): todo
✅ Output:
Shows all tasks currently in the chosen status.

🧠 Data Storage
All tasks are saved in a file named task.json in the same directory as the script.

Example structure:

json
Copy code
[
  {
    "id": "d3f9b1b8-54d9-4dc7-b6ef-85d6c91c74df",
    "description": "Complete Python CLI app",
    "status": "in-progress",
    "CreatedAt": "2025-10-27 09:30:12",
    "UpdatedAt": "2025-10-27 09:45:00"
  }
]
🧾 Notes
Each task is assigned a unique UUID automatically.

You can manually open and edit task.json if needed.

Make sure to use valid statuses: todo, in-progress, or done.

💡 Future Improvements
✨ Add search functionality by keyword
⏰ Add due dates or priorities
📊 Allow exporting tasks to CSV
🌈 Add color-coded terminal output

👨‍💻 Author
Your Name
📧 nkuinmbeng@gmail.com
🐙 GitHub: zamiel01

<p align="center"> <sub>Built with ❤️ using Python.</sub> </p>