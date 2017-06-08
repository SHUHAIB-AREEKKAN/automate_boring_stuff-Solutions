#! /usr/bin/python3
# quickweather.py prints weather report from cmd
import json,requests,sys
#compute location from cmd: get argument cmd
if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location=' '.join(sys.argv[1:])
# Dowmload the JSON data from openweathermap.org API
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=958423162fa4320cd13601725c67f425' % (location)
response=requests.get(url)
response.raise_for_status()
#load JSON data in python variable
weatherData=json.loads(response.text)
# print weather description
w=weatherData['list']
#print(weatherData)
print('Current weather in %s:'(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()

