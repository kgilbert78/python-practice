class Car { // class Car():
    constructor(name, year) { // def __init__(self, name, year)
        this.name = name; // self.name = name
        this.year = year; // self.year - year
    };

    age() { // def age(self):
        let date = new Date(); // today = date.today()
        return date.getFullYear() - this.year; // return (today.year - self.year)
    }
};

let myCar1 = new Car("Ford", 2014); // myCar1 = Car("Ford", 2014)
let myCar2 = new Car("Audi", 2019);

console.log(myCar1.age()) // print(myCar1.age())

class Truck { // class Truck():
    constructor(name, year) { // def __init__(self, name, year)
        this.name = name; // self.name = name
        this.year = year; // self.year - year
    };

    age(paramYear) { // def age(self, param_year):
        return paramYear - this.year; // return param_year - self.year
    }
}

let date = new Date(); // today = date.today()
let currentYear = date.getFullYear(); // current_year = today.year

let myTruck1 = new Truck("Chevy", 2016); // myTruck1 = Truck("Chevy", 2016)
console.log(myTruck1.age(currentYear)) // print(myTruck1.age(current_year))


// from https://www.w3schools.com/js/js_class_intro.asp