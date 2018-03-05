"""
Vehicle classes for the toll fee calculator.
"""

import abc


class Vehicle(abc.ABC):

    @abc.abstractmethod
    def get_type(self):
        pass


class Car(Vehicle):

    @staticmethod
    def get_type():
        return 'Car'


class Motorbike(Vehicle):

    @staticmethod
    def get_type():
        return 'Motorbike'
