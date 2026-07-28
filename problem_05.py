from random import randint

class Train:
    def __init__(self , trainNo):
        self.trainNo = trainNo
        

    def book(self  , fro , to):
        print(f"Ticket is booked of Train No. {self.trainNo} from {fro} to {to}")

    def getstatus(self  , fro , to):
        print(f"Train ({self.trainNo}) is running from {fro} to {to}")
    
    def getfare(self , fro , to):
        print(f"Ticket fare in train No: {self.trainNo} from {fro} to {to} is {randint(200,5000)} ")


t = Train(22314)
t.getfare("a", "b")
