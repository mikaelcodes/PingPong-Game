import turtle 
from rod import Rod 
from moving_ball import Ball

screen = turtle.Screen()
screen.setup(800,800)
screen.bgcolor('lightgreen')



rod1 = Rod(-400)
rod2 = Rod(400)


def left_rod_up():
    parint()


turtle.listen()




ball = Ball()

while True: 
    ball.move()


turtle.done()
