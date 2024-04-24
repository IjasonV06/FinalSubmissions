import turtle as turtle
import random
myPen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
myPen.shape("arrow")
myPen.pensize(2)
myPen.speed(100)
myPen.color("white")
myPen.up()
myPen.goto(0,310)
myPen.write("Turtle Race!", align='center',  font=("Arial", 20, "normal"))
#Start line
myPen.up()
myPen.goto(-320, 300)
myPen.down()
myPen.goto(-320,-300)
#finish line
myPen.up()
myPen.goto(360,300)
myPen.down()
myPen.goto(360,-300)
myPen.hideturtle()
#Contestants:
Orion = turtle.Turtle()
Orion.speed(100)
Orion.shape('turtle')
Orion.color('green')
Orion.pensize(6)
Orion.penup()
Orion.goto(-320,280)
Orion.down()

Joe = turtle.Turtle()
Joe.speed(100)
Joe.shape('turtle')
Joe.color('brown')
Joe.pensize(4)
Joe.up()
Joe.goto(-320,140)
Joe.down()

Tuffie = turtle.Turtle()
Tuffie.speed(100)
Tuffie.shape('turtle')
Tuffie.color('blue')
Tuffie.pensize(5)
Tuffie.up()
Tuffie.goto(-320,0)
Tuffie.down()

Jason = turtle.Turtle()
Jason.speed(100)
Jason.shape('turtle')
Jason.color('Purple')
Jason.pensize(2)
Jason.up()
Jason.goto(-320,-140)
Jason.down()
#Race loop
while True:
    Orion.forward(random.randint(2,8))
    Joe.forward(random.randint(2,8))
    Tuffie.forward(random.randint(2,8))
    Jason.forward(random.randint(2,8))
    
    if Orion.xcor()>345:
        myPen.up()
        myPen.goto(0,-205)
        myPen.color('yellow')
        myPen.write("ORION WON RIGGED!!!", align = 'center', font=("Arial", 50, "normal"))
        myPen.hideturtle()
        break
    elif Joe.xcor()>345:
        myPen.up()
        myPen.goto(0,-205)
        myPen.color('yellow')
        myPen.write("JOE WON,RIGGED!!!", align = 'center', font=("Arial", 50, "normal"))
        myPen.hideturtle()
        break
    elif Tuffie.xcor()>345:
        myPen.up()
        myPen.goto(0,-205)
        myPen.color('yellow')
        myPen.write("TUFFIE WON,RIGGED!!!", align = 'center', font=("Arial", 50, "normal"))
        myPen.hideturtle()
        break
    elif Jason.xcor()>345:
        Jason.pensize(10)
        myPen.up()
        myPen.goto(0,-205)
        myPen.color('yellow')
        myPen.write("JASON WON,WOOOOOO!!!", align = 'center', font=("Arial", 50, "normal"))
        myPen.hideturtle()
        break
def wintext (Orion):
    Orion.penup()
    Orion.goto(230,22)
    Orion.write("WINNER", align = 'center', font =("Arial", 20, "normal"))
def wintext (Joe):
    Joe.penup()
    Joe.goto(230,22)
    Joe.write("WINNER", align = 'center', font =("Arial", 20, "normal"))