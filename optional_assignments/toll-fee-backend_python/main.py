from flask import Flask, request
import handlers

app = Flask(__name__)

@app.route('/get-toll-fee', methods=['GET'])
def get_toll_fee():
    vehicle = request.args.get('vehicle')
    dateTime = request.args.get('dateTime')
    return handlers.get_toll_fee(vehicle, dateTime)

@app.route('/get-all-fees-for-vehicle', methods=['POST'])
def get_all_fees_for_vehicle():
    vehicle = request.json.get('vehicle')
    passage_dates = request.json.get('passageDates')
    return {'vehicle': vehicle, 'passageDates': passage_dates, 'cost': 0}

@app.route('/get-all-fees-for-list', methods=['POST'])
def get_all_fees_for_list():
    passages = request.json.get('passages')
    total_fee = 0
    for passage in passages:
        total_fee += 1
    return {'nrPassages': len(passages), 'totalFee': total_fee}

@app.route('/ping', methods=['GET'])
def ping():
    return {"status": "Server is running"}

if __name__ == '__main__':
    app.run(port=8080)