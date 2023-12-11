import pygame
import sys
import random
import os

pygame.init()

# Configurações de pasta de assets
assets_folder = os.path.join(os.path.dirname(__file__), 'assets')

# Configurações iniciais
width, height = 700, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GTA VI ALPHA PRE-BUILD 2.5.234")
game_over = False

# Carregar a imagem do Game Over
game_over_image = pygame.image.load(os.path.join(assets_folder, "gameover.png")).convert_alpha()
game_over_rect = game_over_image.get_rect(center=(width // 2, height // 2))
background = pygame.image.load(os.path.join(assets_folder, "fundo.png")).convert()

# Música de fundo
pygame.mixer.music.load(os.path.join(assets_folder, 'musica.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Carregar os sprites
sem1 = pygame.image.load(os.path.join(assets_folder, "sem_verm.png")).convert_alpha()
sem2 = pygame.image.load(os.path.join(assets_folder, "sem_verm.png")).convert_alpha()
sem3 = pygame.image.load(os.path.join(assets_folder, "sem_verm.png")).convert_alpha()
sem4 = pygame.image.load(os.path.join(assets_folder, "sem_verm.png")).convert_alpha()
sem_verm = pygame.image.load(os.path.join(assets_folder, "sem_verm.png")).convert_alpha()
sem_verd = pygame.image.load(os.path.join(assets_folder, "sem_verd.png")).convert_alpha()
carro = pygame.image.load(os.path.join(assets_folder, "carro.png")).convert_alpha()
carro2 = pygame.transform.rotate(carro, 180)
carro3 = pygame.transform.rotate(carro, -90)
carro4 = pygame.transform.rotate(carro, 90)

# Redimensionar os sprites
novo_largura_sem, novo_altura_sem = 100, 100
novo_largura_carro, novo_altura_carro = 25, 56
sem1 = pygame.transform.scale(sem1, (novo_largura_sem, novo_altura_sem))
sem2 = pygame.transform.scale(sem2, (novo_largura_sem, novo_altura_sem))
sem3 = pygame.transform.scale(sem3, (novo_largura_sem, novo_altura_sem))
sem4 = pygame.transform.scale(sem4, (novo_largura_sem, novo_altura_sem))
sem_verm = pygame.transform.scale(sem_verm, (novo_largura_sem, novo_altura_sem))
sem_verd = pygame.transform.scale(sem_verd, (novo_largura_sem, novo_altura_sem))
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

# Retângulos de colisão para as faixas
faixa1_rect = pygame.Rect(230, 360, 2, 50)
faixa2_rect = pygame.Rect(290, 265, 50, 2)
faixa3_rect = pygame.Rect(470, 300, 2, 50)
faixa4_rect = pygame.Rect(355, 474, 50, 2)

# Variáveis para controlar a visibilidade das faixas
faixa1_visivel = False
faixa2_visivel = False
faixa3_visivel = False
faixa4_visivel = False

# Controle de tempo para gerar novos carros
tempo_para_novo_carro = 1000
tempo_acumulado = 0

# Adicione uma velocidade para cada carro
velocidades = {carro: 1, carro2: 1, carro3: 1, carro4: 1}

clock = pygame.time.Clock()

# Lista de sprites dos semáforos e suas posições
sprites = [
    (sem1 if faixa1_visivel else sem_verd, (100, 450)),
    (sem2 if faixa2_visivel else sem_verd, (200, 150)),
    (sem3 if faixa3_visivel else sem_verd, (500, 150)),
    (sem4 if faixa4_visivel else sem_verd, (400, 450))
]

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for sprite, pos in sprites:
                if sprite in (sem_verd, sem_verm, sem1, sem2, sem3, sem4):
                    sem_rect = pygame.Rect(pos, (novo_largura_sem, novo_altura_sem))
                    if sem_rect.collidepoint(x, y):
                        if pos == (100, 450):
                            faixa1_visivel = not faixa1_visivel
                        elif pos == (200, 150):
                            faixa2_visivel = not faixa2_visivel
                        elif pos == (500, 150):
                            faixa3_visivel = not faixa3_visivel
                        elif pos == (400, 450):
                            faixa4_visivel = not faixa4_visivel

    if not game_over:
        tempo_passado = pygame.time.get_ticks()
        tempo_decorrido = tempo_passado - tempo_acumulado

        # Atualizar a posição dos carros existentes
        for i, (sprite, pos) in enumerate(sprites):
            if sprite in (carro, carro2, carro3, carro4):
                velocidade_carro = velocidades[sprite]
                if sprite == carro or sprite == carro2:
                    nova_posicao = (pos[0], pos[1] + velocidade_carro)
                elif sprite == carro3:
                    nova_posicao = (pos[0] - velocidade_carro, pos[1])
                elif sprite == carro4:
                    nova_posicao = (pos[0] + velocidade_carro, pos[1])
                sprites[i] = (sprite, nova_posicao)

                if sprite in (carro, carro2):
                    rect_carro = pygame.Rect(nova_posicao, (novo_largura_carro, novo_altura_carro))
                else:
                    rect_carro = pygame.Rect(nova_posicao, (novo_altura_carro, novo_largura_carro))

                if faixa1_visivel and rect_carro.colliderect(faixa1_rect):
                    velocidades[sprite] = 0
                elif faixa2_visivel and rect_carro.colliderect(faixa2_rect):
                    velocidades[sprite] = 0
                elif faixa3_visivel and rect_carro.colliderect(faixa3_rect):
                    velocidades[sprite] = 0
                elif faixa4_visivel and rect_carro.colliderect(faixa4_rect):
                    velocidades[sprite] = 0
                else:
                    velocidades[sprite] = 1

                for j, (outro_sprite, outra_pos) in enumerate(sprites[i+1:], start=i+1):
                    if outro_sprite in (carro, carro2, carro3, carro4):
                        if outro_sprite in (carro, carro2):
                            rect_outro_carro = pygame.Rect(outra_pos, (novo_largura_carro, novo_altura_carro))
                        else:
                            rect_outro_carro = pygame.Rect(outra_pos, (novo_altura_carro, novo_largura_carro))
                        if rect_carro.colliderect(rect_outro_carro):
                            game_over = True
                            break

        # Controle de tempo para gerar novos carros
        if tempo_decorrido > tempo_para_novo_carro:
            novo_sprite, nova_posicao = random.choice(carros)
            sprites.append((novo_sprite, nova_posicao))
            tempo_acumulado = tempo_passado

        sprites = [(sprite, pos) for (sprite, pos) in sprites if 0 <= pos[0] <= width and 0 <= pos[1] <= height]

        screen.blit(background, (0, 0))

        for sprite, pos in sprites:
            screen.blit(sprite, pos)

        if faixa1_visivel:
            pygame.draw.rect(screen, (0, 0, 255), faixa1_rect)
        if faixa2_visivel:
            pygame.draw.rect(screen, (0, 0, 255), faixa2_rect)
        if faixa3_visivel:
            pygame.draw.rect(screen, (0, 0, 255), faixa3_rect)
        if faixa4_visivel:
            pygame.draw.rect(screen, (0, 0, 255), faixa4_rect)

    else:
        screen.blit(game_over_image, game_over_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_over = False
                tempo_acumulado = pygame.time.get_ticks()

    pygame.display.flip()

    clock.tick(60)