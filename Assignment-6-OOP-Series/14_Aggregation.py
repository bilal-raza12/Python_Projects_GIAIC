class Department:
    def __init__(self, employee):
        self.employees = employee

    def show_employee(self):
        print(f"Employee Name: {self.employees.name}")
    
class Employee:
    def __init__(self , name):
        self.name = name

emp = Employee("Bilal Raza")
dept = Department(emp)
print(dept.show_employee())


