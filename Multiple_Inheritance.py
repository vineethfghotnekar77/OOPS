class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the company is {self.company}")

class Coder(Employee):
    language = "Python"
    def Languages(self):
        print(f"Main language is {self.language}")

class programmer(  Coder):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name is {self.company} and language is {self.language}")


a=Employee()
b=programmer()
c=Coder()
b.show()
b.Languages()
b.showLanguage()
