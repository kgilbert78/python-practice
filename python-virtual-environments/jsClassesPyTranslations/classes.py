from datetime import date

class Car():
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def age(self):
        today = date.today()
        return (today.year - self.year)


myCar1 = Car("Ford", 2014)
myCar2 = Car("Audi", 2019)

print(myCar1.age())

class Truck():
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def age(self, param_year):
        return param_year - self.year

today = date.today()
current_year = today.year

myTruck1 = Truck("Chevy", 2016)

print(myTruck1.age(current_year))