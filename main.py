from kivy.config import Config
Config.set('graphics','height','400')
Config.set('graphics','width','200')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label


class HelloWorldApp(App):
    def build(self):
        screen=BoxLayout()
        l=Label(text='hello')
        screen.add_widget(l)
  
        return screen

if __name__ == '__main__':
    HelloWorldApp().run()   
