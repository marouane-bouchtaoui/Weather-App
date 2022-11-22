import json
from django.shortcuts import render
import requests
import datetime as dt
# Create your views here.
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'paris'

    appid = 'ffedea671617c2b25d5dacb3040397f2'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    status = res['weather'][0]['main']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    feltT = res['main']['feels_like']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    wind = res['wind']['speed']
    sunrise = dt.datetime.utcfromtimestamp(res['sys']['sunrise'] + res['timezone'])
    sunset = dt.datetime.utcfromtimestamp(res['sys']['sunset'] + res['timezone'])
    day = dt.date.today()

    return render(request, 'weatherApp/index.html', {'description':description,
     'icon':icon ,'temp':temp, 'pressure':pressure, 'humidity':humidity, 'day':day, 'city':city,
     'wind':wind, 'status':status, 'sunrise':sunrise, 'sunset':sunset, 'feltT':feltT})