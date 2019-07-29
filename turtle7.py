import turtle
turtle.goto(0,0)
turtle.direction=None

def up():
    
    print("you pressed the up key")
    x,y=turtle.pos()
    turtle.goto(x,y+100)
turtle.onkey(up,"Up")
turtle.listen()
def left():
    
    print("you pressed the left key")
    x,y=turtle.pos()
    turtle.goto(x-100,y)
turtle.onkey(left,"Left")
turtle.listen()
def right():
    
    print("you pressed the right key")
    x,y=turtle.pos()
    turtle.goto(x+100,y)
turtle.onkey(right,"Right")
turtle.listen()
def down():
    
    print("you pressed the down key")
    x,y=turtle.pos()
    turtle.goto(x,y-100)
turtle.onkey(down,"Down")
turtle.listen()
def space():
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()
turtle.onkey(space,"space")
turtle.listen()
turtle.mainloop()
