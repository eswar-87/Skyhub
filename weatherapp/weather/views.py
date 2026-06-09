from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import requests
from django.conf import settings
import datetime

# Create your views here.
def home(request):
    data = {}
    error_message = None
    
    # Check if API key is configured
    api_key_missing = not getattr(settings, 'WEATHER_API_KEY', '')
    
    if api_key_missing:
        error_message = "OpenWeatherMap API Key is not configured. Please set the WEATHER_API_KEY environment variable in Render."

    if request.method == 'POST':
        if api_key_missing:
            # Keep the warning message
            pass
        else:
            city = request.POST.get('city', '').strip()
            lat = request.POST.get('lat')
            lon = request.POST.get('lon')

            try:
                if city:
                    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.WEATHER_API_KEY}"
                elif lat and lon:
                    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={settings.WEATHER_API_KEY}"
                else:
                    raise ValueError("No location provided")

                response = requests.get(url)
                list_of_data = response.json()

                if response.status_code == 200:
                    today = datetime.datetime.now()
                    current_date = today.strftime("%d %b, %Y")
                    current_day = today.strftime("%A")

                    data = {
                        "city": list_of_data.get('name', city).title(),
                        "coordinate": f"{list_of_data['coord']['lat']}°, {list_of_data['coord']['lon']}°",
                        "temp": round(list_of_data['main']['temp'], 1),
                        "feels_like": round(list_of_data['main']['feels_like'], 1),
                        "humidity": list_of_data['main']['humidity'],
                        "weather": list_of_data['weather'][0]['main'],
                        "description": list_of_data['weather'][0]['description'].title(),
                        "icon": list_of_data['weather'][0]['icon'],
                        "date": current_date,
                        "day": current_day,
                        "wind_speed": list_of_data['wind']['speed'],
                    }
                else:
                    error_message = list_of_data.get('message', 'City not found').title()
            except Exception as e:
                error_message = "An error occurred while fetching weather data."
    else:
        # If API key is present, no error message on initial load
        if not api_key_missing:
            error_message = None

    return render(request, 'home.html', {"data": data, "error": error_message})
