# http://kivy.readthedocs.io/en/master/tutorials/pong.html
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

Builder.load_string('''
<PongBall>:
    size: 50, 50
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size          

<PongPaddle>:
    size: 15, 50
    canvas:
        Color:
            rgba: 1, 1, 1, 0
        Rectangle:
            pos:self.pos
            size:self.size

<PongGame>:
    ball: pong_ball
    player1: player_left
    player2: player_right
 
    PongBall:
        id: pong_ball
        center: self.parent.center
        
    PongPaddle:
        id: player_left
        x: root.x
        center_y: root.center_y
        
    PongPaddle:
        id: player_right
        x: root.width-self.width
        center_y: root.center_y

''')


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.025
            ball.velocity = vel.x, vel.y # + offset

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        #self.pos = (200,100)

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(0, 0)):
        self.ball.velocity = [8,0] #vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()