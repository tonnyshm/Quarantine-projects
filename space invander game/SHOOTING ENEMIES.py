import pygame
import random
import math

pygame.init()  # initialize the pygame LIB
screen = pygame.display.set_mode((800, 600))

# TITLE AND ICON
pygame.display.set_caption("INDEGE")
icon = pygame.image.load('Naboo.png')
pygame.display.set_icon(icon)

# BACKGROUND
background = pygame.image.load('spacex2.png')
# PLAYER1
playerimg = pygame.image.load('player1.png')
playerX = 350
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerimg, (x, y))


enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('beast.png'))
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

    # BULLETS ADD:

    bulletimg = pygame.image.load('bullet.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    # READY= "YOU CANT SEE THE BULLET ON THE SCREEN"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 30, y + 10))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


score = 0


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True  # GAME LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB VALUES FOR THE SCREEN
    # creen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # IF ANY KEYSTROKE HAPPEN
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -10
        if event.key == pygame.K_RIGHT:
            playerX_change = 10
        if event.key == pygame.K_END:
            bulletX = playerX
            fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        # collision
        scollision = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if scollision:
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    pygame.display.update()
