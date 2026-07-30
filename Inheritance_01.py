class Employee:
    company = "Infosys"

class Programmer(Employee):
    company = "Microsoft"

a = Employee()
b = Programmer()
b.programmer()
#print(a.company, b.company)