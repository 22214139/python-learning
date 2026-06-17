import math
history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: division by zero!"
    return a / b

def sqrt(a):
    if a < 0:
        return "error: negative number!"
    return math.sqrt(a)

def show_history():
    if len(history) == 0:
        print("empty")
        return
    for i, item in enumerate(history, 1):
        print(i, item)

while True:
    print("1: addition")
    print("2: subtraction")
    print("3: multiplication")
    print("4: division")
    print("5: square root")
    print("h: history")
    print("q: exit")
    choice = input("choice: ")
    if choice == "q":
        break
    elif choice == "h":
        show_history()
    elif choice == "1":
        a = float(input("first number: "))
        b = float(input("second number: "))
        result = add(a, b)
        history.append(str(a) + " + " + str(b) + " = " + str(result))
        print("result:", result)
    elif choice == "2":
        a = float(input("first number: "))
        b = float(input("second number: "))
        result = subtract(a, b)
        history.append(str(a) + " - " + str(b) + " = " + str(result))
        print("result:", result)
    elif choice == "3":
        a = float(input("first number: "))
        b = float(input("second number: "))
        result = multiply(a, b)
        history.append(str(a) + " * " + str(b) + " = " + str(result))
        print("result:", result)
    elif choice == "4":
        a = float(input("first number: "))
        b = float(input("second number: "))
        result = divide(a, b)
        history.append(str(a) + " / " + str(b) + " = " + str(result))
        print("result:", result)
    elif choice == "5":
        a = float(input("number: "))
        result = sqrt(a)
        history.append("sqrt(" + str(a) + ") = " + str(result))
        print("result:", result)
    else:
        print("invalid choice!")