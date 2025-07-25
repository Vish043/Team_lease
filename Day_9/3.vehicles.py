class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    
    def show(self):
        print("Brand :",self.brand)
class Car(Vehicle):
    def show(self):
        print("This is a Car. Brand:", self.brand)

class Bike(Vehicle):
    def show(self):
        print("This is a Bike. Brand:", self.brand)

v1 = Car("Toyota")
v2 = Bike("Yamaha")
v1.show()
v2.show()
