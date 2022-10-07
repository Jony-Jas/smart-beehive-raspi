import Adafruit_DHT
from datetime import datetime
DHT11 = Adafruit_DHT.DHT11
#function to return temperature and humidity
def temp_hum():
         hum,temp = Adafruit_DHT.read_retry(DHT11,4);
         return temp,hum;
