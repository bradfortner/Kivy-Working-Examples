# Modified from https://github.com/brousch/pyohio-kivy-tutorial/blob/master/tutorial/step11_tts/saythis.kv
# And https://stackoverflow.com/questions/45217816/kivy-addressing-an-ellipse-widget-created-in-kv-language-using-python

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
kivy.require("1.9.1")

Builder.load_string('''
<Ball@Widget>
    size: 70, 70
    pos: 350,290
    size_hint: None, None
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            pos: self.pos
            size: self.size
<ShrinkThis>:
    button_font_size: '30sp'
    my_circle: my_circle
    Ball:
        id: my_circle
    Button:
        text: 'Shrink & Reposition Circle'
        font_size: root.button_font_size
        size_hint: 1, None
        on_press: root.shrink_reposition_circle()            
''')

class ShrinkThis(FloatLayout):

    my_circle = ObjectProperty(None)

    def shrink_reposition_circle(self):
        self.my_circle.size = (10,10)
        self.my_circle.pos = (300, 500)

class Ball(Widget):
    pass

class ShrinkThisApp(App):
    def build(self):
        return ShrinkThis()

if __name__ == '__main__':
    ShrinkThisApp().run()