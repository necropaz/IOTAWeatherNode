# This Python file uses the following encoding: utf-8
import sys
import json
import time
import os
import IOTAWeatherNode as Node

#Here you can enter the simulatet weather Data
temperature="30"		#Temperature in °C (only for simulation)
humidity="52"		#Humidity in percent (only for simulation)
pressure="1016"		#Pressure in mbar (only for simulation)
#uncomment the next line if you wana use a sense HAT
#Node.Weather.initSensHat()

#Write here the IOTA adress of the Weather Node.
address="RVORZ9SIIP9RCYMREUIXXVPQIPHVCNPQ9HZWYKFWYWZRE9JQKG9REPKIASHUUECPSQO9JT9XNMVKWYGVA"

#Enter here the seed which belongs to the IOTA Weather Node Address.
seed=""


promotionText="This is my promotion!"
commandWeather="{'command':'getWeather'}"
commandPromotion="{'command':'sendPromotion','promotion':'"+promotionText+"'}"

transactionOld=Node.IOTA.searchNewTransaction2(seed)
print("Weather Node is Running.")
print("Waiting until the Weatehr Node recived a request.")
while True:
	time.sleep(5)
	self.transaction=Node.IOTA.searchNewTransaction2(self.seed)
	if self.transactionOld!=self.transaction:
		self.transactionOld=self.transaction
		break            
            
	commandRecived=Node.IOTA.searchMessage(transaction)
	commandRecived=commandRecived.replace('\'','\"')
	jsonData=json.loads(commandRecived)
	if jsonData['command']=="getWeather" :
		#message=Node.Weather.readWeather()
		message="{'Temperature':'"+temperature+"', 'Humidity':'"+humidity+"','Pressure':'"+pressure"'}"
		print("Node.IOTA.sendMessage(self,"+ seed +","+ address+","+ message+", '1'")
		Node.IOTA.sendMessage(seed, address, message, '1')
		print("Succesfully send request.")
	elif jsonData['command']=="sendPromotion":
		print("Promotion request recived")
		print("Promotion Text:"+jsonData['promotion'])
		#Node.Weather.scrollText(jsonData['promotion'])

	else:
		print("Can't read sucessfully a command."+jsonData)
	print("Temperatur: "+jsonData['temperature'+"Humidity: "+jsonData['humidity']+"Pressure: "+jsonData['pressure'])

