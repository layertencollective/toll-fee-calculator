"""
Toll fee calculator
"""

import enum

from .vehicle import Car, Motorbike


class TollFreeVehicles(enum.Enum):
    Motorbike = 1
    Tractor = 2
    Emergency = 3
    Diplomat = 4
    Foreign = 5
    Military = 6


def get_toll_fee(vehicle, dates):
    """
    Calculate the total toll fee for one day

    Args:
        vehicle (vehicle.Vehicle): The vehicle.
        dates (list): Date and time (:py:class:`datetime.datetime`)
            of all passes on one day.

    Returns:
        int: The total toll fee for that day.
    """
    interval_start = dates[0]
    total_fee = 0

    for i in range(len(dates)):
        next_fee = toll_fee_passage(dates[i], vehicle)
        temp_fee = toll_fee_passage(interval_start, vehicle)
        diff = dates[i] - interval_start
        minutes = diff.total_seconds() // 60

        if minutes <= 60:
            if total_fee:
                total_fee -= temp_fee
            if next_fee >= temp_fee:
                temp_fee = next_fee
            total_fee += temp_fee
        else:
            total_fee += next_fee

    return min(total_fee, 60)


def toll_fee_passage(date, vehicle):
    """
    Return the fee for the passage at `date`.

    Args:
        date (datetime.datetime): The passage date.
        vehicle (vehicle.Vehicle): The vehicle.

    Returns:
        int: The toll fee for the passage
    """
    if _is_toll_free_date(date) or _is_toll_free_vehicle(vehicle):
        return 0

    hour = date.hour
    minute = date.minute

    if hour == 6 and minute >= 0 and minute <= 29:
        return 9
    elif hour == 6 and minute >= 30 and minute <= 59:
        return 16
    elif hour == 7 and minute >= 0 and minute <= 59:
        return 22
    elif hour == 8 and minute >= 0 and minute <= 29:
        return 16
    elif hour >= 8 and hour <= 14 and minute <= 29:
        return 9
    elif hour == 15 and minute >= 0 and minute <= 29:
        return 16
    elif hour == 15 and minute >= 0 or hour == 16 and minute <= 59:
        return 22
    elif hour == 17 and minute >= 0 and minute <= 59:
        return 16
    elif hour == 18 and minute >= 0 and minute <= 29:
        return 9
    else:
        return 0


def _is_toll_free_date(date):
    if date.weekday() in (5, 6):
        return True

    elif date.year == 2018:
        if (date.month == 1 and (date.day == 1 or date.day == 5 or date.day == 6)
                or date.month == 3 and (date.day == 29 or date.day == 30)
                or date.month == 4 and (date.day == 2 or date.day == 30)
                or date.month == 5 and (date.day == 1 or date.day == 9 or date.day == 10)
                or date.month == 6 and (date.day == 5 or date.day == 6 or date.day == 22)
                or date.month == 7
                or date.month == 11 and date.day == 2
                or date.month == 12 and (date.day == 24 or date.day == 25 or date.day == 26 or date.day == 31)
            ):
            return True
        else:
            return False
    return False


def _is_toll_free_vehicle(vehicle):
    vehicle_type = vehicle.get_type()
    if vehicle == None:
        return False

    return (
        vehicle_type == TollFreeVehicles.Motorbike.name or
        vehicle_type == TollFreeVehicles.Tractor.name or
        vehicle_type == TollFreeVehicles.Emergency.name or
        vehicle_type == TollFreeVehicles.Diplomat.name or
        vehicle_type == TollFreeVehicles.Foreign.name or
        vehicle_type == TollFreeVehicles.Military.name)
