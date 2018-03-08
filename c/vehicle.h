#ifndef _VEHICLE_H_
#define _VEHICLE_H_

struct Vehicle {
	char *type;
	char *reg_plate;
};

int is_toll_free_vehicle(struct Vehicle);

#endif
