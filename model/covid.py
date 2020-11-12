import json
from urllib import request
import sys
import os

url = "https://api.covid19api.com/summary"

# lakukan http request
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())
#print(data['data'][0]['provinsi'])
# ambil class json dam tampilkan data
global_confirm = data['Global']['NewConfirmed']
global_totalConfirm = data['Global']['TotalConfirmed']
global_newDeaths= data['Global']['NewDeaths']
global_totalDeaths= data['Global']['TotalDeaths']
global_newRecovered= data['Global']['NewRecovered']
global_totalRecovered= data['Global']['TotalRecovered']
countries = data['Countries']
fect= {"global":[{"newconfirm": global_confirm,"totalconfirm": global_totalConfirm,"newdeaths": global_newDeaths,"totaldeaths": global_totalDeaths,"newrecover": global_newRecovered,"totalrecover": global_totalRecovered}]}
wcovid = fect['global']
#print(wcovid)
#for covid in countries:
 #   print("Country: "+covid['Country']+" Country Code: "+covid['CountryCode'])
 #   print("Confirm:"+str(covid['NewConfirmed']))
