import json
from time import time
from random import random
from flask import Flask, render_template, make_response

app = Flask(__name__)

import json

from websocket import create_connection
ws = create_connection("wss://api2.bitfinex.com:3000/ws")
#ws.connect("wss://api2.bitfinex.com:3000/ws")
ws.send(json.dumps({
    "event": "subscribe",
    "channel": "book",
    "pair": "BTCUSD",
    "prec": "P0"
}))



@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    result = ws.recv()
    result = json.loads(result)
    if type(result) == list:
        price = result[1]
    else:
        price = 0
    data = [time() * 1000, price]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    print(data)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
