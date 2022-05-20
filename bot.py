import websocket, json, pprint

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print("CONNECTION OPENED")

def on_close(ws):
    print("CONNECTION CLOSED")

def on_message(ws, msg):
    json_msg = json.loads(msg)
    # pprint.pprint(json_msg)      
    candle = json_msg['k']
    is_candle_closed = candle['x']
    closed_at = candle['c']
    if is_candle_closed:
        print("candle closed at {}".format((closed_at)))


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)

ws.run_forever()

