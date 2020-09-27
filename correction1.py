import pygame

 import random

 import math

 pygame.init()

 #screen window and background

 screen = pygame.display.set_mode((1179,600))

 background = pygame.image.load('forest.png')

 #icon and Application name

 pygame.display.set_caption("Para Attack")

 icon = pygame.image.load('enemy.png')

 pygame.display.set_icon(icon)



#Score board

 score_value = 0

 font = pygame.font.Font('freesansbold.ttf', 32)

 textX = 10

 testY = 10



# Game Over

 over_font = pygame.font.Font('freesansbold.ttf', 64)



#import moving plane

 planeimg = pygame.image.load('plane.png')

 planeX=0

 planeY=50





 #import opponent

 paraimg=pygame.image.load('enemy.png')

 paraX=-30

 paraY=50

 paraX_change=1

 paraY_change=1

 para_status="ready"



#import player

 playerImg = pygame.image.load('man.png')

 playerX = 370

 playerY = 480

 playerX_change = 0



#import weapon

 rocketimg=pygame.image.load('rocket.png')

 rocketX=0

 rocketY=480

 rocketX_change = 1

 rocketY_change = 2

 rocket_state = "ready"







 #function for display score

 def show_score(x, y):

 score = font.render("Score : " + str(score_value), True, (255, 255, 255))

 screen.blit(score, (x, y))



#function for plane position

 def plane(X,Y):

 screen.blit(planeimg, (X,Y))



#function for oponenet postition

 def paradrop(a,b):

 global para_status

 para_status = "drop"

 screen.blit(paraimg,(a,b))





 #function for plaer position

 def player(x, y):

 screen.blit(playerImg, (x, y))



#funcition for attack opponent

 def fire_rocket(x,y):

 global rocket_state

 rocket_state = "fire"

 screen.blit(rocketimg, (x , y ))



#function for find hit of the opponent

 def isCollision(enemyX, enemyY, bulletX, bulletY):

 distance = math.sqrt(math.pow(paraX - rocketX, 2) + (math.pow(paraY - rocketY, 2)))

 if distance < 27:

 return True

 else:

 return False



#game over function

 def game_over_text():

 over_text = over_font.render("GAME OVER", True, (255, 255, 255))

 screen.blit(over_text, (200, 250))



#main program

 run = True

 while run:



# RGB - Red, Green, Blue

 screen.fill((255, 255, 255))



# background Image

 screen.blit(background,(0,0))



# find the key pressing

 for event in pygame.event.get():

 if event.type == pygame.QUIT:

 run = False



if event.type == pygame.KEYDOWN:

 if event.key == pygame.K_LEFT:

 playerX_change = -5

 if event.key == pygame.K_RIGHT:

 playerX_change = 5

 if event.key == pygame.K_SPACE:

 if rocket_state is "ready":

 rocketX = playerX

 fire_rocket(rocketX, rocketY)



if event.type == pygame.KEYUP:

 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

 playerX_change = 0





 #make opponent appear random

 if para_status == "ready":

 if random.randint(0,100) ==5:

 paraX = planeX

 paradrop(paraX, paraY) #calling paradrop function



#Game over

 if paraY >= 600:

 game_over_text()






 #changing the player position key press

 playerX += playerX_change

 if playerX <= 0:

 playerX = 0

 elif playerX >= 1150:

 playerX = 1150



#make the plane run from left to right

 planeX += 3

 if planeX == 1179:

 planeX=0


 #make the opponent drop to ground

 if para_status == "drop":

 paradrop(paraX, paraY)

 paraY += 1



#make the rocket appear to ready state when previous rocket reaches the boundary

 if rocketY <= 0:

 rocketY = 480

 rocket_state = "ready"


 #if rocket state show fire means that the make the rocket travel in straight direction towards sky

 if rocket_state is "fire":

 fire_rocket(rocketX, rocketY)

 rocketY -= rocketY_change



#if the rocket hit the opponent make score increase by 1

 collision = isCollision(paraX, paraY, rocketX, rocketY)

 if collision:

 rocketY = 480

 score_value += 1

 paraX = planeX

 paraY = 50

 rocket_state = "ready"



#show the current score status

 show_score(textX, testY)

 #update the current player position

 player(playerX,playerY)

 #update the currnet plane position

 plane(planeX,planeY)

 #update display

 pygame.display.update()