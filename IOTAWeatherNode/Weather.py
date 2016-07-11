from sense_hat import SenseHat

def readWeather():
	temperature = sense.temperature()
	humidity = sense.get_humidity()
	pressure = sense.get_pressure()
	return "{'Temperature':'"+str(temperature)+"', 'Humidity':'"+str(humidity)+"','Pressure':'"+str(pressure)"'}"

def initSensHat():
	sense=SenseHat()

def scrollText(message):
	sense.show_message(message,text_colour=[255, 0, 0])
