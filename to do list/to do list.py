class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the list.')
        else:
            print(f'Task "{task}" not found in the list.')

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')
        else:
            print("Your To-Do List is empty.")

# Main function to run the To-Do List application
def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions: add, remove, display, exit")
        choice = input("What would you like to do? ").strip().lower()

        if choice == "add":
            task = input("Enter the task you want to add: ").strip()
            todo_list.add_task(task)
        elif choice == "remove":
            task = input("Enter the task you want to remove: ").strip()
            todo_list.remove_task