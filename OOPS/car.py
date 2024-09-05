class car:

    name=str

    brand=str

    price=int

    def __init__(self,name,brand,price):

        self.name=name

        self.brand=brand

        self.price=price

    def __str__(self):
        return self.name
    

class showroom:

    def __init__(self,name,place):

        self.name=name

        self.place=place

        self.cars=[]
    
    def add_vehicles(self,car):
        
        self.cars.append(car)

    def list_vehicles(self):

        for c in self.cars:

            print (c)

innova_instance=car("innova","toyota",1500000)
fortuner_instance=car("fortuner","toyoya",4500000)
Xc90_instance=car("xc90","volvo",9000000)
evoke_instance=car("evoke","rangerover",7000000)

showroom_instance=showroom("aman toyoya","thrissur")

showroom_instance.add_vehicles(innova_instance)
showroom_instance.add_vehicles(fortuner_instance)
showroom_instance.add_vehicles(evoke_instance)
showroom_instance.add_vehicles(Xc90_instance)

showroom_instance.list_vehicles()

showroom_instance2=showroom(" toyoya","kakannad")

showroom_instance2.add_vehicles(innova_instance)
showroom_instance2.add_vehicles(fortuner_instance)

showroom_instance2.list_vehicles()