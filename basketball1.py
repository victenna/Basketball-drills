import turtle
import time
import math,random

#turtle.tracer(2)
t1=turtle.Turtle()
wn=turtle.Screen()
wn.setup(1000,900)
wn.bgcolor('light blue')

# box around a player
t5=turtle.Turtle()
t5.up()
t5.pensize(15)
t5.goto(-450,-318)
t5.down()
#t5.color('blue')
t5.goto(200,-318)

#player image
image1='player.gif'
wn.addshape(image1)
t1.shape(image1)
t1.up()
t1.goto(-350,-200)

#ball image
t2=turtle.Turtle()
image2='ball.gif'
wn.addshape(image2)
t2.shape(image2)
t2.up()
t2.pencolor('blue')
t2.goto(-325,-77)
#t2.showturtle()
t1.speed(0)
t2.speed(0)   
#basket image
t3=turtle.Turtle()
image3='basket.gif'
wn.addshape(image3)
t3.shape(image3)
t3.up()
t3.goto(320,220)

#vector image
t6=turtle.Turtle()
image6='vector.gif'
wn.addshape(image6)
t6.shape(image6)
t6.up()
t6.goto(-160,-400)

# reflecting plate psition
t4=turtle.Turtle('square')
t4.shapesize(0.3,6.5)
t4.color('red')
t4.up()
t4.goto(355,305)
t4.setheading(-65)

#Total Numbers of Drills
Text_Font=('Arial',20,'bold')
Text_Font1=('Arial',25,'bold')

t7=turtle.Turtle()
t7.hideturtle()
t7.color('blue')
t7.up()
t7.goto(-250,330)
t7.write('Total Number of Drills 10',font=Text_Font1)

# Score
score=turtle.Turtle()
score.hideturtle()
score.up()
score.color('blue')

def scr():
    score.goto(150,-100)
    score.clear()
    score.write('Score=',font=Text_Font)
    score.goto(250,-100)
    score.write(s,font=Text_Font)
s=0           
scr()


pi=math.pi
g=9.81
delta=0.15

for q in range (1):
    K1=0
    time.sleep(0.01)
    t2.showturtle()
    t=0
    #eps=0
    eps=50*q
    t1.goto(-350+eps,-200)
    t2.goto(-325+eps,-77)
    
    Vo=float(wn.textinput('Basketball Shooting Drills','Enter initial velocity Vo'))
    theta=float(wn.textinput('Basketball Shooting Drills','Enter angle theta'))
        
    Vox=Vo*math.cos(pi*theta/180)
    Voy=Vo*math.sin(pi*theta/180)
    t2.setheading(theta)
    D=400
    A=t2.xcor()
    for i in range (200):
        
        if t2.xcor()>230 and abs(t2.ycor())>370:
            s=s-1
            scr()
            break
        
        A=abs(230-t2.xcor())
        if A<10 and t2.ycor()<260 and t2.ycor()>0:
            s=s-1
            scr()
            break
        
#---------------------
        if t2.xcor()>220 and abs(t2.ycor()-160)<5:
            s=s+1
            scr()
            break
     
        if D>45:
            i1=i
            X=Vox*t
            Y=Voy*t-g*t*t/2
            time.sleep(0.01)
            t=t+delta
            DX=t2.xcor()-t3.xcor()
            DY=t2.ycor()-(t3.ycor()+90)
            D=int(math.sqrt(DX*DX+DY*DY))
            t2.setposition(X-325+eps,Y-77)
                       
        if D<=45:
            K1=K1+1
            time.sleep(0.01)
            t=t+3*delta
            t2.setheading(-90)
            t2.fd(t)
            if K1==30:
                s=s+1
                scr()
                break


#-----------------------------------
def t_exitonclick():
    
    wn.exitonclick()
t_exitonclick()

#-----------------------------
"""
def h_quit():
    wn.bye()
    
wn.onkey(h_quit, "q")
wn.listen()
"""
