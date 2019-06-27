import matplotlib.pyplot as plt
import requests
import city_forecast
import city_actual_weather


# OpenWeatherMap api request for 5-day forecast
def forecast_data_sending_api_request(c_name):
    k = open('key.txt', 'r', encoding='utf-8-sig') # API key
    api_key = k.read()

    base_url = "http://api.openweathermap.org/data/2.5/forecast?"

    city_name = c_name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    resp = requests.get(complete_url)
    return resp


# Parsing json to dictionary [date and hour] = temperature
def forecast_data_json_parsing(resp, name):
    response = resp.json()

    if response['cod'] != '404':

        dates_temperatures = dict()

        for item in response['list']:
            dates_temperatures[item['dt_txt']] = item['main']['temp']
        
        forecast_data = city_forecast.CityForecast(name, dates_temperatures)

        return forecast_data

    else:
        print('city not found')


# Geting 5-day forecast data
def weather_forecast(name):
    resp = forecast_data_sending_api_request(name)

    city_info = forecast_data_json_parsing(resp, name)
    return city_info


# OpenWeatherMap api request for actual weather
def actual_weather_sending_api_request(c_name): # Requesting for data (actual weather)
    k = open('key.txt', 'r', encoding='utf-8-sig') # API key
    api_key = k.read()

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = c_name
    complete_url = base_url + "appid=" \
                    + api_key + "&q=" \
                    + city_name

    json_response = requests.get(complete_url)
    return json_response


# Parsing json to object
def actual_weather_json_parsing(resp, name): # Transcripting informations (actual weather)
    response = resp.json()

    if response['cod'] != '404':

        temperature = response['main']['temp']
        atmospheric_pressure = response['main']['pressure']
        city_info = city_actual_weather.CityActualWeather(name, 
                                    temperature,
                                    atmospheric_pressure)
        return city_info
        
    else:
        return 'City not found'


# Printing actual weather
def actual_weather_info(name):

    json_response = actual_weather_sending_api_request(name)

    city_info = actual_weather_json_parsing(json_response, name)

    return str(city_info)


# Setting graph for plotting forecast data
def graph_plotting(dates_temperatures, city):
    plt.figure(figsize=(15, 7))

    plt.bar(range(len(dates_temperatures)), 
            [value-273 for value in dates_temperatures.values()],
            align='edge', 
            width= 0.5, 
            color='red') # Kelvins to Celsius

    plt.xticks(range(len(dates_temperatures)), list(dates_temperatures.keys()))

    plt.title('{} Weather Forecast {} - {}'.format(city,
                                                    list(dates_temperatures.keys())[0], 
                                                    list(dates_temperatures.keys())[-1]))

    plt.tick_params(axis='x', rotation=70)
    plt.spring()

    plt.show()

#testing purposes
#if __name__ == '__main__':
    #city = input()
    #actual_weather_info(city)
    #forecast_data = weather_forecast(city)
    #graph_plotting(forecast_data.data, city)
