class mobile:

    Name:str

    storage:str

    price:int

    brand:str

    def __init__(self,name,storage,price,brand):

        self.Name=name

        self.storage=storage

        self.price=price

        self.brand=brand

    def display_mobile(self):
        print(self.Name,self.storage,self.price,self.brand)

    def __str__(self):
        return self.Name

# creating object  

mobile_instance=mobile("iphone 16 ","0128",50000,"apple")

print(mobile_instance)