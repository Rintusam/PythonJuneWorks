class bike:
    name:str

    brand:str

    price:int

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

        self.bikes=[]

    def add_vehicle(self,bike):

        self.bikes.append(bike)
        
    def list_vehicles(self):

        for b in self.bikes:

            print(b)


hunter_instance=bike("hunter", "re",150000 )
activa_instance=bike("activa", "honda",50000 )
pulsar_instance=bike("pulsar", "bajaj",75000 )

showroom_instance=showroom("popular","kakkanad")
       
showroom_instance.add_vehicle(hunter_instance)
showroom_instance.add_vehicle(activa_instance)
showroom_instance.add_vehicle(pulsar_instance)

showroom_instance.list_vehicles()
    