class Vehicle():
    def __init__(self, brand):
        self.brand = brand
        
    def show_brand(self):
        print(f"brand:{self.brand}")
    
class Car(Vehicle):
    """
    A class representing a car, which is a specialized type of Vehicle.
    This class extends the Vehicle class to include model-specific information.
    It also overrides the show_brand method to include model and speed details.
    Attributes:
        brand (str): The brand of the car, inherited from Vehicle.
        model (str): The model of the car.
    Methods:
        __init__(brand, model): Initializes a new Car instance.
        show_brand(speed=0): Displays the car's brand, model, and speed.
    """
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
