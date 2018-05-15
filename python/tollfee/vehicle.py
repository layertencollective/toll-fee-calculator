"""
Vehicle classes for the toll fee calculator.
"""
import abc


class Vehicle(abc.ABC):
    """This class is used to describe the class Vehicle

    Abstract base class for the class Vehicle. This class is used for
    other classes to inherit from.

    Attributes:
        None
    """

    @abc.abstractmethod
    def get_type(self):
        """
        Returns:
            The type of vehicle
        """
        pass

    @abc.abstractmethod
    def fee_free_passage(self):
        """
        Returns:
             True if the vehicle is eligible for a fee free ride, False if not eligible for a free ride.
        """
        pass


class Car(Vehicle):
    """This class is used to describe the class Car

    The class car is a child class of Vehicle. The car class is used to describe to class Car.

    Attributes:
        free_passage: A boolean indicating if the car is eligible for a fee free passage,
        True if eligible, false if not.
    """

    def __init__(self):
        self.free_passage = False

    @staticmethod
    def get_type() -> str:
        """
        Returns:
            The type of vehicle
        """
        return 'Car'

    @staticmethod
    def fee_free_passage() -> bool:
        """
        Returns:
             True if the vehicle is eligible for a fee free ride, False if not eligible for a free ride.
        """
        return False


class TollFreeVehicles(Vehicle):
    """This class is used to describe the class TollFreeVehicles

    The class TollFreeVehicles is a child class of Vehicle. The TollFreeVehicles
    class is used to describe to class TollFreeVehicles.

    Attributes:
        free_passage: A boolean indicating if the car is eligible for a fee free passage,
        True if eligible, false if not.

        vehicle_type: Describes the name of the vehicle type
    """

    def __init__(self, vehicle_type):
        allowed_vehicles = ['motorbike', 'tractor', 'emergency', 'diplomat', 'foreign', 'military']
        if vehicle_type.lower() in allowed_vehicles:
            self.vehicle_type = vehicle_type
        else:
            raise Exception('This vehicle is not eligible for free ride!')
        self.free_passage = True

    def get_type(self) -> str:
        """
        Returns:
            The type of vehicle
        """
        return self.vehicle_type

    def fee_free_passage(self) -> bool:
        """
        Returns:
             True if the vehicle is eligible for a fee free ride, False if not eligible for a free ride.
        """
        return self.free_passage
