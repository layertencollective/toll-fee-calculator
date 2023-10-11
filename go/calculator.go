package main

import (
	"time"
)

// Calculate the total toll fee for one day given a vehicle and the timestamps
// of all the passages during that day.
func getTollFee(vehicle Vehicle, dates ...time.Time) int {
	intervalStart := dates[0]
	totalFee := 0

	for _, date := range dates {
		m := date.Sub(intervalStart) / (1_000_000_000 * 60)
		nextFee := tollFeePassage(date, vehicle)
		tempFee := tollFeePassage(intervalStart, vehicle)

		if m <= 60 {
			if totalFee > 0 {
				totalFee -= tempFee
			}
			if nextFee >= tempFee {
				tempFee = nextFee
			}
			totalFee += tempFee
		} else {
			totalFee += nextFee
		}
	}

	if totalFee > 60 {
		totalFee = 60
	}

	return totalFee
}

func isTollFreeVehicle(vehicle Vehicle) bool {
	vehicleType := vehicle.GetType()

	return vehicleType == "Motorbike" ||
		vehicleType == "Tractor" ||
		vehicleType == "Emergency" ||
		vehicleType == "Diplomat" ||
		vehicleType == "Foreign" ||
		vehicleType == "Military"
}

func tollFeePassage(date time.Time, vehicle Vehicle) int {
	if isTollFreeDate(date) || isTollFreeVehicle(vehicle) {
		return 0
	}

	h := date.Hour()
	m := date.Minute()

	if h == 6 && m >= 0 && m <= 29 {
		return 9
	} else if h == 6 && m >= 30 && m <= 59 {
		return 16
	} else if h == 7 && m >= 0 && m <= 59 {
		return 22
	} else if h == 8 && m >= 0 && m <= 29 {
		return 16
	} else if h >= 8 && h <= 14 && m >= 30 && m <= 59 {
		return 9
	} else if h == 15 && m >= 0 && m <= 29 {
		return 16
	} else if h == 15 && m >= 0 || h == 16 && m <= 59 {
		return 22
	} else if h == 17 && m >= 0 && m <= 59 {
		return 16
	} else if h == 18 && m >= 0 && m <= 29 {
		return 9
	} else {
		return 0
	}
}

func isTollFreeDate(date time.Time) bool {
	year := date.Year()
	month := date.Month()
	day := date.Day()

	dayOfWeek := date.Weekday()
	if dayOfWeek == 6 || dayOfWeek == 7 {
		return true
	}

	if year == 2018 {
		if month == 1 && (day == 1 || day == 5 || day == 6) ||
			month == 3 && (day == 29 || day == 30) ||
			month == 4 && (day == 2 || day == 30) ||
			month == 5 && (day == 1 || day == 9 || day == 10) ||
			month == 6 && (day == 5 || day == 6 || day == 22) ||
			month == 7 ||
			month == 11 && day == 2 ||
			month == 12 && (day == 24 || day == 25 || day == 26 || day == 31) {
			return true
		}
	}

	return false
}
