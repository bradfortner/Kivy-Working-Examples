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
        # Gray background
        canvas.before:
            BorderImage:
                source: 'background.png'
                pos: self.pos
                size: self.size
        Scatter:
            center: self.parent.center
            do_rotation: False
            do_translation: False
            do_scale: False
            rotation: app.angle
            scale: min(self.parent.width/self.width, self.parent.height/self.height)
            Image:
                source: '45rpm.png'             
"""
class RotateRecordApp(App):
    angle = NumericProperty(0)
    def build(self):
        Clock.schedule_interval(self.update_angle, 0)
        return Builder.load_string(kv)

    def update_angle(self, dt, *args):
        self.angle += dt * 100

if __name__ == '__main__':
    RotateRecordApp().run()