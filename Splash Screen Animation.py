# Modified from https://canerblt.wordpress.com/2015/05/25/python-kivy-and-raspberrypi-an-image-and-clock-usage-example/
from kivy.app import App
from kivy.uix.image import Image
from kivy.animation import Animation

class My_Splash_Screen_App(App):

    def build(self):

        '''Splash Screen'''
        my_splash_screen = Image(source='jukebox.png',pos=(800,800))
        animation = Animation(x=0, y=0, d=2, t='out_bounce');
        animation.start(my_splash_screen)

        return my_splash_screen

if __name__ == '__main__':
    My_Splash_Screen_App().run()