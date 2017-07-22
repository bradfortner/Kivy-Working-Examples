# From https://gist.github.com/Zen-CODE/8423383
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

Builder.load_string("""
<Test>:
    hideable: hideable
    Widget:
        canvas:
            Color:
                rgba: 1, 0, 0, 0.5
            Rectangle:
                pos: self.pos
                size: self.size
        id: movable
    Widget:
        id: hideable
        canvas:
            Color:
                rgba: 0, 1, 0, 0.5
            Rectangle:
                pos: self.pos
                size: self.size
        pos: movable.pos
""")


class Test(Widget):
    def my_remove_widget(self):
        print "self.hideable=", self.hideable
        self.remove_widget(self.hideable)
        Clock.schedule_once(lambda dt: self.show_widget(), 1)

    def show_widget(self):
        print "self.hideable=", self.hideable
        self.add_widget(self.hideable)
        Clock.schedule_once(lambda dt: self.my_remove_widget(), 1)


class FunApp(App):
    def build(self):
        test = Test()
        Clock.schedule_once(lambda dt: test.my_remove_widget(), 1)
        return test

FunApp().run()