class Employee:
    def __init__(self, name, employee_id, salary):
        self.name, self.employee_id, self.salary = name, employee_id, salary

    def display_details(self):
        print(f"Employee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary:{self.salary}")

employee1 = Employee("sami", "E001", 50000)
employee2 = Employee("Jane", "E002", 60000)

employee1.display_details()
print()
employee2.display_details()