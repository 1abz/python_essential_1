# Employee Management System

#Employee ID function

def e_id():
    while True:
        employee_id = (input("Enter Employee ID:  "))
        if employee_id.isdigit():
            return employee_id
        else:
            print('Enter integer')


def e_first_name():
    while True:
        employee_fn = input("Enter first name:  ")
        if 2 <= len(employee_fn):
            return employee_fn
        else:
            print('Enter minimum two characters')


def e_last_name():
    while True:
        employee_ln = input("Enter last name:  ")
        if 2 <= len(employee_ln):
            return employee_ln
        else:
            print('Enter minimum two characters')


def e_birth_year():
    while True:
        employee_by = int(input("Enter birth year:  "))
        if 1900 <= (employee_by) <= 2004:
            return employee_by
        else:
            print('Enter value between 1990 and 2004')


def e_birth_month():
    while True:
        employee_bm = int(input("Enter birth month:  "))
        if 1 <= (employee_bm) <= 12:
            return employee_bm
        else:
            print('Enter value between 1 and 12')


def e_birth_day():
    while True:
        employee_bd = int(input("Enter birth day:  "))
        if 1 <= (employee_bd) <= 31:
            return employee_bd
        else:
            print('Enter value between 1 and 31')


def e_position():
    while True:
        employee_p = input("Enter position:  ")
        if len(employee_p.strip()) > 0:
            employee_position = str(employee_p)
            return employee_position
        else:
            print('Enter Position again')


def e_unigrad():
    values = ["Yes", "No"]
    while True:
        employee_ug = (input("University graduate? Enter Yes or No:"))
        if employee_ug in values:
            return employee_ug
        else:
            print('Please enter Yes or No')

def input_employee():
    employ = {
        "Employee ID": e_id(),
        "Employee First Name": e_first_name(),
        "Employee Last Name": e_last_name(),
        "Employee Birth Day": e_birth_day(),
        "Employee Birth Month": e_birth_month(),
        "Employee Birth Year": e_birth_year(),
        "Employee Position": e_position(),
        "Employee Grad": e_unigrad(),
    }
    return employ

def add_employee():
    employeeid = e_id()
    employee_f_name = e_first_name()
    employee_l_name = e_last_name()
    employ_day = e_birth_day()
    employee_b_month = e_birth_month()
    employee_b_year = e_birth_year()
    employee_pos = e_position()
    employee_g = e_unigrad()

    employ ={
                "Employee_ID": employeeid,
                "Employee_First Name": employee_f_name,
                "Employee_Last Name": employee_l_name,
                "Employee_Birth Day": employ_day,
                "Employee_Birth Month": employee_b_month,
                "Employee_Birth Year": employee_b_year,
                "Employee_Position": employee_pos,
                "Employee_Grad": employee_g
    }

    while True:
        employees.append(employ)
        return employee



if __name__ == '__main__':


    print('"1" = Add an employee')
    print('"2" = Remove an employee')
    print('"3" = Get the total number of Employees')
    print('"4" = Get a list of the Employees')
    print('"5" = Update employee data')
    print('"6" = Retrieve the data of an employee (by ID)')
    print('"7" = Update employees data')
    print('"8" = Exit')

    employees = []

    while True:
        command = input('What operation you require, 1/2/3/4/5/6/7:  ')

        if command == "1":
            add_employee()
            print(employees)

        elif command =




#add employee







