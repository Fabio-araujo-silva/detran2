import pygame
import sys
import random

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
carro3 = pygame.transform.scale(carro3, (novo_altura_carro, novo_largura_carro))
carro4 = pygame.transform.scale(carro4, (novo_altura_carro, novo_largura_carro))

# Posição inicial do carro
carro_inicial_pos = (290, 0)
carro2_inicial_pos = (350, 700)
carro3_inicial_pos = (700, 300)
carro4_inicial_pos = (0, 370)

# Lista de carros e suas posições iniciais
carros = [(carro, carro_inicial_pos), (carro2, carro2_inicial_pos), (carro3, carro3_inicial_pos), (carro4, carro4_inicial_pos)]

# Lista de sprites e suas posições
sprites = [(sem1, (200, 150)), (sem2, (100, 450)), (sem3, (500, 150)), (sem4, (400, 450))]

# Controle de tempo para gerar novos carros
tempo_para_novo_carro = 5000
tempo_acumulado = pygame.time.get_ticks()  # Começar com o tempo atual

# Contador inicial para mostrar na tela
fonte_gta = pygame.font.Font("gta_font.ttf", 48)  # Substitua "gta_font.ttf" pelo caminho real da fonte GTA
contador_texto = fonte_gta.render("5", True, (255, 255, 255))  # Contagem regressiva inicial
contador_rect = contador_texto.get_rect(center=(350, 350))
tempo_inicial = pygame.time.get_ticks()

# Velocidade dos carros
velocidade_carro = 0.5

# Loop principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar a posição dos carros existentes
    for i, (sprite, pos) in enumerate(sprites):
        if sprite in (carro, carro2, carro3, carro4):  # Verificar se é um carro
            if sprite == carro:  # Movendo o carro para baixo
                nova_posicao = (pos[0], pos[1] + velocidade_carro)
            elif sprite == carro2:  # Movendo o carro para cima
                nova_posicao = (pos[0], pos[1] - velocidade_carro)
            elif sprite == carro3:  # Movendo o carro para a esquerda
                nova_posicao = (pos[0] - velocidade_carro, pos[1])
            elif sprite == carro4:  # Movendo o carro para a direita
                nova_posicao = (pos[0] + velocidade_carro, pos[1])
            sprites[i] = (sprite, nova_posicao)

    # Controle de tempo para gerar novos carros
    tempo_passado = pygame.time.get_ticks()
    tempo_decorrido = tempo_passado - tempo_acumulado

    # Gerar um novo carro a cada segundo
    if tempo_decorrido > tempo_para_novo_carro:
        # Selecionar um carro e sua posição inicial aleatoriamente
        novo_sprite, nova_posicao = random.choice(carros)
        sprites.append((novo_sprite, nova_posicao))
        tempo_acumulado = tempo_passado

    # Remover carros que saíram da tela
    sprites = [(sprite, pos) for (sprite, pos) in sprites if 0 <= pos[0] <= width and 0 <= pos[1] <= height]

    # Atualizar o contador inicial
    tempo_decorrido_total = (pygame.time.get_ticks() - tempo_inicial) // 1000  # Tempo decorrido em segundos
    if tempo_decorrido_total < 5:  # Mostrar a contagem regressiva inicial
        contador_texto = fonte_gta.render(f"{5 - tempo_decorrido_total}", True, (255, 255, 255))
    else:
        contador_texto = None  # Não renderizar o contador

    # Desenhar o background
    screen.blit(background, (0, 0))

    # Desenhar o contador
    if contador_texto:
        screen.blit(contador_texto, contador_rect)

    # Desenhar os sprites
    for sprite, pos in sprites:
        screen.blit(sprite, pos)

    pygame.display.flip()

    clock.tick(60)  # Limitar a taxa de quadros para 60 FPS
