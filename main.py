import numpy
import matplotlib
import requests
import json


class City:
    def __init__(self, name, temperature, atmospheric_pressure):
        self.name = name
        self.temperature = temperature
        self.atmospheric_pressure = atmospheric_pressure


def FsendingRequest(name):
    k = open('key.txt', 'r', encoding='utf-8-sig') #API key
    api_key = k.read()
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    city_name = name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    resp = requests.get(complete_url)
    return resp

def FjsonInfo(resp, name):
    response = resp.json()
    if response['cod'] != '404':
        print(response)
    else:
        print('city not found')

def weatherForecast(name):
    resp = FsendingRequest(name)
    city_info = FjsonInfo(resp, name)


def AsendingRequest(name): #requesting for data (actual weather)
    k = open('key.txt', 'r', encoding='utf-8-sig') #API key
    api_key = k.read()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    resp = requests.get(complete_url)
    return resp
    
def AjsonInfo(resp, name): #transcripting informations (actual weather)
    response = resp.json()
    if response['cod'] != '404':
        main_json = response['main']
        temperature = main_json['temp']
        atmospheric_pressure = main_json['pressure']
        city_info = City(name, temperature, atmospheric_pressure)
        return city_info
    else:
        print('city not found')

def actualWeather(name):
    resp = AsendingRequest(name)
    city_info = AjsonInfo(resp, name)
    print("{} - temperature: {}K ; atmospheric pressure: {}hPa".format(city_info.name, city_info.temperature, city_info.atmospheric_pressure))

if __name__ == '__main__':
    name = 'Krakow' #example
    actualWeather(name)
    #weatherForecast(name)
