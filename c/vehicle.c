#include <string.h>
#include "vehicle.h"

int is_toll_free_vehicle(struct Vehicle vehicle)
{
	return (strcmp(vehicle.type, "Motorbike") == 0 ||
			strcmp(vehicle.type, "Tractor") == 0 ||
			strcmp(vehicle.type, "Emergency") == 0 ||
			strcmp(vehicle.type, "Diplomat") == 0 ||
			strcmp(vehicle.type, "Foreign") == 0 ||
			strcmp(vehicle.type, "Military") == 0);
}
