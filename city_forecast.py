# Storing informations about weather forecast
class CityForecast:
    def __init__(self, 
                name, 
                data):
        
        self.name = name
        self.data = data # Dictionary contains [Date and Hour]: Temperature

    def __str__(self):
        print("{}".format(self.name))

        forecast_data = ''
        for key, value in self.data.items():
            forecast_data += 'Date: {}: Temperature - {}C '.format(key, value-273)
        
        return forecast_data