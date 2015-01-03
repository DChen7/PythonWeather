import urllib2
import json
from twilio.rest import TwilioRestClient

google_url = "http://maps.googleapis.com/maps/api/geocode/json?address="
weather_url = "http://api.openweathermap.org/data/2.5/weather?q="
account_sid = "AC6e810f461c59369afc89d751e0a60129"
auth_token = "4c12e1dd30e30177552bc9bc37a4ae59"
client = TwilioRestClient(account_sid, auth_token)

def send_sms(zip_code, number):
	response = urllib2.urlopen(google_url + str(zip_code)).read()
	json_response = json.loads(response)
	city_name = json_response["results"][0]["formatted_address"]
	print city_name
	response2 = urllib2.urlopen(weather_url + city_name.replace(' ', '%20')).read()
	json_response2 = json.loads(response2)
	weather = json_response2["weather"][0]
	weather_desc = weather["main"] + " | " + weather["description"]
	print weather_desc

	message = client.messages.create(
		body = weather_desc,
		to = number,
		from_ = "+12407433765"
	)


send_sms(20742, phone_number)
