import pygame
import math
import random

# Inicia o pygame
pygame.init ()

# cria a tela
screen = pygame.display.set_mode((800, 600))

# Título e Icone ---- icon Site -> flaticon.com
pygame.display.set_caption('Invasão Espacial')
icon = pygame.image.load('main-game/img/navinha.png')
pygame.display.set_icon(icon)


# Background --- image Site -> freepik.com
background = pygame.image.load('main-game/img/background.jpg')


# Jogador
playerImg = pygame.image.load('main-game/img/navinha-player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Inimigo
inimigoImg = []
inimigoX = []
inimigoY = []
inimigoX_change = []
inimigoY_change = []
num_inimigos = 6

for i in range(num_inimigos):
    inimigoImg.append(pygame.image.load('main-game/img/alien.png'))
    inimigoX.append(random.randint(0, 800))
    inimigoY.append(random.randint(50, 150))
    inimigoX_change.append(0.3)
    inimigoY_change.append(40)

# Bullet

# Ready - Não é possível ver a bala na tela
# Fire - A bala irá se mover
bulletImg = pygame.image.load('main-game/img/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = 'ready'

# Score --- Site para Fontes -> dafont.com
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over texto
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x,y):
    score = font.render("Pontos: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))



def game_over_text():
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))



def player(x, y):
    screen.blit(playerImg, (x, y))



def inimigo(x, y, i):
    screen.blit(inimigoImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16,y + 10))


def isCollision (inimigoX, inimigoY, bulletX, bulletY):
    distance = math.sqrt(math.pow(inimigoX-bulletX, 2)) + (math.pow(inimigoY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False



# Loop do jogo (necessário para manter o jogo aberto)
running = True
while running:

    # RGB
    screen.fill((0, 0, 0))
    
    # Background img
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Se a tecla for pressionada verifique se é direita ou esquerda
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    # Permite que o player consiga atirar mais de 1 vez
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Verifica se ninguém ta saindo da tela
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Movimentação do inimigo
    for i in range(num_inimigos):

        # Game Over
        if inimigoY[i] > 440:
            for j in range(num_inimigos):
                inimigoY[j] = 2000
            game_over_text()
            break

        inimigoX[i] += inimigoX_change[i]
        if inimigoX[i] <= 0:
            inimigoX_change[i] = 0.3
            inimigoY[i] += inimigoY_change[i]
        elif inimigoX[i] >= 736:
            inimigoX_change[i] = -0.3
            inimigoY[i] += inimigoY_change[i]

        # Colisão
        collision = isCollision(inimigoX[i], inimigoY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            inimigoX[i] = random.randint(0, 736)
            inimigoY[i] = random.randint(50, 150)
            
        inimigo(inimigoX[i], inimigoY[i], i)

    # Movimentação da bala
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
        
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

