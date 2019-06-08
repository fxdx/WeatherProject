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

    actual_weather_output = ObjectProperty()
    city_text_input = ObjectProperty()

    def actual_weather_button(self, country_name):
        print(country_name)
        self.actual_weather_output.text = str(downloading_data.actual_weather_info(self.city_text_input.text))

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()