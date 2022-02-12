#this is a program to make a traffic light
#by: Zeki

#importing the lib
import turtle
mypen = turtle.Turtle()
mypen.penup()
mypen.forward(100)
mypen.down()
mypen.speed(70)

#start of the base
mypen.color("gold1")
mypen.right(90)
mypen.left(180)
mypen.forward(500)
mypen.left(90)
mypen.forward(250)
mypen.left(90)
mypen.forward(500)
mypen.left(90)
mypen.forward(250)
mypen.begin_fill()
for i in range(1):
    mypen.right(90)
    mypen.left(180)
    mypen.forward(500)
    mypen.left(90)
    mypen.forward(250)
    mypen.left(90)
    mypen.forward(500)
    mypen.left(90)
    mypen.forward(250)
mypen.end_fill()

mypen.penup()
mypen.goto(-25,385)
mypen.down()
mypen.color("black")
mypen.circle(55)
mypen.begin_fill()
for i in range (1):
    mypen.circle(55)
mypen.end_fill()

mypen.penup()
mypen.goto(-25,385)
mypen.down()
mypen.color("green")
mypen.circle(50)
mypen.begin_fill()
for i in range(1):
    mypen.circle(50)
mypen.end_fill()

mypen.penup()
mypen.goto(-25,215)
mypen.down()
mypen.color("black")
mypen.circle(55)
mypen.begin_fill()
for i in range (1):
    mypen.circle(55)
mypen.end_fill()

mypen.penup()
mypen.goto(-25,215)
mypen.down()
mypen.color("yellow")
mypen.circle(50)
mypen.begin_fill()
for i in range(1):
    mypen.circle(50)
mypen.end_fill()

mypen.penup()
mypen.goto(-25,65)
mypen.down()
mypen.color("black")
mypen.circle(55)
mypen.begin_fill()
for i in range (1):
    mypen.circle(55)
mypen.end_fill()

mypen.penup()
mypen.goto(-25,65)
mypen.down()
mypen.color("red")
mypen.circle(50)
mypen.begin_fill()
for i in range(1):
    mypen.circle(50)
mypen.end_fill()
