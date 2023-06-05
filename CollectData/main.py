import websocket
import os
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json 
import sys

lastTime = 0
fileName = 'test.json'
label = 8
f = open(fileName,)
finalData = json.load(f,)
numData = -1
numCurFrame = 0
Left = []
Right = []
newData = []


def on_message(ws, message):
    global numData
    global lastTime
    global numCurFrame

    data = json.loads(message)
    curTime = time.time() * 10 
    data['label'] = label

    print("Numdata", numData)
    print("Time: ", curTime)
    print("LastTime: ", lastTime)

    if curTime - lastTime >= 0.5 : 
        lastTime = curTime
        numCurFrame += 1
        print("Numcurframe: ",numCurFrame)

        if numCurFrame == 1:
            numCurFrame = 0
            numData += 1
            print("Numdata: ", numData)

    if numData == 10:
        # finalData.pop(0)
        # with open(fileName, 'w') as outfile:
        #         json.dump(finalData, outfile)
        sys.exit()
                
        
def on_error(ws, error):
    print(1)

def on_close(ws):
    print("### closed ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:6437/v7.json",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)
    
    ws.run_forever()