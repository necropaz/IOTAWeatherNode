def sendRequest(command):
	headers = {'content-type':'application/json'}
	stringified = json.dumps(command)
	request = urllib2.Request(url="http://localhost:14265", data=stringified, headers=headers)
	returnData = urllib2.urlopen(request).read()
	jsonData = json.loads(returnData)
	return jsonData

def searchNewTransaction(address):
	command = {'command':'findTransactions', 'addresses':[address]}
	transaction=sendRequest(command)
	length=len(transaction['hashes'])-1
	data=transaction['hashes'][length].encode('ascii')	
	return data

def readSendersAddress(transaction):
	command = {'command':'getBundle', 'transaction':transaction}
	bundle=sendRequest(command)
	data=messageDecode(bundle['transactions'][1]['address'])
	return data
	
def getNewTransfer(seed):
	command = {'command': 'getTransfers', 'seed': seed, 'securityLevel': 1}
	transactions=sendRequest(command)
	length=len(transaction['hashes'])-1
	data=transaction['hashes'][length].encode('ascii')
	return data
	
def searchMessage(transaction):
	command = {'command':'getBundle', 'transaction': transaction}
	bundle=sendRequest(command)
	data=messageDecode(bundle['transactions'][0]['signatureMessageChunk'])
	message= data.split('}')[0]
	return message

def sendMessage(seed, address, message, value):
	data=messageEncode(message)
	command = {'command':'transfer', 'seed': seed , 'address': address, 'value' : value, 'message': data , 'securityLevel': 1, 'minWeightMagnitude': 13}
	data=sendRequest(command)
	return data

def byteToTryte(char):
	availValues = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	byte=ord(char)
	firstValue = byte % 27
	secondValue = (byte - firstValue) / 27
	trytesValue = availValues[firstValue] + availValues[int(secondValue)]
	return trytesValue
	
def tryteToByte(self, char1,char2):
	availValues = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	firstValue = availValues.rfind(char1)
	secondValue = availValues.rfind(char2)
	byte=(secondValue*27)+firstValue
	return(str(chr(byte)))

def messageEncode(self,message):
	encoded=""
	for i in message:
		encoded= encoded + byteToTryte(i)
	return encoded

def messageDecode(self,trytes):
	decoded=""
	for i in range(0,len(trytes),2):
		decoded= decoded + tryteToByte(trytes[i],trytes[i+1])
	return decoded