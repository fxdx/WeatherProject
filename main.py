import matplotlib.pyplot as plt
import matplotlib
import requests


class Forecast:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        print("{}".format(self.name))
        forecast_data = ''
        for key, value in self.data.items():
            forecast_data += 'Date: {}: Temperature - {}K'.format(key, value)
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
    resp = requests.get(complete_url)
    return resp

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

def weatherForecast(name):
    resp = FsendingRequest(name)
    city_info = FjsonInfo(resp, name)
    print(city_info)
    return city_info


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

def graph_plotting(dates_temperatures): #setting graph, doesn't work (yet)
    plt.plot(dates_temperatures.keys(), dates_temperatures.values())
    plt.set_title('Weather Forecast')
    plt.legend(loc='upper left')
    plt.set_ylabel('Temperature')
    plt.set_xlim(xmin=dates_temperatures[0], xmax=dates_temperatures[-1])
    plt.legend(loc=(0.65, 0.8))
    plt.set_title('Forecast')
    plt.yaxis.tick_right()

if __name__ == '__main__':
    name = 'Krakow' #example
    actualWeather(name)
    data = weatherForecast(name)
    graph_plotting(data.data)
