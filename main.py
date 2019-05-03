import numpy
import matplotlib
import requests
import json


class City:
    def __init__(self, name, temperature, atmospheric_pressure):
        self.name = name
        self.temperature = temperature
        self.atmospheric_pressure = atmospheric_pressure


def sendingRequest(name):
    api_key = "3946234ea602bd35b44f48feed6625c4"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    resp = requests.get(complete_url)
    return resp
    
def jsonInfo(resp, name):
    response = resp.json()
    if response['cod'] != '404':
        main_json = response['main']
        temperature = main_json['temp']
        atmospheric_pressure = main_json['pressure']
        city_info = City(name, temperature, atmospheric_pressure)
        return city_info
    else:
        return

def actualWeather(name):
    resp = sendingRequest(name)
    city_info = jsonInfo(resp, name)
    print("{} - temperature: {}K ; atmospheric pressure: {}hPa".format(city_info.name, city_info.temperature, city_info.atmospheric_pressure))

if __name__ == '__main__':
    name = 'Krakow'
    actualWeather(name)
