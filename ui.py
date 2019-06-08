import kivy
import downloading_data
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):

    weather_output = ObjectProperty()
    city_text_input = ObjectProperty()

    def actual_weather_button_press(self):

        self.weather_output.text = str(downloading_data.actual_weather_info(self.city_text_input.text))

    def weather_forecast_button_press(self):

        forecast_data = downloading_data.weather_forecast(self.city_text_input.text)
        downloading_data.graph_plotting(forecast_data.data, self.city_text_input.text)
        
    

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()