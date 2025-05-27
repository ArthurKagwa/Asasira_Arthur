class Vehicle():
    def __init__(self, brand):
        self.brand = brand
        
    def show_brand(self):
        print(f"brand:{self.brand}")
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


       
    def show_brand(self,speed=0):
        print(f"brand:{self.brand} model:{self.model} speed:{speed}")
        
        
v1 = Vehicle("Toyota")
c1 = Car("Benz","G-wagon")

v1.show_brand()
c1.show_brand()
c1.show_brand(100)
