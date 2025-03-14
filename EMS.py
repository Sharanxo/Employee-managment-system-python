import mysql.connector

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="emp"
)

cursor = con.cursor()


# Function to check if an employee exists
def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'
    cursor.execute(sql, (employee_id,))
    return cursor.fetchone() is not None  # Fetch one record instead of using rowcount


# Function to add an employee
def add_employee():
    try:
        Id = int(input("Enter Employee Id: "))  # Convert to int
        if check_employee(Id):
            print("Employee already exists. Please try again.")
            return

        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = float(input("Enter Employee Salary: "))  # Convert to float

        sql = 'INSERT INTO employees (id, name, post, salary) VALUES (%s, %s, %s, %s)'
        data = (Id, Name, Post, Salary)

        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")

    except ValueError:
        print("Invalid input! Please enter correct data types.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()


# Function to remove an employee
def remove_employee():
    try:
        Id = int(input("Enter Employee Id: "))  # Convert to int
        if not check_employee(Id):
            print("Employee does not exist. Please try again.")
            return

        sql = 'DELETE FROM employees WHERE id=%s'
        cursor.execute(sql, (Id,))
        con.commit()
        print("Employee Removed Successfully")

    except ValueError:
        print("Invalid input! Please enter a valid Employee ID.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()


# Function to promote an employee
def promote_employee():
    try:
        Id = int(input("Enter Employee's Id: "))  # Convert to int
        if not check_employee(Id):
            print("Employee does not exist. Please try again.")
            return

        Amount = float(input("Enter increase in Salary: "))  # Convert to float

        sql_select = 'SELECT salary FROM employees WHERE id=%s'
        cursor.execute(sql_select, (Id,))
        current_salary = cursor.fetchone()[0]  # Get current salary
        new_salary = current_salary + Amount

        sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
        cursor.execute(sql_update, (new_salary, Id))
        con.commit()
        print("Employee Promoted Successfully")

    except ValueError:
        print("Invalid input! Salary must be a number.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()


# Function to display all employees
def display_employees():
    try:
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        if not employees:
            print("No employees found.")
            return
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Function to display the menu
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")

        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            cursor.close()
            con.close()
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    menu()
