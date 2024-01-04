from datetime import datetime

class Person:
    def __init__(self, name, dob, city, contact_no):
        self.name = name
        self.dob = dob
        self.city = city
        self.contact_no = contact_no

class Employee(Person):
    def __init__(self, name, dob, city, contact_no, emp_id, joining_date, salary, department, post):
        super().__init__(name, dob, city, contact_no)
        self.emp_id = emp_id
        self.joining_date = joining_date
        self.salary = salary
        self.department = department
        self.post = post

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [employee for employee in self.employees if employee.emp_id != emp_id]

    def get_all_employees(self):
        return self.employees

    def get_employee_by_name(self, name):
        return [employee for employee in self.employees if employee.name == name]

    def get_employees_by_department(self, department):
        return [employee for employee in self.employees if employee.department == department]

    def get_employees_by_salary_range(self, min_salary, max_salary):
        return [employee for employee in self.employees if min_salary <= employee.salary <= max_salary]

    def get_employees_joined_current_year(self):
        current_year = datetime.now().year
        return [employee for employee in self.employees if datetime.strptime(employee.joining_date, '%Y-%m-%d').year == current_year]

    def get_employees_from_city(self, city):
        return [employee for employee in self.employees if employee.city == city]

    def get_employees_birthday_current_month(self):
        current_month = datetime.now().month
        return [employee for employee in self.employees if datetime.strptime(employee.dob, '%Y-%m-%d').month == current_month]

    def get_employees_age_less_than(self, age):
        current_year = datetime.now().year
        return [employee for employee in self.employees if current_year - datetime.strptime(employee.dob, '%Y-%m-%d').year < age]

def input_employee_details():
    name = input("Enter name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    city = input("Enter city: ")
    contact_no = input("Enter contact number: ")
    emp_id = input("Enter employee ID: ")
    joining_date = input("Enter joining date (YYYY-MM-DD): ")
    salary = float(input("Enter salary: "))
    department = input("Enter department: ")
    post = input("Enter post: ")

    return Employee(name, dob, city, contact_no, emp_id, joining_date, salary, department, post)

manager = EmployeeManager()

while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Print All Employees")
    print("3. Find Employee by Name")
    print("4. Print Employees in Finance Department")
    print("5. Find Employees with Salary > 50000")
    print("6. Find Employees with Salary between 50000-100000")
    print("7. Find Employees Joined in the Current Year")
    print("8. Find Employees from Mirzapur")
    print("9. Find Employees with Birthday in the Current Month")
    print("10. Find Employees with Age < 30")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        employee = input_employee_details()
        manager.add_employee(employee)
        print("Employee added successfully!")

    elif choice == '2':
        print("\nAll Employees:")
        for employee in manager.get_all_employees():
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '3':
        search_name = input("Enter the name to search: ")
        found_employees = manager.get_employee_by_name(search_name)
        if found_employees:
            print("\nEmployee(s) found:")
            for employee in found_employees:
                print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")
        else:
            print(f"No employee found with the name '{search_name}'.")

    elif choice == '4':
        print("\nEmployees in Finance Department:")
        for employee in manager.get_employees_by_department("Finance"):
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '5':
        print("\nEmployees with Salary > 50000:")
        for employee in manager.get_employees_by_salary_range(50000, float('inf')):
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '6':
        print("\nEmployees with Salary between 50000-100000:")
        for employee in manager.get_employees_by_salary_range(50000, 100000):
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '7':
        print("\nEmployees Joined in the Current Year:")
        for employee in manager.get_employees_joined_current_year():
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '8':
        print("\nEmployees from Mirzapur:")
        for employee in manager.get_employees_from_city("Mirzapur"):
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '9':
        print("\nEmployees with Birthday in the Current Month:")
        for employee in manager.get_employees_birthday_current_month():
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '10':
        print("\nEmployees with Age < 30:")
        for employee in manager.get_employees_age_less_than(30):
            print(f"{employee.name} ({employee.emp_id}), Department: {employee.department}, Salary: {employee.salary}")

    elif choice == '0':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
