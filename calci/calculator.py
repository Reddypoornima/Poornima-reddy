def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Main function to run the calculator
def main():
    while True:
        try:
            # Prompt user to input two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Prompt user to choose an operation
        print("\nOperations: +, -, *, /")
        operation = input("Enter the operation you want to perform: ").strip()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please choose a valid operation.")
            continue

        print(f"The result is: {result}\n")

        # Check if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != "yes":
            break

if __name__ == "__main__":
    main()