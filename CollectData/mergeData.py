import json
import os
import sys

finalData = []
fileName = 'rawData-test'

label = ['A-1-test', 'B-0-test', 'D-5-test', 'I-4-test', 'M-3-test', 'N-2-test']

#XinChao: 0
#Toi: 1
#Ten: 2
#MoiNguoi: 3

for curLabel in label:
    newLabel = curLabel + '.json'
    f = open( './test/' + newLabel,)
    Data = json.load(f)
    for curData in Data:
        exists = True
        if exists == True:
            finalData.append(curData)
        
with open(fileName + '.json', 'w') as outfile:
    json.dump(finalData, outfile)