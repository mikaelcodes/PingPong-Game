import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(40,-20)
        self.dx = 2
        self.dy = 2
    
    def move(self):
        x_positon = self.xcor() + self.dx
        y_position = self.ycor() + self.dy
        self.goto(x_positon, y_position)
        
        if self.xcor() > 380 or self.xcor() < -380:
            self.dx *= -1
        
        if self.ycor() > 380 or self.ycor() < -380:
            self.dy *= -1

if __name__ == '__main__':
    ball = Ball()
    while True:
        ball.move()
        
    


    
       