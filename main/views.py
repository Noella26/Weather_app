from django.shortcuts import render
import json 
import urllib.request
from .models import CityWeather

# Create your views here.
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=068f15c57ee9b8d62634cb358128a62e').read()

        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={"country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),} 
    return render(request, 'index.html', data) 
  