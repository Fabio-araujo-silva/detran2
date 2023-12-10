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
carro2 = pygame.transform.rotate(carro, 180)
carro3 = pygame.transform.rotate(carro, -90)
carro4 = pygame.transform.rotate(carro, 90)

# Redimensionar os sprites
novo_largura_sem, novo_altura_sem = 100, 100
novo_largura_carro, novo_altura_carro = 50, 93
sem1 = pygame.transform.scale(sem1, (novo_largura_sem, novo_altura_sem))
sem2 = pygame.transform.scale(sem2, (novo_largura_sem, novo_altura_sem))
sem3 = pygame.transform.scale(sem3, (novo_largura_sem, novo_altura_sem))
sem4 = pygame.transform.scale(sem4, (novo_largura_sem, novo_altura_sem))
carro = pygame.transform.scale(carro, (novo_largura_carro, novo_altura_carro))
carro2 = pygame.transform.scale(carro2, (novo_largura_carro, novo_altura_carro))
carro3 = pygame.transform.scale(carro3, (novo_altura_carro,novo_largura_carro))
carro4 = pygame.transform.scale(carro4, (novo_altura_carro,novo_largura_carro))

# Posição inicial do carro
carro_inicial_pos = (290, 0)
carro2_inicial_pos = (350, 700)
carro3_inicial_pos = (700, 300)
carro4_inicial_pos = (0, 370)

# Lista de sprites e suas posições
sprites = [(sem1, (200, 150)), (sem2, (100, 450)), (sem3, (500, 150)), (sem4, (400, 450)), (carro, carro_inicial_pos), (carro2, carro2_inicial_pos), (carro3, carro3_inicial_pos), (carro4, carro4_inicial_pos)]

# Controle de tempo para gerar novos carros
tempo_para_novo_carro = 5000
tempo_acumulado = 0

# Velocidade dos carros
velocidade_carro = 0.05

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar a posição dos carros existentes
    for i, (sprite, pos) in enumerate(sprites):
        if sprite == carro:  # Ajustar apenas a posição do carro
            nova_posicao = (pos[0], pos[1] + velocidade_carro)  # Movendo o carro para baixo
            sprites[i] = (sprite, nova_posicao)
        elif sprite == carro2:
            nova_posicao = (pos[0], pos[1] - velocidade_carro)  # Movendo o carro para cima
            sprites[i] = (sprite, nova_posicao)
        elif sprite == carro3:
            nova_posicao = (pos[0] - velocidade_carro, pos[1])  # Movendo o carro para a esquerda
            sprites[i] = (sprite, nova_posicao)
        elif sprite == carro4:
            nova_posicao = (pos[0] + velocidade_carro, pos[1])  # Movendo o carro para a direita
            sprites[i] = (sprite, nova_posicao)

    # Controle de tempo para gerar novos carros
    tempo_passado = pygame.time.get_ticks()
    tempo_decorrido = tempo_passado - tempo_acumulado

    # Gerar um novo carro a cada segundo
    if tempo_decorrido > tempo_para_novo_carro:
        # Alternar entre os carros
        if len(sprites) % 4 == 0:
            novo_sprite, nova_posicao = carro, carro_inicial_pos
        elif len(sprites) % 4 == 1:
            novo_sprite, nova_posicao = carro2, carro2_inicial_pos
        elif len(sprites) % 4 == 2:
            novo_sprite, nova_posicao = carro3, carro3_inicial_pos
        else:
            novo_sprite, nova_posicao = carro4, carro4_inicial_pos
        sprites.append((novo_sprite, nova_posicao))
        tempo_acumulado = tempo_passado

    # Remover carros que saíram da tela
    sprites = [(sprite, pos) for (sprite, pos) in sprites if 0 <= pos[0] <= width and 0 <= pos[1] <= height]

    # Desenhar o background
    screen.blit(background, (0, 0))

    # Desenhar os sprites
    for sprite, pos in sprites:
        screen.blit(sprite, pos)

    pygame.display.flip()
