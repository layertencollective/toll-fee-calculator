
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
    var intervalStart = dates[0]
    var totalFee = 0;

    for (const date of dates) {
        var m = Math.floor((date - intervalStart) / (1000 * 60));
        var nextFee = tollFeePassage(date, vehicle);
        var tempFee = tollFeePassage(intervalStart, vehicle);

        if (m <= 60) {
            if (totalFee > 0) totalFee -= tempFee;
            if (nextFee >= tempFee) tempFee = nextFee;
            totalFee += tempFee;
        } else {
            totalFee += nextFee;
        }
    }

    if (totalFee > 60) totalFee = 60;
    return totalFee;

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
        var h;
        
        if (isTollFreeDate(date) || isTollFreeVehicle(vehicle)) return 0;

        h = date.getHours();
        m = date.getMinutes();
    
        if (h === 6 && m >= 0 && m <= 29) return 9;
        else if (h === 6 && m >= 30 && m <= 59) return 16;
        else if (h === 7 && m >= 0 && m <= 59) return 22;
        else if (h === 8 && m >= 0 && m <= 29) return 16;
        else if (h >= 8 && h <= 14 && m >= 30 && m <= 59) return 9;
        else if (h === 15 && m >= 0 && m <= 29) return 16;
        else if (h === 15 && m >= 0 || h === 16 && m <= 59) return 22;
        else if (h === 17 && m >= 0 && m <= 59) return 16;
        else if (h === 18 && m >= 0 && m <= 29) return 9;
        else return 0;
    }
    
    function isTollFreeDate(date) {
        let year = date.getYear();
        let month = date.getMonth();
        let day = date.getDate();
    
        let dayOfWeek = date.getDay();
        if (dayOfWeek === 5 || dayOfWeek === 6) return true;
    
        if (year === 2018) {
            if (month === 1 && (day === 1 || day === 5 || day === 6) ||
                month === 3 && (day === 29 || day === 30) ||
                month === 4 && (day === 2 || day === 30) ||
                month === 5 && (day === 1 || day === 9 || day === 10) ||
                month === 6 && (day === 5 || day === 6 || day === 22) ||
                month === 7 ||
                month === 11 && day === 2 ||
                month === 12 && (day === 24 || day === 25 || day === 26 || day === 31)) {
                return true;
            }
        }
    
        return false;
    }
}

export {getTollFee};