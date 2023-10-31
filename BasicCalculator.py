import math

def calculator(num1, num2, symbol):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    elif symbol == "/":
        return num1 / num2
    elif symbol == "^":
        return pow(num1, num2)

if __name__ == '__main__':
    print(f"Do you wish to use the calculator? (Y/N) ")
    for choice in range(1):
        if input() == 'Y':
            break
        else:
            quit()

    if ('Y'):
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        operation = input("Enter the operation: +, -, *, /, ^ ")
        if (operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "^"):
            print(f"{first_number} {operation} {second_number} = ", end="")
            print(calculator(first_number, second_number, operation)) 
        else:
            print("Not a valid operator")