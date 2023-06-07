import websocket
import os
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json 
import sys

label = 5

fileName = 'D-5-test.json'
f = open(fileName,)
finalData = json.load(f,)

numData = 0

def on_message(ws, message):
    global numData

    data = json.loads(message)
    data['label'] = label

    if data['hands'] and data['hands'][0]['type'] == "right" and len(data['hands']) == 1 : 
        numData += 1
        print("Numdata: ", numData)
        finalData.append(data)

    if numData == 200:
        with open(fileName, 'w') as outfile:
                json.dump(finalData, outfile)
        sys.exit()
                
        
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:6437/v7.json",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)
    
    ws.run_forever()