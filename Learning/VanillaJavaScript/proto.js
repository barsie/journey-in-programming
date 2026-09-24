const person = {
    alive: true
}

const musician = {
    plays: true
}

//  JS uses initially __proto__
// musician.__proto__ = person
// console.log(musician.alive)
// console.log(musician.plays)
// console.log(musician)

// JS now uses setter and getter method to get and set attributes of a prototype, instead of using __proto__
Object.setPrototypeOf(musician, person);
// console.log(Object.getPrototypeOf(musician))

//console.log(musician.__proto__) // direct setter using __proto__
// console.log(Object.getPrototypeOf(person))
// console.log(Object.getPrototypeOf(musician) === musician.__proto__)

// musician can access the property of plays from object 
// console.log(musician.plays)

// but it can access the property of 
// console.log(musician.alive)


// Extending the prototype

const guitaris = {
    style: "two fingers",
    __proto__: musician
}

// console.log(guitaris)
// console.log(guitaris.plays)
// console.log(guitaris.alive)


// No circular dependencies are allow on JS prototypes (person.__proto__ can't be guitarist)

// Object with a getter and a setter
const car = {
    doors: 2,
    seats: "vyneal",

    get seatMaterial(){
        return this.seats
    },

    set seatMaterial(material){
        return this.seats = material
    }
}

const luxuryCar = {}
Object.setPrototypeOf(luxuryCar, car);
luxuryCar.seatMaterial = "leather"
// console.log(luxuryCar)
// console.log(luxuryCar.doors)
// console.log(car)

// Walking up the chain - props and methods are not copied
console.log(luxuryCar.valueOf())

// Get a key of an object
console.log(Object.keys(luxuryCar)) // use the key property directly
Object.keys(luxuryCar).forEach(key => { //use a forEach loop
    console.log(key)
})

for(let key in luxuryCar){ // for..in loop include all inherited property from car
    console.log(key)
}

// Object Constructors
function Animal(species){
    this.species = species;
    this.eats = true;
}

Animal.prototype.walks = function (){
    return `A ${this.species} is walking`
}

const Bear = new Animal("bear");

console.log(Bear.species)
console.log(Bear.walks())
console.log(Bear.__proto__)
console.log(Bear)
console.log(Animal)

// ES6 Example of inheritance

class Vehicle{
    constructor(){
        this.wheels = 4,
        this.motorized = true
    }

    ready(){
        return "Ready to Go..."
    }
}

class Motorcycle extends Vehicle{
    constructor(){
        super();
        this.wheels = 2;
    }

    wheelie(){
        return "On the wheel now"
    }
}

const myBike = new Motorcycle();
console.log(myBike)
console.log(myBike.wheels)
console.log(myBike.wheelie())
console.log(myBike.ready())


const truck = new Vehicle()
console.log(truck)
console.log(truck.wheels)
console.log(truck.ready())