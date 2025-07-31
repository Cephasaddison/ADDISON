# Define variadic arithmetic functions
def add(*numbers):
    return sum(numbers)

def subtract(*numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(*numbers):
    if not numbers:
        return "No numbers to divide."
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero!"
        result /= num
    return result

# Main calculator function
def calculator():
    print("Welcome to the Variadic Calculator!")
    print("Choose an operation: add, subtract, multiply, divide")
    
    operation = input("Enter operation: ").strip().lower()
    number_input = input("Enter numbers separated by spaces: ").strip()
    
    try:
        numbers = [float(num) for num in number_input.split()]
    except ValueError:
        print("Invalid input: Please enter numbers only.")
        return

    # Dictionary to map operation names to functions
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    if operation in operations:
        result = operations[operation](*numbers)
        print("Result:", result)
    else:
        print("Invalid operation. Please choose from add, subtract, multiply, or divide.")

# Run the calculator
calculator()
