import downloadMp3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (800, 30)

# future: use kivy core audio for playback


class YmpBar(BoxLayout):
    def download_mp3(value):
        downloadMp3.main(value.ids.name.text) 
    pass

class YmpMenu(Widget):
    pass
class YmpApp(App):
    def build(self):
        return YmpBar()



if __name__ == '__main__':
    YmpApp().run()