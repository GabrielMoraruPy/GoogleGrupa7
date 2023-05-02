import tkinter as tk

# Define a function to add a task to the list
def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_entry.delete(0, tk.END)
    update_task_list()

# Define a function to update the task list display
def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

# Define a function to remove a task from the list
def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()

# Define a function to exit the program
def quit_program():
    root.destroy()

# Initialize the to-do list and create the main window
tasks = []
root = tk.Tk()
root.title("To-Do List")

# Create the user interface
task_entry = tk.Entry(root, width=30)
task_entry.pack(padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(padx=10, pady=5)

task_list = tk.Listbox(root, height=10)
task_list.pack(padx=10, pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_program)
quit_button.pack(padx=10, pady=10)

# Start the event loop
root.mainloop()
