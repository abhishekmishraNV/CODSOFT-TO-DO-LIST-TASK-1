import tkinter as tk
from tkinter import ttk

class TodoListWidget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Colorful To-Do List")
        self.master.geometry("600x400")
        self.master.configure(bg="#FFFFFF")
        
        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=40, bg="#FFFFFF", fg="#000000")
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task, bg="#00CC00", fg="#FFFFFF")
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_table = ttk.Treeview(self.master, columns=("Task"), selectmode="browse", style="Custom.Treeview")
        self.task_table.heading("#0", text="ID")
        self.task_table.heading("#1", text="Task")
        self.task_table.tag_configure("oddrow", background="#E8E8E8")
        self.task_table.tag_configure("evenrow", background="#FFFFFF")
        self.task_table.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task, bg="#FF0000", fg="#FFFFFF")
        self.remove_button.grid(row=2, column=0, padx=5, pady=10)

        self.clear_button = tk.Button(self.master, text="Clear All", command=self.clear_tasks, bg="#FF0000", fg="#FFFFFF")
        self.clear_button.grid(row=2, column=1, padx=5, pady=10)

        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task, bg="#0000FF", fg="#FFFFFF")
        self.update_button.grid(row=3, column=0, padx=5, pady=10)

        self.edit_button = tk.Button(self.master, text="Edit Task", command=self.edit_task, bg="#0000FF", fg="#FFFFFF")
        self.edit_button.grid(row=3, column=1, padx=5, pady=10)

        self.populate_table()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            task_id = len(self.tasks) + 1
            self.tasks.append((task_id, task))
            self.task_table.insert("", "end", text=str(task_id), values=(task), tags=(f"{task_id % 2 == 0 and 'evenrow' or 'oddrow'}"))
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_items = self.task_table.selection()
        for item in selected_items:
            task_id = int(self.task_table.item(item, "text"))
            del self.tasks[task_id - 1]
            self.task_table.delete(item)
            self.populate_table()

    def edit_task(self):
        selected_items = self.task_table.selection()
        if selected_items:
            item = selected_items[0]
            task = self.task_table.item(item, "values")[0]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(0, task)

    def update_task(self):
        selected_items = self.task_table.selection()
        if selected_items:
            item = selected_items[0]
            task_id = int(self.task_table.item(item, "text"))
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[task_id - 1] = (task_id, updated_task)
                self.task_table.item(item, values=(updated_task))
                self.populate_table()

    def populate_table(self):
        for item in self.task_table.get_children():
            self.task_table.delete(item)
        for task_id, task in enumerate(self.tasks, start=1):
            self.task_table.insert("", "end", text=str(task_id), values=(task), tags=(f"{task_id % 2 == 0 and 'evenrow' or 'oddrow'}"))

    def clear_tasks(self):
        self.tasks = []
        self.populate_table()
        self.task_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TodoListWidget(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()