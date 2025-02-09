# Factorial using lambda (recursive)
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Menu driven program for employee dictionary
def insert_employee(emp_dict):
    emp_code = input("Enter employee code: ")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))
    expert_areas = input("Enter expert areas (comma separated): ").split(',')
    emp_dict[emp_code] = [name, age, salary, expert_areas]

def update_employee(emp_dict):
    emp_code = input("Enter employee code to update: ")
    if emp_code in emp_dict:
        name = input("Enter new employee name: ")
        age = int(input("Enter new employee age: "))
        salary = float(input("Enter new employee salary: "))
        expert_areas = input("Enter new expert areas (comma separated): ").split(',')
        emp_dict[emp_code] = [name, age, salary, expert_areas]
    else:
        print("Employee not found.")

def delete_employee(emp_dict):
    emp_code = input("Enter employee code to delete: ")
    if emp_code in emp_dict:
        del emp_dict[emp_code]
        print("Employee deleted.")
    else:
        print("Employee not found.")

def display_menu():
    print("1. Insert Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Exit")

def main():
    emp_dict = {}
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert_employee(emp_dict)
        elif choice == 2:
            update_employee(emp_dict)
        elif choice == 3:
            delete_employee(emp_dict)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
