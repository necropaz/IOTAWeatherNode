import sys
import json
import time
import os
import IOTAWeatherNode as Node

#Write here the IOTA adress of the Weather Node.
address="RVORZ9SIIP9RCYMREUIXXVPQIPHVCNPQ9HZWYKFWYWZRE9JQKG9REPKIASHUUECPSQO9JT9XNMVKWYGVA"

#Enter here your seed.
seed=""

promotionText="This is my promotion!"
commandWeather="{'command':'getWeather'}"
commandPromotion="{'command':'sendPromotion','promotion':'"+promotionText+"'}"

#If you want to request the actuel Weather set command=commandWeather
#If you want to send a Promotion to the Weather Node type command=commandPromotion
#command=commandPromotion
command=commandWeather

transactionOld=Node.IOTA.searchNewTransaction2(seed)
print("Node.IOTA.sendMessage(self,"+ seed +","+ address+","+ command+", '1'")
Node.IOTA.sendMessage(seed, address, command, '1')
print("Succesfully send request.")

if(command=commandWeather):
	print("Waiting until the Weatehr Node send back the Weather Infos.")
	while True:
		time.sleep(5)
		self.transaction=Node.IOTA.searchNewTransaction2(self.seed)
		if self.transactionOld!=self.transaction:
			self.transactionOld=self.transaction
			break            
            
	commandRecived=Node.IOTA.searchMessage(transaction)
	commandRecived=commandRecived.replace('\'','\"')
	jsonData=json.loads(commandRecived)
	print("Temperatur: "+jsonData['temperature'+"Humidity: "+jsonData['humidity']+"Pressure: "+jsonData['pressure'])

