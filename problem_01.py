class Programmers:
    company = "Microsoft"
    def __init__(self , name , salary , pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmers("Monster" , 1000000 , 583120)
print(p.company ,p.name , p.salary ,p.pincode )
p = Programmers("Infinix" , 1000000 , 583120)
print(p.company ,p.name , p.salary ,p.pincode )
