# Author MRS 

import turtle

class Builder:
    def__init__(self):
    builder = turtle.Turtle()
    self.builder.speed(0)
    self.builder.penup()
    self.builder.hideturtle()

    def build_part(self, color, sides, angle):
        self.builder.color(color)
        self.builder.begin_fill()
        if len(sides) != 0:
            for side in sides:
            self.builder.forward(side)
            self.builder.right(angle)
        else:
            self.builder.circle(angle)
            self.builder.end_fill()
    
    def build_body(self):
        self.builder.goto(50, 50)
        rocket.build_part('red', [200, 100, 200, 100], 90)

window = turtle.Screen()
rocket = Builder()

rocket.build_part('red', [200, 100, 200, 100], 90)
rocket.build_part('blue', [], 200)

window.mainloop()