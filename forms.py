import requests
from flask import Flask, render_template, request

url='https://api.meteo.lt/v1/places/{}/forecasts/long-term'
place ='Vilnius'
place2 = 'Kaunas'
place3 = 'Marijampolė'
#------VILNIUS------
r1 = requests.get(url.format(place)).json()

weather_data = []
weather = {
    'place' : place,
    'time': r1['forecastTimestamps'][60]['forecastTimeUtc'],
    'temperature':r1['forecastTimestamps'][60]['airTemperature']
}
weather_data.append(weather)

#------KAUNAS-------
r2 = requests.get(url.format(place2)).json()
weather_data2 = []
weather2 = {
    'place': place2,
    'time': r2['forecastTimestamps'][60]['forecastTimeUtc'],
    'temperature': r2['forecastTimestamps'][50]['airTemperature']
}
weather_data2.append(weather2)

# ------MARIJAMPOLE-------
r3 = requests.get(url.format(place2)).json()

weather_data3 = []
weather3 = {
    'place': place3,
    'time': r3['forecastTimestamps'][60]['forecastTimeUtc'],
    'temperature': r3['forecastTimestamps'][60]['airTemperature']
}
weather_data3.append(weather3)
