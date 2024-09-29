from art import logo  # Importing a logo from the 'art' module (assumed to display the logo for the calculator app).


# Function to add two numbers
def add(n1, n2):
    return n1 + n2


# Function to subtract the second number from the first
def subtract(n1, n2):
    return n1 - n2


# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2


# Function to divide the first number by the second, includes a check for division by zero
def divide(n1, n2):
    if n2 == 0:
        return "invalid operation"  # Prevents division by zero
    return n1 / n2


# Dictionary that maps symbols to their corresponding operation functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print(logo)  # Displays the calculator logo


# Main calculator function
def calc_app(prev_result=None):
    """
    If prev_result is provided, it will be used as the first number,
    otherwise, the user will be prompted to input the first number.
    """

    # Prompt for the first number, unless continuing with a previous result
    if prev_result is None:
        num1 = float(input("What's the first number?: "))
    else:
        num1 = prev_result

    # Display available operation symbols
    for symbol in operations:
        print(symbol)

    # Ask the user to choose an operation from the available symbols
    operation_symbol = input("Pick an operation from the line above: ")

    # Retrieve the appropriate operation function from the dictionary
    operation = operations[operation_symbol]

    # Prompt for the second number
    num2 = float(input("What's the second number?: "))

    # Perform the calculation using the selected operation
    result = operation(num1, num2)

    # Display the result of the operation
    print(f"{num1} {operation_symbol} {num2} = {result}")

    # Ask the user whether to continue with the current result, start a new calculation, or exit
    choice = input(
        f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'out' to exit: ")

    # Recursive calls based on user's choice
    if choice == 'y':
        calc_app(prev_result=result)  # Continue with the current result
    elif choice == 'n':
        calc_app(prev_result=None)  # Start a new calculation
    elif choice == 'out':
        print("Thanks for using the app")  # Exit the application
    else:
        print("Invalid input")  # Handle invalid input


# Start the calculator app
calc_app()
