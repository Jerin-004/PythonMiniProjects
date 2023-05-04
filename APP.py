import kivy
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label (text ="Jerin")


if __name__ == "__main__":
    MyApp().run()

