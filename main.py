import numpy
import matplotlib
import requests
import json


class Forecast:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        print("{}".format(self.name))
        forecast_data = ''
        for key, value in self.data.items():
            forecast_data += 'Date: {}: Temperature - {}'.format(key, value)
        return forecast_data

class City:
    def __init__(self, name, temperature, atmospheric_pressure):
        self.name = name
        self.temperature = temperature
        self.atmospheric_pressure = atmospheric_pressure

    def __str__(self):
        return str("{} weather: temperature - {}K; atmospheric pressure - {}hPa".format(self.name, self.temperature, self.atmospheric_pressure))


def FsendingRequest(name):
    k = open('key.txt', 'r', encoding='utf-8-sig') #API key
    api_key = k.read()
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    city_name = name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    print(complete_url)
    resp = requests.get(complete_url)
    return resp

def FjsonInfo(resp, name):
    response = resp.json()
    if response['cod'] != '404':
        dates = dict()
        for item in response['list']:
            dates[item['dt_txt']] = item['main']
        forecast_data = Forecast(name, dates)
        print(dates)
        return forecast_data
    else:
        print('city not found')

def weatherForecast(name):
    resp = FsendingRequest(name)
    city_info = FjsonInfo(resp, name)
    print(city_info)


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
        temperature = response['main']['temp']
        atmospheric_pressure = response['main']['pressure']
        city_info = City(name, temperature, atmospheric_pressure)
        return city_info
    else:
        print('city not found')

def actualWeather(name):
    resp = AsendingRequest(name)
    city_info = AjsonInfo(resp, name)
    print(city_info)

if __name__ == '__main__':
    name = 'Krakow' #example
    #actualWeather(name)
    weatherForecast(name)
