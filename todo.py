# todo.py - Simple CLI To-Do App

tasks = []

def show_menu():
    print("\n==== To-Do CLI App ====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task name: ")
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added!")

def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"Task '{tasks[num - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
