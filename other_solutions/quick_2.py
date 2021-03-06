

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickweather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from openweathermap.org's API
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=958423162fa4320cd13601725c67f425' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into Python variable.
weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
