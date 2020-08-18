import pygame
import random as rand

def towardsMiddle(current, center):
    xPos = current[0]
    yPos = current[1]
    xCen = center[0]
    yCen = center[1]
    if int((xCen - xPos)/50)<0:
        xPos -= 1
    elif int((xCen - xPos)/50)>0:
        xPos += 1
    
    if int((yCen - yPos)/50)<0:
        yPos -= 1
    elif int((yCen - yPos)/50)>0:
        yPos += 1
    
    newPos = (xPos,yPos)
    return newPos

def randTuple():
    newEnemy = (rand.randrange(0,w),rand.randrange(0,h))
    if ((w/2-750)<newEnemy[0]<(w/2+75)) and ((h/2-75)<newEnemy[1]<(h/2+75)):
        newEnemy = randTuple()
    return newEnemy

#Start setup
pygame.init()
h=400
w=500
win = pygame.display.set_mode((w,h))
pygame.display.set_caption("My first game")
#End setup

playerX = int((w/2))
playerY = int((h/2))
player = (playerX,playerY)

wPressed = False
aPressed = False
sPressed = False
dPressed = False

enemies = []

hp = 1000

#Game loop
isRunning = True
while isRunning:
    pygame.time.delay(50)


    
    #Your code goes here
    win.fill((0,0,0))
    if wPressed == True:
        playerY = playerY - 5
    if aPressed == True:
        playerX = playerX - 5
    if sPressed == True:
        playerY = playerY + 5
    if dPressed == True:
        playerX = playerX + 5

    if playerX<25 or playerX>(w-25) or playerY<25 or playerY>(h-25):
        playerX = int((w/2))
        playerY = int((h/2))

    if len(enemies) < 4:
        enemies.append(randTuple())

    index=0
    for enemy in enemies:
        pygame.draw.circle(win, (0,0,255),enemy,20)
        if -30<(enemy[0]-player[0])<30 and -30<(enemy[1]-player[1])<30:
            enemies.remove(enemy)
            #Remove the enemy
        if len(enemies) == 4:
            enemies[index] = towardsMiddle(enemy,(int(w/2),int(h/2)))
        if ((w/2-50)<enemy[0]<(w/2+50)) and ((h/2-50)<enemy[1]<(h/2+50)):
            hp -= 1
        index+=1
    
    player = (playerX,playerY)
    pygame.draw.rect(win, (255,255,255),(int(w/2)-52,int(h/2)-77,104,29),4)
    pygame.draw.rect(win, (192,192,192),(int(w/2)-50,int(h/2)-75,int(hp/10),25))
    pygame.draw.circle(win,(0,255,0),(int(w/2),int(h/2)),40)
    pygame.draw.circle(win,(255,0,0),player,25)


    if hp <= 0:
        isRunning = False

    pygame.display.set_caption("My First Game ("+str(int(hp/10))+")")

    
    #Event loop here
    pygame.display.update()
    for event in pygame.event.get():
        
        #Check if game quit
        if event.type == pygame.QUIT:
            isRunning = False

        #Gets pressed key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                wPressed = True
            if event.key == pygame.K_a:
                aPressed = True
            if event.key == pygame.K_s:
                sPressed = True
            if event.key == pygame.K_d:
                dPressed = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                wPressed = False
            if event.key == pygame.K_a:
                aPressed = False
            if event.key == pygame.K_s:
                sPressed = False
            if event.key == pygame.K_d:
                dPressed = False
                

pygame.quit()
