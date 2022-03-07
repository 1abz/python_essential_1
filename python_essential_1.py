amount_of_employees = int(input('How many employees does your business have: '))

for index in range(amount_of_employees):
    first_name_str = ""
    while first_name_str.strip() == "":
        first_name_str = input('What is the employees first name: ')
        if first_name_str.strip() == "":
            print('Invalid input. Please enter valid first name')

    last_name_str = ""
    while last_name_str.strip() == "":
        last_name_str = input('What is the employees last name: ')
        if last_name_str.strip() == "":
            print('Invalid input. Please enter valid last name:')

    x = None
    while x is None:
        age = (input('What is the employees age: '))
        if age.strip() != "":
            if int(age) < 18 or int(age) > 100:
                print('Enter age between 18 and 100')
            else:
                x = True
        else:
            print('Please enter an integer')

    print(f"{first_name_str} {last_name_str} , {age}")



