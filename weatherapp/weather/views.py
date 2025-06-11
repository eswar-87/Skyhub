from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import requests
from django.conf import settings
import datetime

# Create your views here.
def home(request):
    data={}
    if request.method == 'POST':
        city = request.POST['city']
        source = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}".format(city,settings.WEATHER_API_KEY)
        list_of_data = requests.get(source.format(city)).json()

        today=datetime.datetime.now()
        current_date=today.strftime("%d-%m-%Y")
        current_day=today.strftime("%A")


        data = {
            "city": city,
            "coordinate" : str(list_of_data['coord']['lat']) + '   ' +str(list_of_data['coord']['lon']),
            "temp" : round((list_of_data['main']['temp'] -32) * 5.0/9.0,2),
            "humidity" : str(list_of_data['main']['humidity']),
            "weather" : list_of_data['weather'][0]['description'].title(),
            "date" : current_date,
            "day" : current_day,
        }

    else:
        data = {}
    return render(request,'home.html',{"data":data})
