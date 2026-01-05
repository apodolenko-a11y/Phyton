#harjutus 07
import turtle
t=turtle.Turtle()
t.speed(5)

def draw_rectangle():
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(300)
    t.right(90)
    
for i in range(8):
    draw_rectangle()
    
turtle.done()