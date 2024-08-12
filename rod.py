import turtle

class Rod(turtle.Turtle):
    def __init__(self,x):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(5,1)
        self.fillcolor('brown')
        self.goto(x,0)
    
    
    


if __name__ == '__main__':
    rod = Rod(400)
    rod2 = Rod(-400)
    turtle.mainloop()
    
    
        
