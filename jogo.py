import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
width, height = 700, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GTA VI ALPHA PRE-BUILD 2.5.234")

# Carregar o background
background = pygame.image.load("fundo.png").convert()

# Carregar os sprites
sem1 = pygame.image.load("semaforo.png").convert_alpha()
sem2 = pygame.image.load("semaforo.png").convert_alpha()
sem3 = pygame.image.load("semaforo.png").convert_alpha()
sem4 = pygame.image.load("semaforo.png").convert_alpha()

# Posições iniciais dos sprites
sem1_pos = (100, 100)
sem2_pos = (200, 200)
sem3_pos = (300, 300)
sem4_pos = (400, 400)

# Carregar os sprites e redimensioná-los
novo_largura_sem, novo_altura_sem = 50,50
novo_largura_carro, novo_altura_carro = 50,93
sem1 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))
sem2 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))
sem3 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))
sem4 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))

# Lista de sprites e suas posições
sprites = [(sem1, sem1_pos), (sem2, sem2_pos), (sem3, sem3_pos), (sem4, sem4_pos)]

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenhar o background
    screen.blit(background, (0, 0))

    # Desenhar os sprites
    for sprite, pos in sprites:
        screen.blit(sprite, pos)

    # Gerar um novo carro a cada intervalo de tempo aleatório
    if random.randint(0, 50) == 0:  # Ajuste este número para controlar a frequência de geração de carros
        carro_pos = (random.randint(0, width), random.randint(0, height))
        carro = pygame.transform.scale(pygame.image.load("carro.png").convert_alpha(), (novo_largura_carro, novo_altura_carro))
        sprites.append((carro, carro_pos))

    # Mover os carros
    for i, (sprite, pos) in enumerate(sprites):
        if sprite == carro:
            new_pos = (pos[0] + 1, pos[1])  # Ajuste este valor para controlar a velocidade do carro
            if new_pos[0] > width:
                sprites.remove((sprite, pos))
            else:
                sprites[i] = (sprite, new_pos)

    pygame.display.flip()
