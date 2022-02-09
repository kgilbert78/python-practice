class Car():
    def __init__(self, brand):
        self.carname = brand
    
    def present(self):
        return "I have a " + self.carname

class Model(Car):
    def __init__(self, brand, mod):
        super().__init__(brand) # initialize parent class (Car) with super to make the child class inherit all the methods and properties from its parent
        self.model = mod
        

    def show(self):
        return self.present() + ', it is a ' + self.model

myCar = Model("Ford", "Mustang")

print(myCar.show())

#  getters and setters (In Python you do this manually)
class Truck():
    def __init__(self, brand):
        self._truckname = brand
    
    def get_name(self):
        return self._truckname
    
    def set_name(self, user_input):
        self._truckname = user_input

myTruck = Truck("GMC")
print(myTruck.get_name())

myTruck.set_name("Toyota") # reset name with setter function
print(myTruck.get_name())