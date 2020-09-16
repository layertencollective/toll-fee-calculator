
class Vehicle {
}

class Car extends Vehicle {
    getType() {
        return 'Car';
    }
}

class Motorbike extends Vehicle {
    getType() {
        return 'Motorbike';
    }
}

export { Car, Motorbike };