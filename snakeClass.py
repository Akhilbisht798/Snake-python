import turtle as t
STARTING_POS = [(0,0),(-20,0),(-40,0)]
SPEED = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        

    def create_snake(self):
        for positon in STARTING_POS:
            self.add_segment(positon)
            

    def add_segment(self,positon):
        tim = t.Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(positon)
        self.segments.append(tim)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        

    def move(self):
        for i in range(len(self.segments)-1 ,0,-1):
            nx = self.segments[i-1].xcor()
            ny = self.segments[i-1].ycor()
            self.segments[i].goto(nx,ny)
        self.segments[0].forward(SPEED)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
