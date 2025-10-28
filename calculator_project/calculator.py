def calculator():
    print("=== Simple Calculator ===")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose operation: +, -, *, /")
        op = input("Enter operation: ")
        
        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero!")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()