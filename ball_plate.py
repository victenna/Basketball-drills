import turtle
import time
import math

wn = turtle.Screen()
wn.setup(1000, 900)
wn.bgcolor("light blue")

# Angle Game
t0 = turtle.Turtle()
image0 = "angle_game.gif"
wn.addshape(image0)
t0.shape(image0)
t0.up()
t0.goto(200, -300)

# player image
t1 = turtle.Turtle()
image1 = "player.gif"
wn.addshape(image1)
t1.shape(image1)
t1.up()
t1.goto(-350, -200)

# ball image
t2 = turtle.Turtle()
image2 = "ball.gif"
wn.addshape(image2)
t2.shape(image2)
t2.up()
t2.pencolor("blue")
t2.goto(-325, -77)
# t2.showturtle()

# ball trace
t3 = turtle.Turtle()
t3.up()
t3.pencolor("blue")
t3.pensize(4)
t3.goto(-325, -77)
t3.hideturtle()

# reflecting plate position
t4 = turtle.Turtle("square")
t4.shapesize(0.6, 1.5)
t4.color("red")
t4.up()
t4.goto(345, 285)
t4.setheading(-45)
t4.showturtle()
# vector image
t6 = turtle.Turtle()
image6 = "vector.gif"
wn.addshape(image6)
t6.shape(image6)
t6.up()
t6.goto(-160, -400)

# Name of Game
t7 = turtle.Turtle()
image7 = "angle_game1.gif"
wn.addshape(image7)
t7.shape(image7)
t7.up()
t7.goto(50, 350)

Text_Font = ("Arial", 20, "bold")

# Score
score = turtle.Turtle()
score.hideturtle()
score.up()
score.color("blue")

def scr():
    score.goto(150, -100)
    score.clear()
    score.write("Score=", font=Text_Font)
    score.goto(250, -100)
    score.write(s, font=Text_Font)

s = 0
scr()
pi = math.pi
g = 9.81
delta = 0.55
t1.speed(0)
t2.speed(0)
S = 8
s = 0
eps = 0
Vo = 120
S = 10
for q in range(S + 1):
    if q == S:
        time.sleep(1)
        turtle.bye()
    t3.up()
    t3.clear()

    t2.showturtle()
    t = 0
    t1.goto(-350, -200)
    t2.goto(-325, -77)
    t3.goto(-325, -77)
    t3.down()

    t4.goto(345, 285 - 200 * q / S)
    t4.showturtle()

    theta = float(wn.textinput("Angle Game for Kids", "Enter angle theta"))

    Vox = Vo * math.cos(pi * theta / 180)
    Voy = Vo * math.sin(pi * theta / 180)
    t2.setheading(theta)
    t3.setheading(theta)
    D = 400

    for i in range(150):
        # print (i)

        if D > 30:
            i1 = i
            X = Vox * t
            Y = Voy * t - g * t * t / 2
            time.sleep(0.03)
            t = t + delta
            DX = t2.xcor() - t4.xcor()
            DY = t2.ycor() - t4.ycor()
            D = int(math.sqrt(DX * DX + DY * DY))
            t2.setposition(X - 325, Y - 77)
            t3.setposition(X - 325, Y - 77)
            if t2.xcor() > 445 or t2.ycor() > 410 or t2.ycor() < -316:
                s = s - 1
                scr()
                break

        if D <= 30:
            s = s + 1
            scr()
            t2.hideturtle()
            break
