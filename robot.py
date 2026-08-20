import turtle
my_turtle=turtle.Turtle()
#user_input=input("The gandi ji robot is sad,happy or hungry")
user_input=("The gandi ji robot is sad")
my_turtle.shape("arrow")
my_turtle.color("red")
my_turtle.speed(1000000000000)

my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)

my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)

my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(40)
my_turtle.right(90)
my_turtle.forward(20)
my_turtle.circle(15)

my_turtle.forward(45)
my_turtle.circle(15)
my_turtle.forward(35)
my_turtle.right(90)
my_turtle.forward(40)

my_turtle.right(90)
my_turtle.forward(40)
my_turtle.right(90)
if user_input == "The gandi ji robot is hungry":
    my_turtle.forward(11)
    my_turtle.circle(20)

elif user_input == "The gandi ji robot is sad":
    my_turtle.forward(10)
    my_turtle.circle(20,180)

elif user_input =="The gandi ji robot is happy":
    my_turtle.forward(10)
    my_turtle.circle(20,-180)

else :
    my_turtle.forward(10)
    my_turtle.left(90)
    my_turtle.forward(30)
    my_turtle.right(180)
    my_turtle.forward(50)

turtle.done()