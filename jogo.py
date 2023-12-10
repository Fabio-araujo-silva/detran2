import pygame
import sys

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
carro = pygame.image.load("carro.png").convert_alpha()

# Posições iniciais dos sprites
sem1_pos = (100, 100)
sem2_pos = (200, 200)
sem3_pos = (300, 300)
sem4_pos = (400, 400)
carro_pos = (500, 500)

# Carregar os sprites e redimensioná-los
novo_largura_sem, novo_altura_sem = 50,50
novo_largura_carro, novo_altura_carro = 50,93
sem1 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))
sem2 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))
sem3 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))
sem4 = pygame.transform.scale(pygame.image.load("semaforo.png").convert_alpha(), (novo_largura_sem, novo_altura_sem))
carro = pygame.transform.scale(pygame.image.load("carro.png").convert_alpha(), (novo_largura_carro, novo_altura_carro))


# Lista de sprites e suas posições
sprites = [(sem1, sem1_pos), (sem2, sem2_pos), (sem3, sem3_pos), (sem4, sem4_pos), (carro, carro_pos)]

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

    pygame.display.flip()