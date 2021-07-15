on = True

def add():
    a = float(input('Enter a number. '))
    b = float(input('Enter a number. '))
    print(a + b)


def substract():
    a = float(input('Enter a number. '))
    b = float(input('Enter a number. '))
    print(a - b)

def multiply():
    a = float(input('Enter a number. '))
    b = float(input('Enter a number. '))
    print(a * b)


def divide():
    a = float(input('Enter a number. '))
    b = float(input('Enter a number. '))
    print(a / b)


while on:
    operation = input('Please type +, -, *, / or q to quit ')
    if operation == '+':
        add()
    elif operation == '-':
        substract()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else:
        print("you did not select a valid operation")

