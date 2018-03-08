#ifndef _TOLLCALC_H_
#define _TOLLCALC_H_

#include <time.h>
#include "vehicle.h"

int get_toll_fee(struct Vehicle, time_t *, int n);
int toll_fee_passage(time_t, struct Vehicle);

#endif
