from kivy.animation import Animation
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout

Builder.load_string('''                               
<Loading>:
    # Describe the record's position and size here
    size_hint: None, None
    size: 160, 160
    pos_hint: {'top': .895, 'right': .605}
    canvas.before:
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
        size: self.parent.size # So we don't have to change it every time, change the size above only
        pos_hint: {'center_x': .5, 'center_y': .5}
<MyBackgroundImage>
    Image:
        source: 'new_jukebox.png'
        
''')

class Loading(FloatLayout):
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Loading, self).__init__(**kwargs)
        anim = Animation(angle=360, duration=2)
        anim += Animation(angle=360, duration=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

class MyBackgroundImage(FloatLayout):
    pass

class RotationAnimation(App):
    def build(self):
        f = FloatLayout()  # The new main widget
        f.add_widget(MyBackgroundImage())
        f.add_widget(Loading())  # Add the loading record to it
        return f

RotationAnimation().run()