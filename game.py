import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1061,596))
background = pygame.image.load('jungleresized1.jpeg')


pygame.display.set_caption("Jungle Hunt!!!")
icon = pygame.image.load('enemy.png')
pygame.display.set_icon(icon)

playerImage = pygame.image.load('man.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

planeImage = pygame.image.load('plane.png')
planeX = 1000
planeY = 50

enemyImage = pygame.image.load('enemy.png')
enemyX = -30
enemyY = 50
enemyX_change = 1
enemyY_change = 1
enemy_status = "ready"

rocketImage = pygame.image.load('rocket.png')
rocketX = 0
rocketY = 480
rocketX_change = 1
rocketY_change = 2
rocket_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)


def enemy(enemyX,enemyY):
	global enemy_status
	enemy_status = "drop"
	screen.blit(enemyImage,(enemyX,enemyY))

def player(playerX,playerY):
	screen.blit(playerImage,(playerX,playerY))

def plane(planeX,planeY):
	screen.blit(planeImage,(planeX,planeY))

def fire_rocket(x,y):
         global rocket_state
         rocket_state = "fire"
         screen.blit(rocketImage, (x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
	distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
	if distance < 27:
		return True
	else:
		return False

def showScore(x,y):
	score = font.render("Score: " + str(score_value), True, (255,255,255))
	screen.blit(score, (x,y))

def game_over_text():
	over_text = font.render("Game Over ", True, (0,0,0))
	screen.blit(over_text,(200,250))



run = True

while run:
	screen.fill((255,0,0))
	screen.blit(background,(0,0))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			playerX_change = -5
		if event.key == pygame.K_RIGHT:
			playerX_change = 5
		if event.key == pygame.K_SPACE:
			if rocket_state is "fire":
				rocketX = playerX
				fire_rocket(rocketX,rocketY)
				

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or pygame.K_RIGHT:
			playerX_change = 0

	#if event.type == pygame.KEYDOWN:
	#	if event.key == pygame.K_UP:
	#		playerY_change = -5
	#	if event.key == pygame.K_DOWN:
	#		playerY_change = 5 	

	if rocketY <= 0:
		rocketY = 480
		rocket_state = "ready"

	if rocket_state is "fire":
		fire_rocket(rocketX,rocketY)
		rocketY = rocketY - rocketY_change

	if enemyY>=590:
		game_over_text()
		run = False

	playerX += playerX_change
	if playerX<=0:
		playerX = 0
	elif playerX>= 950:
		playerX = 950

	if enemy_status == "ready":
		enemyX = planeX
		enemy(enemyX,enemyY)

	playerY += playerY_change
	if playerY<=40:
		playerY = 40
	elif playerY>=550:
		playerY = 550

	planeX += 3
	if planeX >=1000:
		planeX = 0

	if enemyY > 596:
		enemyY = 50
		enemy_status = "ready"

	if enemy_status == "ready":
		enemyX = planeX
		enemy(enemyX,enemyY)

	if enemy_status == "drop":
		enemy(enemyX,enemyY)
		enemyY+=3

	player(playerX,playerY)
	plane(planeX,planeY)

	score_value +=1
	showScore(10,10)
	
	collision = isCollision(enemyX,enemyY,rocketX,rocketY)

	if collision:
		rocketY = 480
		enemyX = planeX
		enemyY = 50
		rocket_state = "ready"
		

	pygame.display.update()