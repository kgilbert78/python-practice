class Car { // class Car():
    constructor(brand) { // def __init__(self, brand):
        this.carname = brand; // self.carname = brand
    }
    present() { // def present(self):
        return 'I have a ' + this.carname; // return "I have a " + self.carname
    }
}

class Model extends Car { // class Model(Car):
    constructor(brand, mod) { // def __init__(self, brand, mod):
        super(brand); // super().__init__(brand)
        this.model = mod; // self.model = mod
    }
    show() { // def show(self):
        return this.present() + ', it is a ' + this.model; // return self.present() + ', it is a ' + self.model
    }
}

let myCar = new Model("Ford", "Mustang"); // myCar = Model("Ford", "Mustang")

console.log(myCar.show()) // print(myCar.show())

// getters and setters (In Python you do this manually)
class Truck {  // class Truck():
    constructor(brand) {  // def __init__(self, brand):
        this._truckname = brand; // self._truckname = brand
    }
    get truckname() { // def get_name(self):
        return this._truckname; // return self._truckname
    }
    set truckname(userInput) { // def set_name(self, user_input):
        this._truckname = userInput; // self._truckname = user_input
    }
}

let myTruck = new Truck("GMC"); // myTruck = Truck("GMC")
console.log(myTruck.truckname) // print(myTruck.get_name())

myTruck.truckname = "Toyota";
console.log(myTruck.truckname) // print(myTruck.get_name())


// NOTE:
// Unlike functions, and other JavaScript declarations, class declarations are not hoisted.
// That means that you must declare a class before you can use it.

// all from https://www.w3schools.com/js/js_class_inheritance.asp