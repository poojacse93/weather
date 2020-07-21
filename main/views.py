from django.shortcuts import render
import requests
# Create your views here.
import json
import urllib.request

def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        #source = urllib.request.urlopen(
        source = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=95134bad9106b116b9accdb0bf532de6'
            #'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=95134bad9106b116b9accdb0bf532de6').read()
            

        
        #list_of_data = json.loads(source)
        list_of_data = requests.get(source.format(city)).json()
        

        data = {
            "country_code": list_of_data['sys']['country'],
           "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            #"temp": str(list_of_data['main']['temp']) + 'K' ,
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": (list_of_data['main']['pressure']),
            "humidity": (list_of_data['main']['humidity']),
            "description": (list_of_data['weather'][0]['description']),
        }
        print(data)
    else:
        data = {}
    return render(request,"main/index.html", data)