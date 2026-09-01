class Employee():
    start_time = "10Am"
    End_time = "5Pm"

class Adminstaff(Employee):
    def __init__(self,role):
        self.role = role
    
    
class Accountant(Adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary



acc1 = Accountant(  50_000 , "CA" )

print(acc1.role , acc1.salary , acc1.start_time , acc1.End_time  )