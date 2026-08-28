class product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count+=1

    def get_info(self):#Instance Method
        print(f"Product Name: {self.name}, Price: {self.price}")

    @classmethod
    def get_count(cls):#Class Method
        print(f"Total Products: {cls.count}")

    @staticmethod
    def cal_discount(price,discount):
        final_price=price-(price*discount/100)
        print(f"Final Price after discount: {final_price}")

p1=product("Laptop", 15_000)
p2=product("Mobile", 10_000)
p3=product("Tablet", 20_000)
p1.get_info()
product.get_count()
p1.cal_discount(p1.price,15)