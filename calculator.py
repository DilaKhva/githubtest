while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    c = input("Choose: ")

    if c == "5":
        break

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if c == "1":
        print(a + b)
    elif c == "2":
        print(a - b)
    elif c == "3":
        print(a * b)
    elif c == "4":
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print(a / b)