class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self , name , salary , language): # It is and dunder method where fuction get called automatically.It is also known as Paramaterized constructor.  
        self.language = language
        self.name = name
        self.salary = 1300000
        print("I am creating an object.")

a = Employee("Infinix" , 1300000 , "C++")
#a.name = "Monster"
print(a.name , a.language , a.salary)
print("Name:", a.name)