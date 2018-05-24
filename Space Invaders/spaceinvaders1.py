#program for the classic space invader game
import turtle
import os
import math
import random
import winsound

#setting up the screen
screen=turtle.Screen()
screen.screensize()
screen.setup(width = 700, height = 750)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("space_invaders_background.gif")

#register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

border_pen=turtle.Turtle()
border_pen.penup()
border_pen.speed(0)
border_pen.color("white")
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for i in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

#creating the player
player=turtle.Turtle()
player.setheading(90)
player.speed(0)
player.setposition(0, -250)
player.penup()
player.shape('player.gif')

#Initializing the score
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.color("white")
score_pen.setposition(-290,280)
scorestring="Score= %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 12, "bold"))
score_pen.hideturtle()

#creating the enemies
enemies=[]
for i in range(5):
    enemies.append(turtle.Turtle())
    x=random.randint(-200,200)
    y=random.randint(100,200)
    enemies[i].setposition(x, y)
    enemies[i].speed(0)
    enemies[i].penup()
    enemies[i].shape('invader.gif')
    enemyspeed=2

#moving player left and right
playerspeed=15
def move_left():
    x=player.xcor()
    x-=playerspeed
    if x < -280:
        x=-280
    player.setx(x)

def move_right():
    x=player.xcor()
    x+=playerspeed
    if x > 280:
        x=280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        winsound.PlaySound("laser.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False

#making the player's bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.speed(0)
bullet.penup()
bullet.shape("triangle")
bulletspeed=20
bullet.hideturtle()
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.setposition(0,-400)
bulletstate="ready"

#Making the turtle listen the key presses
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemyspeed
        if x > 280 or x < -280:
            enemyspeed*=-1
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
        if enemy.ycor() < -280:
            x1=random.randint(-200,200)
            y1=random.randint(100,200)
            enemy.setposition(x1,y1)
        enemy.setx(x)
        #checking if the bullet hits the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
            bullet.hideturtle()
            bullet.setposition(0,-400)
            x=random.randint(-200,200)
            y=random.randint(100,200)
            enemy.setposition(x, y)
            bulletstate="ready"
            score+=10
            scorestring="Score=%s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 12, "bold"))


        #checking if the enemy collides with player
        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            pen=turtle.Turtle()
            pen.hideturtle()
            pen.color("white")
            pen.speed(0)
            string="   Game Over\nYour Score=%s" %score
            pen.write(string, False, align="center", font=("Arial", 12, "bold"))
            break
        
    #move the bullet
    if bulletstate=="fire":
        bullet.sety(bullet.ycor()+bulletspeed)
    if bullet.ycor()>280:
        bullet.hideturtle()
        bulletstate="ready"



delay=raw_input("Press Enter to exit!")