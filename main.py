import pygame

# Inicia o pygame
pygame.init ()

# cria a tela
screen = pygame.display.set_mode((800, 600))

# Loop do jogo (necessário para manter o jogo aberto)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

