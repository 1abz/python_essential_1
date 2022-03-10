
# Mathematical Operations

def subtract(x, y):
    return x - y


def add(x, y):
    return x + y


def multiply(x,y):
    return x * y


def division(x, y):
    return x / y


# if __name__ == '__main__':


first_number = int(input("Type First number: "))
second_number = int(input("Type Second Number "))

while True:
    operation = input('What operation you require, addition, subtraction, multiplication, division:  ' )
    operation = operation.lower()

    if operation in ('addition', 'subtraction', 'multiplication', 'division'):

        if operation == 'addition':
            print(add(first_number, second_number))

        elif operation == 'subtraction':
            print(subtract(first_number, second_number))

        elif operation == 'multiplication':
            print(multiply(first_number, second_number))

        elif operation == 'division':
            print(division(first_number, second_number))


        next_calc = input('Do you require another operation: yes/no  ')
        if next_calc == 'no':
            print('Thankyou!')
            break



