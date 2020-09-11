'use strict';

const TollFreeVehicles = Object.freeze({
    'MOTORBIKE': 'Motorbike',
    'TRACTOR': 'Tractor',
    'EMERGENCY': 'Emergency',
    'DIPLOMAT': 'Diplomat',
    'FOREIGN': 'Foreign',
    'MILITARY': 'Military'
});

/**
 * Calculate the total toll fee for one day.
 * 
 * @param {Vehicle} vehicle The vehicle.
 * @param {...Date} dates Date and time of all passages on one day.
 * @return {number} The total toll fee for that day.
 */
function getTollFee(vehicle, ...dates) {
    let intervalStart = dates[0]
    let totalFee = 0;

    for (const date of dates) {
        let nextFee = tollFeePassage(date, vehicle);
        let tempFee = tollFeePassage(intervalStart, vehicle);

        let minutes = Math.floor((date - intervalStart) / (1000 * 60));

        if (minutes <= 60) {
            if (totalFee > 0) totalFee -= tempFee;
            if (nextFee >= tempFee) tempFee = nextFee;
            totalFee += tempFee;
        } else {
            totalFee += nextFee;
        }
    }

    if (totalFee > 60) totalFee = 60;
    return totalFee;
}

function isTollFreeVehicle(vehicle) {
    if (vehicle == null) return false;

    let vehicleType = vehicle.getType();
    return vehicleType === TollFreeVehicles.MOTORBIKE ||
           vehicleType === TollFreeVehicles.TRACTOR ||
           vehicleType === TollFreeVehicles.EMERGENCY ||
           vehicleType === TollFreeVehicles.DIPLOMAT ||
           vehicleType === TollFreeVehicles.FOREIGN ||
           vehicleType === TollFreeVehicles.MILITARY;
}

/**
 * Return the fee for the passage at `date`.
 * 
 * @param {Date} date The passage date.
 * @param {Vehicle} vehicle The vehicle.
 * @return {number} The toll fee for the passage.
 */
function tollFeePassage(date, vehicle) {
    if (isTollFreeDate(date) || isTollFreeVehicle(vehicle)) return 0;
    
    let hour = date.getHours();
    let minute = date.getMinutes();

    if (hour === 6 && minute >= 0 && minute <= 29) return 9;
    else if (hour === 6 && minute >= 30 && minute <= 59) return 16;
    else if (hour === 7 && minute >= 0 && minute <= 59) return 22;
    else if (hour === 8 && minute >= 0 && minute <= 29) return 16;
    else if (hour >= 8 && hour <= 14 && minute >= 30 && minute <= 59) return 9;
    else if (hour === 15 && minute >= 0 && minute <= 29) return 16;
    else if (hour === 15 && minute >= 0 || hour === 16 && minute <= 59) return 22;
    else if (hour === 17 && minute >= 0 && minute <= 59) return 16;
    else if (hour === 18 && minute >= 0 && minute <= 29) return 9;
    else return 0;
}

function isTollFreeDate(date) {
    let year = date.getYear();
    let month = date.getMonth();
    let day = date.getDate();

    let dayOfWeek = date.getDay();
    if (dayOfWeek === 5 || dayOfWeek === 6) return true;

    if (year === 2018) {
        if (month === 0 && (day === 1 || day === 5 || day === 6) ||
            month === 2 && (day === 29 || day === 30) ||
            month === 3 && (day === 2 || day === 30) ||
            month === 4 && (day === 1 || day === 9 || day === 10) ||
            month === 5 && (day === 5 || day === 6 || day === 22) ||
            month === 6 ||
            month === 10 && day === 2 ||
            month === 11 && (day === 24 || day === 25 || day === 26 || day === 31)) {
            return true;
        }
    }

    return false;
}

export {getTollFee};