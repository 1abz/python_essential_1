employees = []


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
        if 2 <= len(employee_fn.strip()):
            return employee_fn
        else:
            print('Enter minimum two characters')


def e_last_name():
    while True:
        employee_ln = input("Enter last name:  ")
        if 2 <= len(employee_ln.strip()):
            return employee_ln
        else:
            print('Enter minimum two characters')


def e_birth_year():
    while True:
        employee_by = (input("Enter birth year:  "))
        if employee_by.isdigit():
            return employee_by
        if 1900 <= int(employee_by) <= 2004:
            return employee_by
        else:
            print('Enter value between 1990 and 2004')


def e_birth_month():
    while True:
        employee_bm = (input("Enter birth month:  "))
        if employee_bm.isdigit():
            if 1 <= int(employee_bm) <= 12:
                return employee_bm
        else:
            print('Enter value between 1 and 12')


def e_birth_day():
    while True:
        employee_bd = int(input("Enter birth day:  "))
        if 1 <= employee_bd <= 31:
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
                "Employee ID": employeeid,
                "Employee First Name": employee_f_name,
                "Employee Last Name": employee_l_name,
                "Employee Birth Day": employ_day,
                "Employee Birth Month": employee_b_month,
                "Employee Birth Year": employee_b_year,
                "Employee Position": employee_pos,
                "Employee Grad": employee_g
    }

    while True:
        employees.append(employ)
        return employees


def del_employee():
    while True:
        del_employee_id = (input("Enter Employee ID: "))
        if del_employee_id.isdigit():
            for i_d in range(len(employees)):
                if employees[i_d]['Employee ID'] == del_employee_id:
                    del employees[i_d]
                    return employees
                else:
                    print("Employee ID doesnt exist")


def retrieve_data():
    while True:
        ret_employee_id = e_id()
        if ret_employee_id.isdigit():
            for rid in range(len(employees)):
                if employees[rid]['Employee ID'] == ret_employee_id:
                    print(employees[rid])
                    return
            else:
                print("insert valid id")


def update_employee():
    updated_employee_number = e_id()
    key = input('Enter key: ')
    new_value = input("Enter updated value: ")
    employees[updated_employee_number][key]=new_value

