import pygame
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
inimigoImg = pygame.image.load('main-game/img/alien.png')
inimigoX = random.randint(0, 800)
inimigoY = random.randint(50, 150)
inimigoX_change = 0.3
inimigoY_change = 40

# Bullet

# Ready - Não é possível ver a bala na tela
# Fire - A bala irá se mover
bulletImg = pygame.image.load('main-game/img/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1.5
bullet_state = 'ready'



def player(x, y):
    screen.blit(playerImg, (x, y))



def inimigo(x, y):
    screen.blit(inimigoImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16,y + 10))



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
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
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
    inimigoX += inimigoX_change

    if inimigoX <= 0:
        inimigoX_change = 0.3
        inimigoY += inimigoY_change
    elif inimigoX >= 736:
        inimigoX_change = -0.3
        inimigoY += inimigoY_change

    # Movimentação da bala
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
        
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    inimigo(inimigoX, inimigoY)
    pygame.display.update()

