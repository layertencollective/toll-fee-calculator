package main

type Vehicle interface {
	GetType() string
}

type Car struct {
}

func (c Car) GetType() string {
	return "Car"
}

type Motorbike struct {
}

func (m Motorbike) GetType() string {
	return "Motorbike"
}
