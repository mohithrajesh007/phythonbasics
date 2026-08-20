import turtle
mohith=turtle.Turtle()
screen = turtle.Screen()
screen.listen()
def moveup():
    mohith.left(90)
    mohith.forward(50)
    mohith.right(90)

def moveleft():
    mohith.left(180)
    mohith.forward(50)
    mohith.right(180)

def moveright():
    mohith.forward(50)

def movedown():
    mohith.right(90)
    mohith.forward(50)
    mohith.left(90)

screen.onkey(moveup,"Up")
screen.onkey(movedown,"Down")
screen.onkey(moveleft,"Left")
screen.onkey(moveright,"Right")

turtle.done()