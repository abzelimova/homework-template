from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.



def weather(request):
    try:
        url = "http://api.openweathermap.org/data/2.5/find?q=Moscow,RU&APPID=405aa012a8db633c20c30217f4159ce4"
        try:
            json_data = getAPI(url)
        except Exception as e:
            raise ConnectionError
        temper = int(json_data['list'][0]['main']['temp'] - 273)
        city = json_data['list'][0]['name']
        press = json_data['list'][0]['main']['pressure'] / 10
        sp =  json_data['list'][0]['wind']['speed']
        return  render(request, 'weather/index.html', {
            'name' : city,
            'temp' : temper,
            'pressure': press,
            'speed': sp,
        })
    except ConnectionError:
        return render(request, 'weather/error.html')

def getAPI(url):
    r = requests.get(url)
    return r.json()
