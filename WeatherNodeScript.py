import sys
import json
import time
import os
import iota

#Here you can enter the simulatet weather Data
temperature="30"	#Temperature in Celsius (only for simulation)
humidity="52"		#Humidity in percent (only for simulation)
pressure="1016"		#Pressure in mbar (only for simulation)
#uncomment the next line if you wana use a sense HAT
#Node.Weather.initSensHat()

#Write here the IOTA adress of the Weather Node.
address=input("Address IOTA Node? ")

#Enter here your seed.
seed=input("Address IOTA Node Seed? ")
node=iota(seed)
print("Weather Node is Running.")
print("Waiting until the Weatehr Node recived a request.")
txCounter=node.txCounter
while True:
	time.sleep(5)
	self.transaction=node.searchNewTransaction()
	if txCounter!=node.txCounter
		break            

commandRecived=Node.IOTA.searchMessage(transaction)
commandRecived=commandRecived.replace('\'','\"')
jsonData=json.loads(commandRecived)
if jsonData['command']=="getWeather" :
	#message=Node.Weather.readWeather()
	message="{'Temperature':'"+temperature+"', 'Humidity':'"+humidity+"','Pressure':'"+pressure+"'}"
	print(message)
	node.sendMessage(address, message, '1')
	print("Succesfully send request.")
elif jsonData['command']=="sendPromotion":
	print("Promotion request recived")
	print("Promotion Text:"+jsonData['promotion'])
	#Node.Weather.scrollText(jsonData['promotion'])
else:
	print("Can't read sucessfully a command."+jsonData)

print("End Iota Weather Node!")
