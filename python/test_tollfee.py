"""
Test if tollfee module is working as intended
"""

import pytest
import tollfee
import datetime
import holidays

# Generate different times and dates
fee_day = datetime.datetime(year=2018, month=5, day=14, hour=0, minute=0, second=0)
fee_free_day_sunday = datetime.datetime(year=2018, month=5, day=13, hour=0, minute=0, second=0)
fee_free_day_saturday = datetime.datetime(year=2018, month=5, day=12, hour=0, minute=0, second=0)
car = tollfee.Car()

# Generate vehicles that are not eligible to free passage
motorbike = tollfee.TollFreeVehicles('Motorbike')
tractor = tollfee.TollFreeVehicles('tractor')
emergency = tollfee.TollFreeVehicles('emergency')
diplomat = tollfee.TollFreeVehicles('Diplomat')
foreign = tollfee.TollFreeVehicles('foreign')
military = tollfee.TollFreeVehicles('military')


@pytest.mark.parametrize("vehicle, expected", [(car, False), (motorbike, True), (tractor, True),
                                               (emergency, True), (diplomat, True), (foreign, True), (military, True)])
def test_is_toll_free_vehicle(vehicle, expected):
    """Test if function for evaluating if vehicle can pass toll for free"""
    assert (expected == tollfee._is_toll_free_vehicle(vehicle)), (vehicle, 'is not eligible for free ride')


@pytest.mark.parametrize("date, vehicle, expected", [(fee_day + datetime.timedelta(hours=6, minutes=0), car, 9),
                                                     (fee_day + datetime.timedelta(hours=6, minutes=30), car, 16),
                                                     (fee_day + datetime.timedelta(hours=7, minutes=0), car, 22),
                                                     (fee_day + datetime.timedelta(hours=8, minutes=0), car, 16),
                                                     (fee_day + datetime.timedelta(hours=8, minutes=30), car, 9),
                                                     (fee_day + datetime.timedelta(hours=9, minutes=0), car, 9),
                                                     (fee_day + datetime.timedelta(hours=15, minutes=0), car, 16),
                                                     (fee_day + datetime.timedelta(hours=15, minutes=30), car, 22),
                                                     (fee_day + datetime.timedelta(hours=17, minutes=0), car, 16),
                                                     (fee_day + datetime.timedelta(hours=18, minutes=0), car, 9),
                                                     (fee_day + datetime.timedelta(hours=18, minutes=30), car, 0)])
def test_toll_fee_passage(date, vehicle, expected):
    """Test that toll_fee_passage returns the correct fee"""
    assert (expected == tollfee.toll_fee_passage(date, vehicle))


# Generate holiday dates to test the _is_toll_free_date function on
dates_data = []
for date, _ in sorted(holidays.SE(years=2018).items()):
    dates_data.append((date, True))

dates_data.append((datetime.datetime(year=2018, month=5, day=14), False))


@pytest.mark.parametrize("date, expected", dates_data)
def test_is_toll_free_date(date, expected):
    """Test if the _is_toll_free_data has all the holidays implemented correctly"""
    assert (expected == tollfee._is_toll_free_date(date)), (date, 'is missing from the calculator')


data_test_get_toll_fee = [(car, fee_day, True, False, False, 0, 3, 1, 0),
                          (car, fee_day, False, True, False, 0, 6, 6, 0),
                          (car, fee_day, False, True, False, 8, 10, 1, 16),
                          (car, fee_day + datetime.timedelta(minutes=30), False, True, False, 8, 10, 1, 9),
                          (car, fee_day, False, False, True, 0, 60, 10, 0),
                          (car, fee_day + datetime.timedelta(hours=10), False, False, True, 0, 2, 1, 9),
                          (car, fee_day + datetime.timedelta(hours=7), False, False, True, 59, 61, 1, 22),
                          (car, fee_free_day_sunday, False, True, False, 7, 18, 1, 0),
                          (car, fee_free_day_sunday, False, True, False, 7, 18, 1, 0),
                          (car, fee_free_day_saturday, False, True, False, 7, 18, 1, 0)]


@pytest.mark.parametrize("vehicle, start_time, days, hours, minutes, start, stop, step, expected",
                         data_test_get_toll_fee)
def test_get_toll_fee(vehicle, start_time, days, hours, minutes, start, stop, step, expected):
    """Test what toll fee we get with multiple passages"""
    dates = []
    for i in range(start, stop, step):
        if days:
            dates.append(start_time + datetime.timedelta(days=i))
        if hours:
            dates.append(start_time + datetime.timedelta(hours=i))
        if minutes:
            dates.append(start_time + datetime.timedelta(minutes=i))

    assert (expected == tollfee.get_toll_fee(vehicle, dates)), 'Fee other then expected!'
