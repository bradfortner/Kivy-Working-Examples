# Modified from https://bradfortner.wordpress.com/2016/12/30/kivy-for-the-non-computer-scientist-part-12-kv-language-switching-between-kivy-gui-screens/

import kivy
kivy.require('1.9.1')
from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty

Builder.load_string("""
<WelcomeScreen>:
    GridLayout:
        cols: 1
        Label:
            text: "You're On The Welcome Screen. Please Select Which Screen You Want To Go To"
        Button:
            text: 'One Way Switch To Startup Screen' #  Sets above button text property
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'
        Button:
            text: 'One Way Switch To Rotating 45RPM Screen'
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_two'
        Button:
            text: 'One Way Switch To Rotating Logo Screen'
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_three'
<FirstScreen>:
    FloatLayout:
        canvas.before:
            BorderImage:
                source: 'retro.jpg'
                pos: self.pos
                size: self.size
            PushMatrix
            Rotate:
                angle: root.angle
                axis: 0, 0, 1
                origin: root.center
        canvas.after:
            PopMatrix
        Image:
            source: 'convergence_logo.png'
            size_hint: None, None
            size: 500, 500
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    FloatLayout:
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
<SecondScreen>:
    FloatLayout:
        canvas.before:
            BorderImage:
                source: 'background.png'
                pos: self.pos
                size: self.size
            PushMatrix
            Rotate:
                angle: root.angle
                axis: 0, 0, 1
                origin: root.center
        canvas.after:
            PopMatrix
        Image:
            source: 'new.png'
            size_hint: None, None
            size: 600, 600
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
<ThirdScreen>:
    FloatLayout:
        canvas.before:
            BorderImage:
                source: 'background.png'
                pos: self.pos
                size: self.size
            PushMatrix
            Rotate:
                angle: root.angle
                axis: 0, 0, 1
                origin: root.center
        canvas.after:
            PopMatrix
        Image:
            source: 'convergence_logo.png'
            size_hint: None, None
            size: 600, 600
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
""")

class WelcomeScreen(Screen):
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        anim = Animation(angle=360, duration=2)
        anim += Animation(angle=360, duration=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

class FirstScreen(Screen):
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        anim = Animation(angle=360, duration=2)
        anim += Animation(angle=360, duration=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

class SecondScreen(Screen):
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        anim = Animation(angle=360, duration=2)
        anim += Animation(angle=360, duration=-2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

class ThirdScreen(Screen):
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)
        anim = Animation(angle=360, duration=2)
        anim += Animation(angle=360, duration=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome_screen'))
sm.add_widget(FirstScreen(name='screen_one'))
sm.add_widget(SecondScreen(name='screen_two'))
sm.add_widget(ThirdScreen(name='screen_three'))

class SwitchingScreenApp(App):

    def build(self):
        Clock.schedule_once(self.screen_switch_one, 2)
        Clock.schedule_once(self.screen_switch_two, 4)
        Clock.schedule_once(self.screen_switch_three, 6)
        Clock.schedule_once(self.screen_switch_welcome, 8)
        return sm

    def screen_switch_one(a,b):
        sm.current = 'screen_one'
    def screen_switch_two(a,b):
        sm.current = 'screen_two'
    def screen_switch_three(a,b):
        sm.current = 'screen_three'
    def screen_switch_welcome(a,b):
        sm.current = 'welcome_screen'

SwitchingScreenApp().run()