/*
 * Toll fee calculator
 */

#include <time.h>
#include "tollcalculator.h"
#include "vehicle.h"

int is_toll_free_date(time_t time);

/*
 * Calculate the total toll fee for one day.
 * Args:
 *	- vehicle: The Vehicle
 *	- dates: Array of all passage times on one day
 *	- n: Number of passages in dates array
 */
int get_toll_fee(struct Vehicle vehicle, time_t *dates, int n)
{
	int total_fee = 0;
	time_t interval_start = dates[0];
	for (int i = 0; i < n; i++) {
		int next_fee = toll_fee_passage(dates[i], vehicle);
		int temp_fee = toll_fee_passage(interval_start, vehicle);
		int diff_minutes = (dates[i] - interval_start) / 60;
		if (diff_minutes <= 60) {
			if (total_fee)
				total_fee -= temp_fee;
			if (next_fee >= temp_fee)
				temp_fee = next_fee;
		}
		else
			total_fee += next_fee;
	}
	return (total_fee < 60) ? total_fee : 60;
}

/*
 * Return the fee for the passage at `time`.
 * Args:
 *  - time: The passage time
 *  - vehicle: The vehicle
 */
int toll_fee_passage(time_t time, struct Vehicle vehicle)
{
	if (is_toll_free_date(time) || is_toll_free_vehicle(vehicle))
		return 0;

	struct tm passage_time;
	localtime_r(&time, &passage_time);
	int hour = passage_time.tm_hour;
	int minute = passage_time.tm_min;
	if (hour == 6 && minute >= 0 && minute <= 29) return 9;
	else if (hour == 6 && minute >= 30 && minute <= 59) return 16;
	else if (hour == 7 && minute >= 0 && minute <= 59) return 22;
	else if (hour == 8 && minute >= 0 && minute <= 29) return 16;
	else if (hour >= 8 && hour <= 14 && minute >= 30 && minute <= 59) return 9;
	else if (hour == 15 && minute >= 0 && minute <= 29) return 16;
	else if (hour == 15 && minute >= 0 || hour == 16 && minute <= 59) return 22;
	else if (hour == 17 && minute >= 0 && minute <= 59) return 16;
	else if (hour == 18 && minute >= 0 && minute <= 29) return 9;
	else return 0;
}

int is_toll_free_date(time_t time)
{
	int month, day, day_of_week;
	struct tm date;
	localtime_r(&time, &date);
	month = date.tm_mon + 1;
	day = date.tm_mday;
	day_of_week = date.tm_wday;

	if (day_of_week >= 5)
		return 1;
	if (date.tm_year == 2018) {
		if (month == 1 && (day == 1 || day == 5 || day == 6) ||
				month == 3 && (day == 29 || day == 30) ||
				month == 4 && (day == 2 || day == 30) ||
				month == 5 && (day == 1 || day == 9 || day == 10) ||
				month == 6 && (day == 5 || day == 6 || day == 22) ||
				month == 7 ||
				month == 11 && day == 2 ||
				month == 12 && (day == 24 || day == 25 || day == 26 || day == 31)) {
			return 1;
		}
	}
	return 0;
}
