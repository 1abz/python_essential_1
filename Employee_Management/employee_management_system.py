import functions
# Employee Management System

if __name__ == '__main__':

    print('"1" = Add an employee')
    print('"2" = Remove an employee')
    print('"3" = Get the total number of Employees')
    print('"4" = Get a list of the Employees')
    print('"5" = Update employee data')
    print('"6" = Retrieve the data of an employee (by ID)')
    print('"7" = Quit')



    while True:
        command = input('What operation you require, 1/2/3/4/5/6/7:  ')

        if command == "1":
            functions.add_employee()
            print(functions.employees)


        elif command == "2":
            functions.del_employee()
            print(functions.employees)


        elif command == "3":
            print('Total Number of employees in list')
            print(len(functions.employees))

        elif command == "4":
            print(functions.employees)

        elif command == "5":
            functions.del_employee()
            print(functions.employees)


        elif command == "6":
            functions.retrieve_data()


        elif command == "7":
            print('Thankyou for using the employee management system')
            break

        else:
            print("Incorrect command. Try again :)")
