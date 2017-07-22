import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
kivy.require("1.9.1")

class MyPopupProgressBar(Widget):

    progress_bar = ObjectProperty() # Kivy properties classes are used when you create an EventDispatcher.
    
    def __init__(self, **kwa):
        super(MyPopupProgressBar, self).__init__(**kwa) #super combines and initializes two widgets Popup and ProgressBar
        self.progress_bar = ProgressBar() # instance of ProgressBar created.
        self.popup = Popup(title='Place Yout Title Here.....', content=self.progress_bar) # progress bar assigned to popup
        self.popup.bind(on_open=self.puopen) # Binds super widget to on_open.
        Clock.schedule_once(self.progress_bar_start) # Uses clock to call progress_bar_start() (callback) one time only

    def progress_bar_start(self, instance): # Provides initial value of of progress bar and lanches popup
        self.progress_bar.value = 1 # Initial value of progress_bar
        self.popup.open() # starts puopen()

    def next(self, dt): # Updates Project Bar
        if self.progress_bar.value >= 100: # Checks to see if progress_bar.value has met 100
            return False # Returning False schedule is canceled and won't repeat
        self.progress_bar.value += 1 # Updates progress_bar's progress

    def puopen(self, instance): # Called from bind.
        Clock.schedule_interval(self.next, .0005) # Creates Clock event scheduling next() every 5-1000th of a second.

class MyApp(App):
    def build(self):
        return MyPopupProgressBar()

if __name__ in ("__main__"):
    MyApp().run()