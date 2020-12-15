#########################################################
# RUN 'snakegame.py' TO STATR THE GAME FROM THE STATING #
#########################################################

#########################################################
# THIS IS NOT TO BE RUN, FROM HERE ######################
#########################################################
####   CAUTION ##################

import pygame # took help from stack over flow to learn
import turtle # took help from git hub and stack over flow to learn
import time 
import random

time_lag = 0.1 # This is the time between the two succesive animation change. Here it is used to control the speed of motin of snake.
#Bydereasing it, we can decrease the time of execution of animation
pygame.init()
#This are all music parameters used 
music=pygame.mixer.Sound("Sounds\\game_music.wav")
music.play(-1)
food_eat=pygame.mixer.Sound("Sounds\\food_eat.wav")
game_over=pygame.mixer.Sound("Sounds\\game_over.wav")
#Assigning the variables
score = 0
high_score = 0
level=1
body_parts = []

# Setting up of screen variables
display = turtle.Screen()
display.title("Snake Ultimate by ADITYA and DEVANSHU")
display.bgpic('Images\\backpic2.gif')
display.setup(width=600, height=600)
display.tracer(0) # Turns off the screen updates

# Snake mouth
mouth = turtle.Turtle()
mouth.speed(0)
###########################################################################
display.addshape('Images\\snake_mouth.gif')  ########### THIS IS THE ONLY #
turtle.shape('Images\\snake_mouth.gif')   #####        DIFFERENCE BETWEEN #
mouth.shape('Images\\snake_mouth.gif')   ####### 'main1.py' AND 'main2.py'#
###########################################################################
#mouth.color("black")
mouth.penup()
mouth.goto(40,0)
mouth.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
fx,fy=random.randint(-280,280), random.randint(-280,280)
food.goto(fx,fy)

# Snake Obstacle
obstacle=turtle.Turtle()
display.addshape('Images\\brick.gif')
turtle.shape('Images\\brick.gif')
obstacle.shape("Images\\brick.gif")
obstacle.penup()
obstacle.speed()
obstacle.goto(40,40)
obstacle.pendown()


obs_=turtle.Turtle()
display.addshape('Images\\brick.gif')
turtle.shape('Images\\brick.gif')
obs_.shape("Images\\brick.gif")
obs_.penup()
obs_.speed()
obs_.goto(0,0)
obs_.goto(0,0)
obs_.pendown()

obs2=turtle.Turtle()
obs2.penup()
obs2.speed(0)
display.addshape('Images\\brick.gif')
turtle.shape('Images\\brick.gif')
obs2.shape("Images\\brick.gif")
#obs2.shape("square")
#obs2.color("black")
c2,d2=1,1

obs3=turtle.Turtle()
obs3.penup()
obs3.speed(0)

display.addshape('Images\\brick.gif')
turtle.shape('Images\\brick.gif')
obs3.shape("Images\\brick.gif")
#obs3.shape("square")
#obs3.color("black")
c3,d3=1,1

obs4=turtle.Turtle()
obs4.penup()
obs4.speed(0)
display.addshape('Images\\brick.gif')
turtle.shape('Images\\brick.gif')
obs4.shape("Images\\brick.gif")
x4=random.randint(-299,299)
y4=random.randint(-299,299)
c4,d4=1,1

obs5=turtle.Turtle()
obs5.penup()
obs5.speed(0)
display.addshape('Images\\brick.gif')
turtle.shape('Images\\brick.gif')
obs5.shape("Images\\brick.gif")
#obs2.shape("square")
#obs2.color("black")
c5,d5=1,1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0 Level: 1", align="center", font=("Courier", 22, "normal"))

# Functions # this basic idea is consulted or referred from GIT HUB 
def move_up():
    if mouth.direction != "down":
        mouth.direction = "up"

def move_down():
    if mouth.direction != "up":
        mouth.direction = "down"

def move_left():
    if mouth.direction != "right":
        mouth.direction = "left"

def move_right():
    if mouth.direction != "left":
        mouth.direction = "right"

def move():
    
        
    if mouth.direction == "up":
        y = mouth.ycor()
        mouth.sety(y + 20)

    if mouth.direction == "down":
        y = mouth.ycor()
        mouth.sety(y - 20)

    if mouth.direction == "left":
        x = mouth.xcor()
        mouth.setx(x - 20)

    if mouth.direction == "right":
        x = mouth.xcor()
        mouth.setx(x + 20)

