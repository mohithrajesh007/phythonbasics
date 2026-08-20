import turtle
import random

TotalScore =0

mohith = turtle.Screen()
mohith.title("FallingStars")
mohith.listen()
basket = turtle.Turtle()
star = turtle.Turtle()
levelTracker = turtle.Turtle()
mohith.setup(width=700,height=700)

basket.shape("square")
star.shape("arrow")
basket.shapesize(stretch_wid=1,stretch_len=5)
mohith.bgcolor("black")
basket.color("green")
star.color("yellow")
star.penup()
basket.penup()

def level_tracking():
    if star.distance(basket) < 50:

        levelTracker.color("blue")
    levelTracker.shape("square")
    levelTracker.penup()
    levelTracker.hideturtle()
    levelTracker.goto(-325,325)

def positions():
    star.goto(+250,325)
    basket.goto(0,-250)

def screenstarting():

    basket.forward(30)
    basket.showturtle()
    star.showturtle()
    mohith.bgcolor("white")
    basket.hideturtle()
    star.hideturtle()
    basket.pencolor("black")
    basket.goto(-345,250)
    basket.write("controls: up arrow - up",font= 5)
    basket.forward(55)
    basket.right(90)
    basket.forward(20)
    basket.write("Down arrow - down", font=5)
    basket.forward(20)
    basket.write("Left arrow - left", font=5)
    basket.forward(20)
    basket.write("Right arrow - right", font=5)
    basket.forward(20)
    basket.write("Q - restart", font=5)
    basket.forward(20)
    basket.write("M - drawing", font=5)
    basket.forward(20)
    basket.write("N - no drawing", font=5)
    basket.forward(20)
    basket.write("1 - pause", font=5)
    basket.forward(20)
    basket.write("2 - resume", font=5)
    basket.forward(20)
    basket.write("0 - exit", font=5)
    basket.goto(-100, 250)
    basket.write("Rules:", font=5)
    basket.forward(30)
    basket.write("if you don't collect the star which is falling down you will lose one of your life", font=5)
    basket.forward(30)
    basket.write("1.Move the basket where ever the stars are falling to get points.", font=5)
    basket.forward(30)
    basket.write("3.Use the controls to move around.", font=5)
    basket.forward(30)
    basket.write("Press Q to start", font=5)
    basket.right(90)
    mohith.bgcolor("black")
    star.right(90)
    star.goto(+250,325)
    basket.goto(0,-250)
    basket.showturtle()

def fallingstar():
    exitflag = "false"
    while "false":
        star.hideturtle()
        x = random.randint(-325, +325)
        star.goto(x, 325)
        star.showturtle()
        star.ycor()
        star.speed(1)
        star.forward(500)
        exitflag = "true"

def pausethegame():
    basket.pencolor("green")
    basket.write("The game is paused")
    stop_controls1()

def resumethegame():
    basket.clear()
    controls()

def restartthegame():
    score = 0
    lives = 3
    levelTracker.clear()
    star.clear()
    levelTracker.showturtle()
    star.showturtle()

def wrapfunction():
    if basket.xcor() > 325:
        basket.goto(-325, -250)
    if basket.xcor() < -325:
        basket.goto(325, -250)
    if basket.ycor() > 325:
        basket.goto(0, -325)
    if basket.ycor() < -325:
        basket.goto(0, 325)


def moveleft():
    basket.forward(30)
    wrapfunction()
    mohith.listen()

def moveright():
    basket.backward(30)
    wrapfunction()
    mohith.listen()

def pendownbasket():
    basket.pendown()

def clear():
    basket.clear()

def exit():
    mohith.bye()

def pen_up():
    basket.penup()
    star.penup()
    wrapfunction()

def stop_controls1():
    mohith.onkey(None, "Down")
    mohith.onkey(None, "Left")
    mohith.onkey(None, "Right")
    mohith.onkey(None, "Up")
    mohith.onkey(None, "n")
    mohith.onkey(None, "m")
    wrapfunction()

def stop_controls2():
    mohith.onkey(None, "Left")
    mohith.onkey(None, "Right")
    mohith.onkey(None, "n")
    mohith.onkey(None, "m")
    mohith.onkey(None, "1")
    mohith.onkey(None, "2")
    mohith.onkey(None, "q")
    wrapfunction()

def controls():
    mohith.onkey(moveleft, "Left")
    mohith.onkey(moveright, "Right")
    mohith.onkey(pen_up, "n")
    mohith.onkey(pendownbasket, "m")
    mohith.onkey(pausethegame, "1")
    mohith.onkey(resumethegame, "2")
    mohith.onkey(clear,"r")
    mohith.onkey(restartthegame,"q")
    wrapfunction()

positions()
controls()
screenstarting()
level_tracking()
wrapfunction()
fallingstar()
turtle.done()