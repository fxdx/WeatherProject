# Storing informations about actual weather
class CityActualWeather:
    def __init__(self, name, 
                temperature, atmospheric_pressure):
        
        self.name = name
        self.temperature = temperature
        self.atmospheric_pressure = atmospheric_pressure

    def __str__(self):
        return str("{} weather: temperature - {}C; atmospheric pressure - {}hPa".format(self.name, 
                                                                                        round(self.temperature-273, 2), 
                                                                                        round(self.atmospheric_pressure, 2)))