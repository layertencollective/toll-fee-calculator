
export class Vehicle {
}

class Car extends Vehicle {
    getType(): unknown {
        return 'Car';
    }
}

class Motorbike extends Vehicle {
    getType(): unknown {
        return 'Motorbike';
    }
}

export { Car, Motorbike };