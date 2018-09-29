# https://cs.nyu.edu/courses/spring13/CSCI-UA.0002-007/CSCI_UA-02_Day21.pdf

import turtle

background = turtle.Turtle()


background.speed(0)

background.fillcolor('black')
background.begin_fill()
background.penup
background.goto(-300, 0)
background.pendown
background.forward(300)
background.left(120)
background.forward(300)
background.left(120)
background.forward(300)
background.end_fill()

rowSixTriangles = turtle.Turtle()
rowSixTriangles.speed(0)

rowSixTriangles.fillcolor('white')
rowSixTriangles.begin_fill()
rowSixTriangles.penup
rowSixTriangles.goto(-300, 0)
rowSixTriangles.pendown

for x in range(1, 7):
    rowSixTriangles.forward(50)
    rowSixTriangles.left(120)
    rowSixTriangles.forward(50)
    rowSixTriangles.left(120)
    rowSixTriangles.penup()
    rowSixTriangles.forward(50)
    rowSixTriangles.left(120)
    rowSixTriangles.forward(50)
    rowSixTriangles.pendown()


rowSixTriangles.end_fill()
rowSixTriangles.penup()

rowFiveTriangles = turtle.Turtle()
rowFiveTriangles.speed(0)
rowFiveTriangles.fillcolor('white')
rowFiveTriangles.penup()
rowFiveTriangles.goto(-300, 0)
rowFiveTriangles.left(60)
rowFiveTriangles.forward(50)
rowFiveTriangles.right(60)
rowFiveTriangles.pendown()
rowFiveTriangles.begin_fill()

for x in range(1, 6):
    rowFiveTriangles.forward(50)
    rowFiveTriangles.left(120)
    rowFiveTriangles.forward(50)
    rowFiveTriangles.left(120)
    rowFiveTriangles.penup()
    rowFiveTriangles.forward(50)
    rowFiveTriangles.left(120)
    rowFiveTriangles.forward(50)
    rowFiveTriangles.pendown()

rowFiveTriangles.end_fill()


rowFourTriangles = turtle.Turtle()
rowFourTriangles.speed(0)
rowFourTriangles.fillcolor('white')
rowFourTriangles.penup()
rowFourTriangles.goto(-300, 0)
rowFourTriangles.left(60)
rowFourTriangles.forward(100)
rowFourTriangles.right(60)
rowFourTriangles.pendown()
rowFourTriangles.begin_fill()

for x in range(1,5):
    rowFourTriangles.forward(50)
    rowFourTriangles.left(120)
    rowFourTriangles.forward(50)
    rowFourTriangles.left(120)
    rowFourTriangles.penup()
    rowFourTriangles.forward(50)
    rowFourTriangles.left(120)
    rowFourTriangles.forward(50)
    rowFourTriangles.pendown()

rowFourTriangles.end_fill()

rowThreeTriangles = turtle.Turtle()
rowThreeTriangles.speed(0)
rowThreeTriangles.fillcolor('white')
rowThreeTriangles.penup()
rowThreeTriangles.goto(-300, 0)
rowThreeTriangles.left(60)
rowThreeTriangles.forward(150)
rowThreeTriangles.right(60)
rowThreeTriangles.pendown()
rowThreeTriangles.begin_fill()

for x in range(1, 4):
    rowThreeTriangles.forward(50)
    rowThreeTriangles.left(120)
    rowThreeTriangles.forward(50)
    rowThreeTriangles.left(120)
    rowThreeTriangles.penup()
    rowThreeTriangles.forward(50)
    rowThreeTriangles.left(120)
    rowThreeTriangles.forward(50)
    rowThreeTriangles.pendown()

rowThreeTriangles.end_fill()

rowTwoTriangles = turtle.Turtle()
rowTwoTriangles.speed(0)
rowTwoTriangles.fillcolor('white')
rowTwoTriangles.penup()
rowTwoTriangles.goto(-300, 0)
rowTwoTriangles.left(60)
rowTwoTriangles.forward(200)
rowTwoTriangles.right(60)
rowTwoTriangles.pendown()
rowTwoTriangles.begin_fill()

for x in range(1, 3):
    rowTwoTriangles.forward(50)
    rowTwoTriangles.left(120)
    rowTwoTriangles.forward(50)
    rowTwoTriangles.left(120)
    rowTwoTriangles.penup()
    rowTwoTriangles.forward(50)
    rowTwoTriangles.left(120)
    rowTwoTriangles.forward(50)
    rowTwoTriangles.pendown()

rowTwoTriangles.end_fill()

rowOneTriangles = turtle.Turtle()
rowOneTriangles.speed(0)
rowOneTriangles.fillcolor('white')
rowOneTriangles.penup()
rowOneTriangles.goto(-300, 0)
rowOneTriangles.left(60)
rowOneTriangles.forward(250)
rowOneTriangles.right(60)
rowOneTriangles.pendown()
rowOneTriangles.begin_fill()

for x in range(1, 2):
    rowOneTriangles.forward(50)
    rowOneTriangles.left(120)
    rowOneTriangles.forward(50)
    rowOneTriangles.left(120)
    rowOneTriangles.penup()
    rowOneTriangles.forward(50)
    rowOneTriangles.left(120)
    rowOneTriangles.forward(50)
    rowOneTriangles.pendown()

rowOneTriangles.end_fill()


# change color of triangle 1
rowOneTriangles.penup()
rowOneTriangles.goto(-300, 0)
rowOneTriangles.left(60)
rowOneTriangles.forward(250)
rowOneTriangles.fillcolor('blue')
rowOneTriangles.begin_fill()
rowOneTriangles.pendown()
rowOneTriangles.right(60)
rowOneTriangles.forward(50)
rowOneTriangles.left(120)
rowOneTriangles.forward(50)
rowOneTriangles.left(120)
rowOneTriangles.forward(50)
rowOneTriangles.end_fill()

turtle.done()
