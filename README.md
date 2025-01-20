# Task Tracker App

This project is a simple task tracker app built using Python's Tkinter library. The application allows users to add, delete, save, and load tasks with different statuses (Not Done, In-Progress, Done). It also includes functionality to save tasks in a text file and load them later.

## Features

- Add new tasks
- Change task status (Not Done, In-Progress, Done)
- Delete individual tasks or all tasks at once
- Save tasks to a file and load tasks from a file
- Simple, user-friendly interface

## Skills Utilized

### 1. **Tkinter**  
The app uses Tkinter to create a graphical user interface (GUI). Key elements utilized include:
- **Widgets**: Entry, Button, Listbox, Label, Radiobutton, Frame
- **Window management**: Creating new windows with `Toplevel`, handling window events, resizing, and adding icons
- **Layout management**: Using `.grid()` for arranging widgets in a structured manner
- **Messageboxes**: Displaying error messages and confirmation prompts using `messagebox`

### 2. **File Handling**  
Implemented the functionality to save and load tasks from text files:
- Used `filedialog` for browsing and selecting files to save and load
- Reading from and writing to text files with proper error handling

### 3. **Conditional Logic**  
- **Task Validation**: Ensured that a task is entered before adding it by checking if the input is empty
- **Status Handling**: Used radiobuttons to select task status and displayed the status accordingly
- **File Handling Errors**: Managed exceptions when saving or loading files to ensure the app remains functional even in case of errors

### 4. **Error Handling**  
Handled common issues such as empty input fields and file errors with proper error messages using `messagebox`.

### 5. **Modular Code Structure**  
- Broke down the code into smaller, reusable functions (`add()`, `delete()`, `save()`, etc.) for better organization and maintainability
- Used functions for specific tasks like creating a new window for adding a task and canceling the process

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## How to Run

1. Ensure Python is installed on your system.
2. Clone or download the repository.
3. Run the `task_tracker.py` file.

```bash
python task_tracker.py
