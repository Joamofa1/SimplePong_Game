import turtle
win=turtle.Screen()
win.title("Pong Game ")
win.bgcolor("blue")
win.setup(width=800,height=600)
win.tracer(0)  #Stops the window from updating.Speeds up game

#Stick A
stick_a=turtle.Turtle()
stick_a.speed(0) # Speed of animation set to maximum possible speed
stick_a.shape("square")
stick_a.color("white")
stick_a.penup() # Not draw a line when moving
stick_a.shapesize(stretch_wid=5,stretch_len=1)
stick_a.goto(-370,0)

#Stick B
stick_b=turtle.Turtle()
stick_b.speed(0) # Speed of animation set to maximum possible speed
stick_b.shape("square")
stick_b.color("white")
stick_b.penup() # Not draw a line when moving
stick_b.shapesize(stretch_wid=5,stretch_len=1)
stick_b.goto(370,0)

#Ball
ball=turtle.Turtle()
ball.speed(0) # Speed of animation set to maximum possible speed
ball.shape("circle")
ball.color("white")
ball.penup() # Not draw a line when moving
ball.goto(0,0)

#Functions
def up_a():
    y=stick_a.ycor()
    y=+20
    stick_a.sety(y)
#keyborad binding
win.listen()
win.onkeypress(up_a,"w")

def down_a():
    y=stick_a.ycor()
    y=-20
    stick_a.sety(y)

win.listen()
win.onkeypress(down_a,"s")

def up_b():
    y=stick_b.ycor()
    y=+20
    stick_b.sety(y)
#keyborad binding
win.listen()
win.onkeypress(up_b,"i")

def down_b():
    y=stick_b.ycor()
    y=-20
    stick_b.sety(y)

win.listen()
win.onkeypress(down_b,"k")

#Main game loop
while True:
    win.update()