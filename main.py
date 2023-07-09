import turtle
import time
import random
#Game_board
Screen = turtle.Screen()
Screen.bgcolor("white")
Screen.title("Catch The Turtle")
#time turtle
turtlew = turtle.Turtle()
turtlew.hideturtle()
turtlew.penup()
turtlew.setposition(-25,240)
turtlew.pendown()
#score turtle
turtles = turtle.Turtle()
turtles.hideturtle()
turtles.penup()
turtles.setposition(-25,220)
turtles.pendown()

#turtle for click

myTurtle = turtle.Turtle()
myTurtle.color("Green","Green")
myTurtle.shape("turtle")
myTurtle.shapesize(3/2)
myTurtle.left(90)
myTurtle.penup()
turtleList=[]
score = 0
def location_turtle():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turtleList.append([x,y])
    myTurtle.hideturtle()
    myTurtle.setposition(x,y)
    myTurtle.showturtle()




def count(t):
    while t > 0 :
        turtlew.write(f"Time : {t}",font=("calibri",15,"normal"))
        time.sleep(0.4)
        turtlew.clear()
        location_turtle()
        time.sleep(0.4)
        t = t - 1
    else:
        turtlew.write("Game over!",font=("calibri", 15, "normal"))

def get_score(x,y):
    global score
    turtles.clear()
    score += 1
    turtles.write(f"Score : {score}", font=("calibri", 15, "normal"))


myTurtle.onclick(get_score)
count(30)
Screen.mainloop()
