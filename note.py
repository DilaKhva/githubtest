notes = []

while True:
    print("\n1. Add note\n2. View notes\n3. Delete note\n4. Exit")
    c = input("Choose: ")

    if c == "1":
        note = input("Note: ")
        notes.append(note)
        print("Saved!")

    elif c == "2":
        if not notes:
            print("No notes yet.")
        else:
            for i, n in enumerate(notes, 1):
                print(f"{i}. {n}")

    elif c == "3":
        num = int(input("Number to delete: "))
        if 1 <= num <= len(notes):
            notes.pop(num - 1)
            print("Deleted!")
        else:
            print("Invalid.")

    elif c == "4":
        break
