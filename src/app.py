from flask import Flask
from flask import render_template
import requests
import json
import os

app = Flask(__name__)
tflurl='https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tflrail/status?'
print(tflurl)
LineColours=dict({
    "Bakerloo": "#B36305",
    "Central": "#E32017",
    "Circle": "#FFD300",
    "District": "#00782A",
    "DLR": "#00A4A7",
    "Hammersmith & City": "#F3A9BB",
    "Jubilee": "#A0A5A9",
    "London Overground": "#0019a8",
    "Metropolitan": "#9B0056",
    "Northern": "#000000",
    "Overground": "#EE7C0E",
    "Piccadilly": "#003688",
    "TfL Rail":"#0019a8",
    "Tramlink": "#84B817",
    "Victoria": "#0098D4",
    "Waterloo & City": "#95CDBA",
})
def getFeed():
    myList=[]

    response = requests.get(tflurl)
    apiData = json.loads(response.content)
    for i in apiData:
        myDict={}
        myDict.update({'name':i['name'],'lineStatuses':i['lineStatuses'][0]['statusSeverityDescription'],'LineColour':LineColours.get(i['name'])})
        myList.append(myDict)
    #print(myList[0]['Bakerloo'])
    return tuple(myList)
@app.route('/')
def root():
    response = getFeed()
    return render_template('index.html',posts=response)