# Keyboard bindings
display.listen()
display.onkeypress(move_up, "Up")
display.onkeypress(move_down, "Down")
display.onkeypress(move_left, "Left")
display.onkeypress(move_right, "Right")

# Main game loop
while True:
    display.update()
    

    if level==2 and c2>=d2:
        x2=random.randint(-299,299)
        y2=random.randint(-299,299)
        obs2.penup()
        obs2.goto(x2,y2)
        d2+=1
    
    if level == 3 and c3>=d3:
        x3=random.randint(-299,299)
        y3=random.randint(-299,299)
        obs3.penup()
        obs3.goto(x3,y3)
        d3+=1
    
    if level == 4 and c4>=d4:
        x4=random.randint(-299,299)
        y4=random.randint(-299,299)
        obs4.penup()
        obs4.goto(x4,y4)
        d4+=1


    # Check for a collision with the border
    if mouth.distance(obs3)<20 and level>=3:
        time.sleep(1)
        mouth.goto(40,0)
        mouth.direction = "stop"
        display.addshape('Images\\game_over.gif')
        turtle.shape('Images\\game_over.gif')
        display.update()
        pygame.mixer.pause()    
        game_over.play()    
        time.sleep(3.2)
        turtle.shape("blank")
        display.update()
        pygame.mixer.unpause()
        display.bgpic('Images\\backpic.gif')
        time_lag = 0.1
        pen.clear()
        obs3.reset(),obs2.reset(),obs4.reset()
        c2=d2
        c3=d3
        c4=d4
        c5=d5
        for body in body_parts:
            body.goto(1000, 1000)
        
        # Clear the body_parts list
        body_parts.clear()

        # Reset the score
        score = 0
        level = 1

        # Reset the time_lag
        time_lag = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))
        
        
    
    if mouth.distance(obs4)<20 and level>=4:
        time.sleep(1)
        mouth.goto(40,0)
        mouth.direction = "stop"
        display.addshape('Images\\game_over.gif')
        turtle.shape('Images\\game_over.gif')
        display.update()
        pygame.mixer.pause()    
        game_over.play()    
        time.sleep(3.2)
        turtle.shape("blank")
        display.update()
        pygame.mixer.unpause()
        display.bgpic('Images\\backpic.gif')
        # Reset the time_lag
        time_lag = 0.1
        pen.clear()
        obs3.reset(),obs2.reset(),obs4.reset()
        c2=d2
        c3=d3
        c4=d4
        c5=d5
        for body in body_parts:
            body.goto(1000, 1000)
        
        # Clear the body_parts list
        body_parts.clear()

        # Reset the score
        score = 0
        level = 1

        # Reset the time_lag
        time_lag = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))

    if mouth.distance(obs2)<20 and level>=2:
        time.sleep(1)
        mouth.goto(40,0)
        mouth.direction = "stop"
        display.addshape('Images\\game_over.gif')
        turtle.shape('Images\\game_over.gif')
        display.update()
        pygame.mixer.pause()    
        game_over.play()    
        time.sleep(3.2)
        turtle.shape("blank")
        display.update()
        obs2.hideturtle()
        pygame.mixer.unpause()
        display.bgpic('Images\\backpic.gif')
        # Reset the time_lag
        time_lag = 0.1
        pen.clear()
        obs3.reset(),obs2.reset(),obs4.reset()
        c2=d2
        c3=d3
        c4=d4
        c5=d5
        for body in body_parts:
            body.goto(1000, 1000)
        
        # Clear the body_parts list
        body_parts.clear()

        # Reset the score
        score = 0
        level = 1

        # Reset the time_lag
        time_lag = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))
        
    
    if mouth.distance(obstacle)<20:
        time.sleep(1)
        mouth.goto(40,0)
        mouth.direction = "stop"
        display.addshape('Images\\game_over.gif')
        turtle.shape('Images\\game_over.gif')
        display.update()
        pygame.mixer.pause()    
        game_over.play()    
        time.sleep(3.2)
        turtle.shape("blank")
        display.update()
        pygame.mixer.unpause()
        display.bgpic('Images\\backpic.gif')
        score = 0
        level = 1
        # Reset the time_lag
        time_lag = 0.1
        pen.clear()
        obs3.reset(),obs2.reset(),obs4.reset()
        c2=d2
        c3=d3
        c4=d4
        c5=d5 
        for body in body_parts:
            body.goto(1000, 1000)
        
        # Clear the body_parts list
        body_parts.clear()

        # Reset the score
        score = 0
        level = 1

        # Reset the time_lag
        time_lag = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))
        
    if mouth.distance(obs_)<20:
        time.sleep(1)
        mouth.goto(40,0)
        mouth.direction = "stop"
        display.addshape('Images\\game_over.gif')
        turtle.shape('Images\\game_over.gif')
        display.update()
        pygame.mixer.pause()    
        game_over.play()    
        time.sleep(3.2)
        turtle.shape("blank")
        display.update()
        pygame.mixer.unpause()
        display.bgpic('Images\\backpic.gif')
        score = 0
        level = 1
        # Reset the time_lag
        time_lag = 0.1
        pen.clear()
        obs3.reset(),obs2.reset(),obs4.reset()
        c2=d2
        c3=d3
        c4=d4
        c5=d5 
        for body in body_parts:
            body.goto(1000, 1000)
        
        # Clear the body_parts list
        body_parts.clear()

        # Reset the score
        score = 0
        level = 1

        # Reset the time_lag
        time_lag = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))

    if mouth.xcor()>290 or mouth.xcor()<-290 or mouth.ycor()>290 or mouth.ycor()<-290:
        time.sleep(1)
        mouth.goto(40,0)
        mouth.direction = "stop"
        display.addshape('Images\\game_over_brick.gif')
        turtle.shape('Images\\game_over_brick.gif')
        display.update()
        pygame.mixer.pause()    
        game_over.play()    
        time.sleep(3.2)
        turtle.shape("blank")
        display.update()
        pygame.mixer.unpause()
        obs3.reset(),obs2.reset(),obs4.reset()
        c2=d2
        c3=d3
        c4=d4 
        c5=d5    
        # Hide the body_parts
        for body in body_parts:
            body.goto(1000, 1000)
        
        # Clear the body_parts list
        body_parts.clear()

        # Reset the score
        score = 0
        level = 1

        # Reset the time_lag
        time_lag = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal")) 


    # Check for a collision with the food
    
    if mouth.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        #plays the sound
        food_eat.play()
        # Add a body
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        color_set={"red", "green", "yellow",'violet','blue','black','magenta','pink','grey'}
        for n in color_set:    
            new_body.color(n)
            new_body.penup()
            body_parts.append(new_body)

        # Shorten the time_lag # idea from git hub 
        time_lag -= 0.01

        # Increase the score
        score += 10
        if score%20==0:
            level+=1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal")) 
   
    # Move the end body_parts first in reverse order
    for index in range(len(body_parts)-1, 0, -1):
        x = body_parts[index-1].xcor()
        y = body_parts[index-1].ycor()
        body_parts[index].goto(x, y)

    # Move body 0 to where the mouth is
    if len(body_parts) > 0:
        x = mouth.xcor()
        y = mouth.ycor()
        body_parts[0].goto(x,y)

    move()    
    
    if level == 1:
        display.bgpic('Images\\backpic2.gif')
    if level == 2:
        display.bgpic('Images\\backpic.gif')
    if level == 3:
        display.bgpic('Images\\backpic3.gif')
    if level == 4:
        display.bgpic('Images\\backpic4.gif')
    if level == 5:
        display.bgpic('Images\\backpic5.gif')

    # Check for mouth collision with the body body_parts
    for body in body_parts:
        if body.distance(mouth) < 20:
            time.sleep(1)
            mouth.goto(40,0)
            mouth.direction = "stop"
            display.addshape('Images\\game_over_snake.gif')
            turtle.shape('Images\\game_over_snake.gif')
            display.update()
            pygame.mixer.pause()    
            game_over.play()    
            time.sleep(3.2)
            turtle.shape("blank")
            display.update()
            pygame.mixer.unpause()
            display.bgpic('Images\\backpic2.gif')
            # Hide the body_parts
            for body in body_parts:
                body.goto(1000, 1000)
        
            # Clear the body_parts list
            body_parts.clear()

            # Reset the score
            score = 0
            level = 1
            # Reset the time_lag
            time_lag = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {} Level: {}".format(score, high_score, level), align="center", font=("Courier", 22, "normal"))

    time.sleep(time_lag)
display.mainloop()




######################### the game has not been made from scratch. A very basic idea was taken from a template file(from github), that too not copied but rewritten by us. Many modifications and new features has been added.  
