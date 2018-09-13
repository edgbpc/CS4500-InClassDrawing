import turtle
import time
import random

for i in range(1, 80):
    turtle.forward(i)
    turnangle = random.randint(10, 45+1)
    turtle.right(turnangle)
    randRed = str(random.randint(0, 256))
    randBlue = random.randint(0, 256)
    randGreen = random.randint(0, 256)


    str(randRed)
    str(randBlue)
    str(randGreen)


    turtle.color(randRed)

#turtle.forward(50)
#turtle.right(5)
#urtle.forward(50)
#turtle.split("p")
time.sleep(5)
