import pygame
import sys
import random
import os

pygame.init()

# Configurações da tela
width, height = 700, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GTA VI ALPHA PRE-BUILD 2.5.234")

# Configurações de pasta de assets
assets_folder = os.path.join(os.path.dirname(__file__), 'assets')

#música de fundo
pygame.mixer.music.load(os.path.join(assets_folder, 'musica.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#background
background = pygame.image.load(os.path.join(assets_folder, "fundo.png")).convert()

# Carregar os sprites
sem1 = pygame.image.load(os.path.join(assets_folder, "semaforo.png")).convert_alpha()
sem2 = pygame.image.load(os.path.join(assets_folder, "semaforo.png")).convert_alpha()
sem3 = pygame.image.load(os.path.join(assets_folder, "semaforo.png")).convert_alpha()
sem4 = pygame.image.load(os.path.join(assets_folder, "semaforo.png")).convert_alpha()
carro = pygame.image.load(os.path.join(assets_folder, "carro.png")).convert_alpha()
carro2 = pygame.transform.rotate(carro, 180)
carro3 = pygame.transform.rotate(carro, -90)
carro4 = pygame.transform.rotate(carro, 90)

# Redimensionar os sprites
novo_largura_sem, novo_altura_sem = 100, 100
novo_largura_carro, novo_altura_carro = 50, 115
sem1 = pygame.transform.scale(sem1, (novo_largura_sem, novo_altura_sem))
sem2 = pygame.transform.scale(sem2, (novo_largura_sem, novo_altura_sem))
sem3 = pygame.transform.scale(sem3, (novo_largura_sem, novo_altura_sem))
sem4 = pygame.transform.scale(sem4, (novo_largura_sem, novo_altura_sem))
carro = pygame.transform.scale(carro, (novo_largura_carro, novo_altura_carro))
carro2 = pygame.transform.scale(carro2, (novo_largura_carro, novo_altura_carro))
carro3 = pygame.transform.scale(carro3, (novo_altura_carro, novo_largura_carro))
carro4 = pygame.transform.scale(carro4, (novo_altura_carro, novo_largura_carro))

# Posição inicial do carro
carro_inicial_pos = (280, 0)
carro2_inicial_pos = (360, 700)
carro3_inicial_pos = (700, 280)
carro4_inicial_pos = (0, 390)

# Lista de carros e suas posições iniciais
carros = [(carro, carro_inicial_pos), (carro2, carro2_inicial_pos), (carro3, carro3_inicial_pos), (carro4, carro4_inicial_pos)]

# Lista de sprites e suas posições
sprites = [(sem1, (200, 150)), (sem2, (100, 450)), (sem3, (500, 150)), (sem4, (400, 450))]

# Controle de tempo para gerar novos carros
tempo_para_novo_carro = 1000000000000000000000000000000000000000000
tempo_acumulado = 0

# Velocidade dos carros
velocidade_carro = 5

# Carregar a imagem do Game Over
game_over_image = pygame.image.load(os.path.join(assets_folder, "gameover.png")).convert_alpha()
game_over_rect = game_over_image.get_rect(center=(width // 2, height // 2))

# Variável de controle do estado do jogo
game_over = False

# Variáveis para controlar a visibilidade das faixas
faixa1_visivel = True
faixa2_visivel = True
faixa3_visivel = True
faixa4_visivel = True

clock = pygame.time.Clock()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for sprite, pos in sprites:
                if sprite in (sem1, sem2, sem3, sem4):  # Verificar se é um semáforo
                    sem_rect = pygame.Rect(pos, (novo_largura_sem, novo_altura_sem))
                    if sem_rect.collidepoint(x, y):
                        if pos == (400, 450):
                            faixa1_visivel = not faixa1_visivel
                        elif pos == (100, 450):
                            faixa2_visivel = not faixa2_visivel
                        elif pos == (200, 150):
                            faixa3_visivel = not faixa3_visivel
                        elif pos == (500, 150):
                            faixa4_visivel = not faixa4_visivel

    if not game_over:
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

                # Cria rect pra futura colisao
                rect_carro = pygame.Rect(nova_posicao, (novo_largura_carro, novo_altura_carro))

                # Verificar colisões
                for j, (outro_sprite, outra_pos) in enumerate(sprites[i+1:], start=i+1):
                    if outro_sprite in (carro, carro2, carro3, carro4):
                        rect_outro_carro = pygame.Rect(outra_pos, (novo_largura_carro, novo_altura_carro))
                        if rect_carro.colliderect(rect_outro_carro):
                            game_over = True
                            break

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

        # Desenhar o background
        screen.blit(background, (0, 0))

        # Desenhar os sprites
        for sprite, pos in sprites:
            screen.blit(sprite, pos)

        # Desenhar as faixas se estiverem visíveis
        if faixa1_visivel:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(355, 474, 50, 2))
        if faixa2_visivel:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(230, 360, 2, 50))
        if faixa3_visivel:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(290, 265, 50, 2))
        if faixa4_visivel:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(470, 300, 2, 50))

    else:
        # Desenhar a imagem de Game Over
        screen.blit(game_over_image, game_over_rect)

    pygame.display.flip()

    clock.tick(60)  # Limitar a taxa de quadros para 60 FPS
