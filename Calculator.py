def calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Operations: +, -, *, /")

try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
    	result = num1 + num2
        print(result)
    elif operator == '-':
        result = num1 - num2
        print(result)
    elif operator == '*':
        result = num1 * num2
        print(result)
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
         print("Invalid operator. Please use +, -, *, or /.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
calculator()





