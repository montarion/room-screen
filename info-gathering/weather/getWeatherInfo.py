import requests
import urllib.request, json

def getWeather():
    ##Check response of API-Call
    # response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=3e7479392874b48638d0847329f31fad')
    #
    # if response.status_code == 200:
    #     print("Gelukt")
    # else:
    #     print("Error")

    ##read out most relevant data of received JSON
    with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?id=2745912&APPID=3e7479392874b48638d0847329f31fad") as url:
        #data= JSON string
        data = json.loads(url.read().decode())
        
        print(str(data["city"]["name"])+", "+str(data["city"] ["country"]))
        gradenC = ((data["list"][1]["main"]["temp"])-272.15)
        print("Graden in C: "+ str(gradenC.__round__(1)))
        print("Weather forecast: "+str(data["list"][1]["weather"][0]["description"]))
        print("Humidity: "+str(data["list"][1]["main"]["humidity"])+"%")
        print(data["list"][1]["main"])
    
getWeather()
