print("Welcome to the Smart Calculator!")

while True:
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))

    # Display available operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get operation choice from user
    operation = input("Enter the operation symbol: ")

    # Get the second number from the user
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on user input
    if operation == "+":
        result = num1 + num2
        print("Result:", result)
    elif operation == "-":
        result = num1 - num2
        print("Result:", result)
    elif operation == "*":
        result = num1 * num2
        print("Result:", result)
    elif operation == "/":
        # Check if division by zero
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Cannot divide by zero!")
    else:
        # Handle invalid operation input
        print("Invalid operation symbol!")

    # Ask the user if they want to calculate again
    repeat = input("calculate again? (yes/no): ").lower()
    if repeat != "yes":
        print("Thanks for using the calculator.")
        break
