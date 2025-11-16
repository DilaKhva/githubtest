tasks = []

while True:
    print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
        print("Added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == "3":
        num = int(input("Task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Removed!")
        else:
            print("Invalid number.")

    elif choice == "4":
        break
