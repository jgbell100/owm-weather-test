import googlemaps
import pyowm
import sys
from apikey import google_api_key, owm_api_key


def getLatLongFromAddress(address):

	geocode_result = gmaps.geocode(address)
	geometry = [d['geometry'] for d in geocode_result if 'geometry' in d]
	location = [d['location'] for d in geometry if 'location' in d]
	lat = [d['lat'] for d in location if 'lat' in d]
	lng = [d['lng'] for d in location if 'lng' in d]
	return lat[0], lng[0]

def getElevationFromLatLong(lat, lng):
	elev = gmaps.elevation((lat,lng))
	elev = [d['elevation'] for d in elev if 'elevation' in d][0]
	return elev


gmaps = googlemaps.Client(key=google_api_key)
owm = pyowm.OWM(owm_api_key)  

if len(sys.argv) == 2:
	address = sys.argv[1]	
else:
	print ("Usage: python %s <address>") % sys.argv[0]
	exit(0)

lat, lng = getLatLongFromAddress(address)

observation_list = owm.weather_around_coords(lat, lng)
weather = observation_list[0].get_weather()

wind_speed = weather.get_wind()['speed']
humidity = weather.get_humidity()
status = weather.get_status()

print wind_speed
print humidity
print status



