import pygame
import sys, time
import random

pygame.init()
frame = pygame.display.set_mode((640,480))

#Colors
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
frame.fill(black)

grow=False
move=1

#Game Module 
snake=list()
snake=[(100,40,20,20),(100,60,20,20),(100,80,20,20)]

randomX= random.randrange(20,621,20)
randomY= random.randrange(20,461,20)

#OBJECT
def snakeChange():
    global move
    global done
    global randomX
    global randomY
    
    #CHANGES
    x,y,w,h=snake[0]

    if move==1:
        x+=20
    elif move==2:
        x-=20
    elif move==3:
        y-=20
    elif move==4:
        y+=20

    #CRASHES
    if (x,y,w,h) in snake:
        done=True
    if x<=0 or y<=0 or x>=640 or y>=480:
        done=True

    #MOVES  
    snake.insert(0,(x,y,w,h))
    snake.pop(len(snake)-1)
        
#SNACKS
def snacks():
    global grow
    global randomX
    global randomY
    
    pygame.draw.rect(frame,blue,(randomX,randomY,20,20),0)

    x,y,w,h=snake[0]    
    if x==randomX and y==randomY:
        randomX= random.randrange(20,621,20)
        randomY= random.randrange(20,461,20)
        grow=True
        pygame.draw.rect(frame,blue,(randomX,randomY,20,20),0)

    #OTHER SUPPLEMENTS
    
    
#Run Game
done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move=1
            elif event.key == pygame.K_LEFT:
                move=2
            elif event.key == pygame.K_UP:
                move=3
            elif event.key == pygame.K_DOWN:
                move=4

    snakeChange()

    if grow:
        for i in range(3):
            x,y,w,h=snake[0]
            snake.insert(0,(x,y,w,h))
        grow=False

    frame.fill(black)
    for s in range(len(snake)):
        pygame.draw.rect(frame,white,snake[s],0)
        pygame.draw.rect(frame,blue,snake[s],1)

    snacks()

    pygame.display.update()
    time.sleep(.1)

pygame.quit()
