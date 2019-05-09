import matplotlib.pyplot as plt
import requests

#Storing informations about weather forecast
class Forecast:
    def __init__(self, name, data):
        self.name = name
        self.data = data #dictionary contains [Date and Hour]: Temperature

    def __str__(self):
        print("{}".format(self.name))
        forecast_data = ''
        for key, value in self.data.items():
            forecast_data += 'Date: {}: Temperature - {}K '.format(key, value)
        return forecast_data

#Storing informations about actual weather
class City:
    def __init__(self, name, temperature, atmospheric_pressure):
        self.name = name
        self.temperature = temperature
        self.atmospheric_pressure = atmospheric_pressure

    def __str__(self):
        return str("{} weather: temperature - {}K; atmospheric pressure - {}hPa".format(self.name, self.temperature, self.atmospheric_pressure))

#OpenWeatherMap api request for 5-day forecast
def FsendingRequest(name):
    k = open('key.txt', 'r', encoding='utf-8-sig') #API key
    api_key = k.read()
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    city_name = name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    resp = requests.get(complete_url)
    return resp

#parsing json to dictionary [date and hour] = temperature
def FjsonInfo(resp, name):
    response = resp.json()
    if response['cod'] != '404':
        dates_temperatures = dict()
        for item in response['list']:
            dates_temperatures[item['dt_txt']] = item['main']['temp']
        forecast_data = Forecast(name, dates_temperatures)
        return forecast_data
    else:
        print('city not found')


#geeting 5-day forecast data
def weatherForecast(name):
    resp = FsendingRequest(name)
    city_info = FjsonInfo(resp, name)
    return city_info

#OpenWeatherMap api request for actual weather
def AsendingRequest(name): #requesting for data (actual weather)
    k = open('key.txt', 'r', encoding='utf-8-sig') #API key
    api_key = k.read()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    resp = requests.get(complete_url)
    return resp

#parsing json to object
def AjsonInfo(resp, name): #transcripting informations (actual weather)
    response = resp.json()
    if response['cod'] != '404':
        temperature = response['main']['temp']
        atmospheric_pressure = response['main']['pressure']
        city_info = City(name, temperature, atmospheric_pressure)
        return city_info
    else:
        print('city not found')

#printing actual weather
def actualWeather(name):
    resp = AsendingRequest(name)
    city_info = AjsonInfo(resp, name)
    print(city_info)

#setting graph for plotting forecast data
def graph_plotting(dates_temperatures, city):
    plt.figure(figsize=(15, 7))
    plt.bar(range(len(dates_temperatures)), list(dates_temperatures.values()), align='edge', width= 0.5, color='red')
    plt.xticks(range(len(dates_temperatures)), list(dates_temperatures.keys()))
    plt.title('{} Weather Forecast {} - {}'.format(city, list(dates_temperatures.keys())[0], list(dates_temperatures.keys())[-1]))
    plt.tick_params(axis='x', rotation=70)
    plt.spring()
    plt.show()

if __name__ == '__main__':
    city = 'Krakow' #example
    actualWeather(city)
    forecast_data = weatherForecast(city)
    graph_plotting(forecast_data.data, city)
