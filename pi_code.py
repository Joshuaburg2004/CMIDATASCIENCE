import urllib.request
import requests
import threading
from sense_hat import SenseHat
from datetime import datetime
def thingspeak():
	while True:
		sense = SenseHat()
		sense.clear()
		temp = sense.get_temperature() - 12
		if temp != -12:
			time = datetime.now()
			full_datetime = time.strftime("%d/%m/%y at %I:%M%p")
			threading.Timer(15, thingspeak).start()
			URL = 'https://api.thingspeak.com/update?api_keys='
			KEY = 'RF6TOUQX9HPIIDS9'
			HEADER = '&field1={}'.format(temp)
			new_URL = 'https://api.thingspeak.com/update?api_key=BOSOOG8KF43MSQZ6' + HEADER
			data = urllib.request.urlopen(new_URL)
		else:
			continue
if __name__ == '__main__':
	thingspeak()
