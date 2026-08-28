class student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = student("Harry" , 9.6)
stu2 = student("Rohan" , 10.0)
stu3 = student("Ravi" , 8.5)

print(stu1.name ,"=", stu1.cgpa)
print(stu2.name , "=", stu2.cgpa)
print(stu3.name , "=", stu3.cgpa)

print(stu1.get_cgpa())

