def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    num1 = float(input("Enter the first number: "))
    while True:
        print("Available operation symbols: ")
        for symbol in operations:
            print(symbol, end=" ")
        print()

        should_continue = True
        while should_continue:
            operation_symbol = input("Select an operation symbol: ")
            if operation_symbol not in operations:
                print("Invalid operation symbol. Please try again.")
            else:
                num2 = float(input("Enter the second number: "))
                calculation_function = operations[operation_symbol]
                answer = calculation_function(num1, num2)
                print(f"{num1} {operation_symbol} {num2} = {answer}")

                choice = input("Do you want to continue with this result as the first number? (yes/no): ")
                if choice.lower() == 'yes':
                    num1 = answer
                elif choice.lower() == 'no':
                    should_continue = False
                else:
                    print("Invalid choice. Please try again.")

        new_calculation = input("Do you want to start a new calculation? (yes/no): ")
        if new_calculation.lower() == 'yes':
            calculator()
        elif new_calculation.lower() == 'no':
            break
        else:
            print("Invalid choice. Please try again.")

calculator()
