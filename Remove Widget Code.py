# https://stackoverflow.com/questions/38973030/need-advice-remove-widget-for-kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyBox(BoxLayout):

    def __init__(self,**kwargs):
        super(MyBox,self).__init__(**kwargs)
        self.orientation = "vertical"

        self.count = 0

        self.controlbuttons = BoxLayout(orientation="horizontal")

        self.controlbuttons.add_widget(Button(on_press=self.add_button,text="Add Button"))
        self.controlbuttons.add_widget(Button(on_press=self.remove_button,text="Remove Button"))

        self.buttons = BoxLayout(orientation="vertical")

        self.add_widget(self.controlbuttons)
        self.add_widget(self.buttons)

    def add_button(self,*args):
        self.count += 1
        self.buttons.add_widget(Button(text=str(self.count)))

    def remove_button(self,*args):
        if len(self.buttons.children):
            self.count -= 1
            self.buttons.remove_widget(self.buttons.children[0])


class MyApp(App):
    def build(self):
        return MyBox()


if __name__ == "__main__":
    MyApp().run()