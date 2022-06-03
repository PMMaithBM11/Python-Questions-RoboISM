
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
while True:
    op = input("Enter operator: ")
    if op in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == '+':
            print(add(num1, num2))
            break

        elif op == '-':
            print(subtract(num1, num2))
            break

        elif op == '*':
            print(multiply(num1, num2))
            break

        elif op == '/':
            print(divide(num1, num2))
            break
    else:
        print("Invalid Input")
