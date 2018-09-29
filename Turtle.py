# https://cs.nyu.edu/courses/spring13/CSCI-UA.0002-007/CSCI_UA-02_Day21.pdf

import turtle


def colorNode(currentLocation):

    if currentLocation == 1:
        # change color of triangle 1
        rowOneTriangles.penup()
        rowOneTriangles.goto(-175, 215)
        rowOneTriangles.left(60)
        # rowOneTriangles.forward(250)
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

    if 2 <= currentLocation <= 3:
        print(2)
    if 4 <= currentLocation <= 6:
        print(3)
    if 7 <= currentLocation <= 10:
        print(4)
    if 11 <= currentLocation <= 15:
        print(5)
    if 16 <= currentLocation <= 21:
        print(6)


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
'''

# change color of triangle 1
rowOneTriangles.penup()
rowOneTriangles.goto(-175, 215)
rowOneTriangles.left(60)
# rowOneTriangles.forward(250)
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

# level 2
rowTwoTriangles.penup()
rowTwoTriangles.goto(-200, 173)
rowTwoTriangles.left(60)
# rowOneTriangles.forward(250)
rowTwoTriangles.fillcolor('blue')
rowTwoTriangles.begin_fill()
rowTwoTriangles.pendown()
rowTwoTriangles.right(60)
rowTwoTriangles.forward(50)
rowTwoTriangles.left(120)
rowTwoTriangles.forward(50)
rowTwoTriangles.left(120)
rowTwoTriangles.forward(50)
rowTwoTriangles.end_fill()

# level 3
rowThreeTriangles.penup()
rowThreeTriangles.goto(-225, 129)
rowThreeTriangles.left(60)
# rowOneTriangles.forward(250)
rowThreeTriangles.fillcolor('blue')
rowThreeTriangles.begin_fill()
rowThreeTriangles.pendown()
rowThreeTriangles.right(60)
rowThreeTriangles.forward(50)
rowThreeTriangles.left(120)
rowThreeTriangles.forward(50)
rowThreeTriangles.left(120)
rowThreeTriangles.forward(50)
rowThreeTriangles.end_fill()

# level 4
rowFourTriangles.penup()
rowFourTriangles.goto(-250, 88)
rowFourTriangles.left(60)
# rowOneTriangles.forward(250)
rowFourTriangles.fillcolor('blue')
rowFourTriangles.begin_fill()
rowFourTriangles.pendown()
rowFourTriangles.right(60)
rowFourTriangles.forward(50)
rowFourTriangles.left(120)
rowFourTriangles.forward(50)
rowFourTriangles.left(120)
rowFourTriangles.forward(50)
rowFourTriangles.end_fill()

# level 5
rowFiveTriangles.penup()
rowFiveTriangles.goto(-275, 44)
rowFiveTriangles.left(60)
# rowOneTriangles.forward(250)
rowFiveTriangles.fillcolor('blue')
rowFiveTriangles.begin_fill()
rowFiveTriangles.pendown()
rowFiveTriangles.right(60)
rowFiveTriangles.forward(50)
rowFiveTriangles.left(120)
rowFiveTriangles.forward(50)
rowFiveTriangles.left(120)
rowFiveTriangles.forward(50)
rowFiveTriangles.end_fill()

# level 6
rowSixTriangles.penup()
rowSixTriangles.goto(-300, 0)
rowSixTriangles.left(60)
# rowOneTriangles.forward(250)
rowSixTriangles.fillcolor('blue')
rowSixTriangles.begin_fill()
rowSixTriangles.pendown()
rowSixTriangles.right(60)
rowSixTriangles.forward(50)
rowSixTriangles.left(120)
rowSixTriangles.forward(50)
rowSixTriangles.left(120)
rowSixTriangles.forward(50)
rowSixTriangles.end_fill()


# starting position for level 1 (-175, 215)
# starting position for level 2 (-200, 173)
# starting position for level 3 (-225, 129)
# starting position for level 4 (-250, 88)
# starting position for level 5 (-275, 44)
# starting position for level 5 (-300, 0)


'''
currentLocation = 1
colorNode(currentLocation)


turtle.done()
