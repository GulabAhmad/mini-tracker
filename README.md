# Mini Task Tracker 📋

A lightweight, menu-driven command-line task management application built in Python. Designed as part of the **PSEB AI Engineering Bootcamp (Week 1 Assignment)**, this application allows users to manage everyday tasks with instant JSON file persistence.

---

## 🎯 Project Goal

The primary goal of this project is to build an interactive, menu-driven CLI tool demonstrating core programming fundamentals:
- **Data structures**: Managing lists of dictionaries.
- **Control flow & functions**: Modular code architecture with clear separation of concerns.
- **File I/O & Serialization**: Reading from and writing to a persistent `tasks.json` file.
- **Defensive programming & Error handling**: Gracefully handling missing files, corrupted JSON data, blank input, and out-of-range selections.

---

## ✨ Key Features

- **➕ Add Task**: Add new tasks with automatic `Pending` status. Rejects empty/blank inputs.
- **📋 View Tasks**: View all existing tasks with 1-based numbering and clear `[Pending]` or `[Done]` tags.
- **✅ Mark Complete**: Mark a pending task as finished. Warns if the task is already completed.
- **🗑️ Delete Task**: Remove an unwanted task safely by its assigned number.
- **💾 Automatic Persistence**: Automatically loads tasks from `tasks.json` at startup, and writes updates after every change.
- **🛡️ Robust Error Handling**:
  - Handles `FileNotFoundError` on initial run without crashing.
  - Handles `json.JSONDecodeError` if storage file is empty or corrupted.
  - Validates user input for numeric task selections and boundary limits.

---

## 📂 Project Structure

```text
mini-tracker/
│
├── mini_task_tracker.py   # Main Python application
├── tasks.json             # Persistent task storage file
├── .gitignore             # Git ignore configuration
└── README.md              # Project documentation and guide
```

---

## 🚀 How to Run the Program

### Prerequisites
Make sure you have **Python 3.8+** installed. No external packages are required (uses standard library modules: `json`).

### 1. Clone the Repository
```bash
git clone https://github.com/GulabAhmad/mini-tracker.git
cd mini-tracker
```

### 2. Run the Application
Run the script using Python:

**On Windows:**
```bash
py mini_task_tracker.py
# or
python mini_task_tracker.py
```

**On macOS / Linux:**
```bash
python3 mini_task_tracker.py
```

---

## 🖥️ Demo & Usage Example

When launched, the program displays:

```text
Loaded 3 saved task(s) from tasks.json.

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 2

1. Complete Week 1 Python Fundamentals [Done]
2. Build Mini Task Tracker CLI [Done]
3. Prepare individual working demonstration [Pending]

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 1
Task title: Submit GitHub repository link
Task added.

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 3
Task number: 3
Task completed.

--- TASK TRACKER ---
1. Add  2. View  3. Complete  4. Delete  5. Exit
Choice: 5
Goodbye! Your tasks are saved in tasks.json.
```

---

## 📦 Data Schema

Tasks are stored in `tasks.json` in the following format:

```json
[
    {
        "title": "Complete Week 1 Python Fundamentals",
        "done": true
    },
    {
        "title": "Prepare individual working demonstration",
        "done": false
    }
]
```

---

## 👤 Author

- **Name:** Gulab Ahmad
- **Program:** PSEB AI Engineering Bootcamp
- **Assignment:** Week 1 - Mini Task Tracker
- **Repository:** [https://github.com/GulabAhmad/mini-tracker](https://github.com/GulabAhmad/mini-tracker)