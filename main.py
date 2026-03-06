def add(a,b):
    a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b==0:
         return a/b
    return a/b

def power(a,b):
    return a ** b

a = float(input("Enter your first number:"))
b = float(input("Enter your second number:"))
operation = input("Enter operation (+ , - , * , / , **):")

def calculate():
    a = float(input("Enter your first number:"))
    b = float(input("Enter your second number:"))
    operation = input("Enter operation (+ , - , * , / , **):")

    if operation == "+":
        print(add(a,b))
    elif operation == "-":
        print(subtract(a,b))
    elif operation == "*":
        print(multiply(a,b))
    elif operation == "/":
        print(divide(a,b))
    elif operation == "**":
        print(power(a,b))
    else :
        print("Invaild operation")
