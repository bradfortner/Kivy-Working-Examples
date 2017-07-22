# Modified from https://gist.github.com/tshirtman/6222891
import kivy
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.clock import Clock
kivy.require("1.9.1")  # used to alert user if this code is run on an earlier version of Kivy.

kv = """
BoxLayout:
    Widget:
        canvas.before:
            BorderImage:
                source: 'retro.jpg'
                pos: self.pos
                size: self.size
        Scatter:
            size_hint: None,None
            pos: 360,290
            do_rotation: False
            do_translation: False
            do_scale: False
            rotation: app.angle
            scale: 4.1
            Image:
                source: 'convergence_logo.png' 
        Label:
            text: "Convergence Music System 2.0"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 348,520
        Label:
            text: "Convergence Music System 2.0"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 352,520
        Label:
            text: "Convergence Music System 2.0"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 350,518
        Label:
            text: "Convergence Music System 2.0"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 350,522
        Label:
            text: "Convergence Music System 2.0"
            color: 1,1,1,1 # Sets text colour to white.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 350,520
        Label:
            text: "We're Starting Up...."
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 128,90
        Label:
            text: "We're Starting Up...."
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 132,90
        Label:
            text: "We're Starting Up...."
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 130,92
        Label:
            text: "We're Starting Up...."
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 130,88
        Label:
            text: "We're Starting Up...."
            color: 1,1,1,1 # Sets text colour to white.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 130,90
        Label:
            text: "Please Do Not Adjust Your Media Device!"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 388,30
        Label:
            text: "Please Do Not Adjust Your Media Device!"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 392,30
        Label:
            text: "Please Do Not Adjust Your Media Device!"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 390,28
        Label:
            text: "Please Do Not Adjust Your Media Device!"
            color: 0,0,0,1 # Sets text colour to black used as font edge.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 390,32
        Label:
            text: "Please Do Not Adjust Your Media Device!"
            color: 1,1,1,1 # Sets text colour to white.
            font_size: 35
            bold: True
            size_hint: None,None
            pos: 390,30
"""
class RotateLogoApp(App):
    angle = NumericProperty(0)
    def build(self):
        Clock.schedule_interval(self.update_angle, 0)
        return Builder.load_string(kv)

    def update_angle(self, dt, *args):
        self.angle += dt * 100

if __name__ == '__main__':
    RotateLogoApp().run()