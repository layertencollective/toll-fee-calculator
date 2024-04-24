import services

def get_toll_fee(vehicle, dateTime):
    toll_fee = services.calculate_toll_fee(vehicle, dateTime)
    # Convert toll_fee to JSON and return it
    return {"tollFee": toll_fee}