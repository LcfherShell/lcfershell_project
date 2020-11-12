import requests
import json 
import urllib.request 
import re

def Weatcher():
    xurl =  'http://ipinfo.io/json'
    response = urllib.request.urlopen(xurl).read()
    get_data = json.loads(response)
    ip4= get_data['ip']
    unit = get_data['city']+','+get_data['region']+','+get_data['country']
    loc  = unit.replace(',',', ')
    city = unit.replace(' ','%20')
    url= urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=7310eead122b20022cf7f76c947ce0ea').read() 
    list_of_data = json.loads(url) 
    data = { 
        "ip4": str(ip4),
        "loc": str(loc), 
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": str(list_of_data['coord']['lon'])+' '+ str(list_of_data['coord']['lat']), 
        "temp": str(list_of_data['main']['temp']) + 'k',
        "description": list_of_data['weather'], 
        "pressure": str(list_of_data['main']['pressure']), 
        "humidity": str(list_of_data['main']['humidity']), 
    } 
    return data

weather = Weatcher()

ip4 = weather['ip4']
loc = weather['loc']
country_code = weather['country_code']
coordinate = weather['coordinate']
temperatur =  weather['temp']
description = weather['description']#for
pressure = weather['pressure']
humidity = weather['humidity']
for s in description:
        clouds = s['description'] 

print(' * Running Module: Weather')
