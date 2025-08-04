# Simple To-Do List Application
class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "✔" if task["completed"] else "✘"
                print(f"{idx}. [{status}] {task['task']}")

    def mark_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as complete!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number!")

# Main Program
if __name__ == "__main__":
    todo = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark as complete: "))
                todo.mark_complete(task_number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            try:
                task_number = int(input("Enter task number to delete: "))
                todo.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "5":
            print("Exiting To-Do List. Have a productive day!")
            break
        else:
            print("Invalid choice! Please try again.")