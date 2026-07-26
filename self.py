class Employee():
    name = "Monster"
    salary="1000000"
    age ="20"

    def getInfo(self):#Here we must give self or anything as attribute or else it throws an error
        print(f"The name is {self.name} and his salary is {self.salary}")

a = Employee()
a.name = "Infinity"
a.getInfo() 
#If it give gives an error such as 0 positional argument but 1 was given then it is converted like this
#Employee.getInfo(a)