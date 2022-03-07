amount_of_employees = int(input('How many employees does your business have: '))

for index in range(amount_of_employees) :
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

    age = int(input('What is the employees age: '))

    print(f"{first_name_str} {last_name_str} , {age}")
