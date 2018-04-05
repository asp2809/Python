import turtle
from random import randint
s=turtle.Screen()
s.bgcolor("light green")        #giving the background color of the screen as "light green"
t=turtle.Turtle()               #initializing the track making turtle
t.speed(10)
t.right(90)
t.penup()

for i in range(0,15):           #making the track with track turtle initialized at (-140,100)
    t.goto(-140+(i*20), 100)
    t.write(i)
    
    for x in range(0,11):       #making the dotted path
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)

#Initializing all the turtles and attributes to them
a=turtle.Turtle()               
a.color("red")
a.shape('turtle')
a.penup()
#initializing initial positions of the turtles taking a reference of (-140,100)
a.goto(-140,100-40) 
#loop for rotating the turtle 360 degree           
for i in range(0,4):
    a.right(90)

b=turtle.Turtle()
b.color("green")
b.shape('turtle')
b.penup()
b.goto(-140,100-80)
for i in range(0,4):
    b.right(90)

c=turtle.Turtle()
c.color("yellow")
c.shape('turtle')
c.penup()
c.goto(-140,100-120)
for i in range(0,4):
    c.right(90)

d=turtle.Turtle()
d.color("blue")
d.shape('turtle')
d.penup()
d.goto(-140,100-160)
for i in range(0,4):
    d.right(90)

e=turtle.Turtle()
e.color("violet")
e.shape('turtle')
e.penup()
e.goto(-140,100-200)
for i in range(0,4):
    e.right(90)

a.pendown()
b.pendown()
c.pendown()
d.pendown()
e.pendown()

#race starts here 
#All the turtles move according to the random values giving to them between 1 and 4 which goes on for 90 times
for i in range(90):                 
    a.forward(randint(1,5))
    b.forward(randint(1,5))
    c.forward(randint(1,5))
    d.forward(randint(1,5))
    e.forward(randint(1,5))


s.exitonclick()