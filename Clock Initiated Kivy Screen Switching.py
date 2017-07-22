# Modified from https://bradfortner.wordpress.com/2016/12/30/kivy-for-the-non-computer-scientist-part-12-kv-language-switching-between-kivy-gui-screens/

import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<WelcomeScreen>:
    GridLayout:
        cols: 1
        Label:
            text: "You're On The Welcome Screen. Please Select Which Screen You Want To Go To"
        Button:
            text: 'Switch To Screen One' #  Sets above button text property
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'
        Button:
            text: 'Switch To Screen Two'
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_two'
        Button:
            text: 'Switch To Screen Three'
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_three'
<FirstScreen>:
    GridLayout:
        cols: 1 # Sets column property to 1.
        Button: # Creates a Button Widget instance.
            text: "You're On Screen One. Press To Return To Welcome Screen"
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'welcome_screen'
<SecondScreen>:
    GridLayout:
        cols: 1
        Button:
            text: "You're On Screen Two. Press To Return To Welcome Screen"
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'welcome_screen'
<ThirdScreen>:
    GridLayout:
        cols: 1
        Button:
            text: "You're On Screen Three. Press To Return To Welcome Screen"
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'welcome_screen'
""")

class WelcomeScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

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