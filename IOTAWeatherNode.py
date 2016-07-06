import sys
import json
import urllib2
import os


adress="RVORZ9SIIP9RCYMREUIXXVPQIPHVCNPQ9HZWYKFWYWZRE9JQKG9REPKIASHUUECPSQO9JT9XNMVKWYGVAZETAIRPTM"

def sendRequest(command):
	headers = {'content-type':'application/json'}
	request = urllib2.Request(url="http://localhost:14265", data=command, headers=headers)
	returnData = urllib2.urlopen(request).read()
	jsonData = json.loads(returnData)
	return returnData

def searchRequest():
    command = "{'command':'findTransactions', 'adresses':['"+adress+"']}"
    print(sendRequest(command))
    #print(transaction)
	#command = "{'command':'getBundle', 'hash': '"+transaction+"'}"
    #jsonData=sendRequest(command)
    #print(jsonData)

def readRequestRaw(trytes):
	command = {'command':'analyzeTransactions', 'trytes': trytes}
	stringified = json.dumps(command)
	headers = {'content-type':'application/json'}
	request = urllib2.Request(url="http://localhost:14265", data=stringified, headers=headers)
	returnData = urllib2.urlopen(request).read()
	jsonData = json.loads(returnData)
	return jsonData

def sendTransfer(seed, senderAdress, message):
	command = {'command':'transfer', 'seed': seed, 'adress': senderAdress, 'value': '0', 'message' : message, 'securityLevel':'1', 'minWeightMagnitude': '13' }
	stringified = json.dumps(command)
	headers = {'content-type':'application/json'}
	request = urllib2.Request(url="http://localhost:14265", data=stringified, headers=headers)
	returnData = urllib2.urlopen(request).read()
	jsonData = json.loads(returnData)
	return jsonData

def readWeather():
	humidity = sense.get_humidity()
	temperatur= sense.get_teperature()
	pressure = sense.get_pressure()
	return "Temperature:"+temperatur+"Humidity:"+humidity+"Pressure:"+pressure

def initSensHat():
	sense=SenseHat()

def sendWeather(seed, senderAdress):
	message=readWeather()
	tail=sendTransfer(seed, senderAdress, message)
	return tail

def scrollText(message):
	sense.show_message(message,text_colour=[255, 0, 0])

def main(argv):
    #adress="RVORZ9SIIP9RCYMREUIXXVPQIPHVCNPQ9HZWYKFWYWZRE9JQKG9REPKIASHUUECPSQO9JT9XNMVKWYGVAZETAIRPTM"
    searchRequest()

if __name__ == "__main__":
    print "Starting spammer"
    main(sys.argv[1:])
