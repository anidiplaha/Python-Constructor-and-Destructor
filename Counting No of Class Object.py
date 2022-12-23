class Employee:
       count = 0
       def __init__(self):
             Employee.count = Employee.count + 1
employee_1 = Employee()
employee_2 = Employee()
employee_3 = Employee()
employee_4 = Employee()
employee_5 = Employee()
employee_6 = Employee()
employee_7 = Employee()
employee_8 = Employee()
print("The Total number of Employees:", Employee.count) 
