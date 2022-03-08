
# Mathematical Operations

def subtract(x, y):
    return x - y


def add(x, y):
    return x + y


def multiply(x,y):
    return x * y


def division(x, y):
    return x / y


while True:
    print('Case sensitive')
    operation = input('What operation you require, addition, subtraction, multiplication, division:  ' )

    if operation in ('addition', 'subtraction', 'multiplication', 'division'):

        first_number = int(input("Type First number: "))
        second_number = int(input("Type Second Number "))

        if operation == 'addition':
            print(add(first_number, second_number))

        elif operation == 'subtraction':
            print(subtract(first_number, second_number))

        elif operation == 'multiplication':
            print(multiply(first_number, second_number))

        elif operation == 'division':
            print(add(first_number, second_number))



