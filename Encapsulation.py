#Wrapping data and functions into single unit.
#used in Data hiding
#(*) Public = Data csn be accessed inside and outside the class.
#(*) Protected = Data can be accessed inside and the class and sub-classes.
#(*) Private = Data can be accessed within the class.

class BankAccount:
    def __init__(self,name,balance):
        self.name = name #Puclic
        self.__balance = balance #Private

    def get_balance(self):#Getter
        return self.__balance

    def set_balance(self , newbalance): #Setter
        self.__balance = newbalance



acc1 = BankAccount("Ravi",100_000)
acc1.set_balance(200_000)
print(acc1.name,acc1.get_balance())
