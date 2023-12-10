import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo cores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Definindo a largura e a altura da janela do jogo
WIDTH, HEIGHT = 800, 600

# Criando a janela do jogo
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Definindo a classe Car
class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = GRAY

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, 50, 20))

    def move(self):
        if self.direction == 'EAST':
            self.x += 5
        elif self.direction == 'WEST':
            self.x -= 5
        elif self.direction == 'NORTH':
            self.y -= 5
        elif self.direction == 'SOUTH':
            self.y += 5

# Definindo a classe Stoplight
class Stoplight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), 10)

    def change_color(self):
        if self.color == RED:
            self.color = GREEN
        else:
            self.color = RED

# Definindo a classe RoadLine
class RoadLine:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def draw(self):
        if self.orientation == 'HORIZONTAL':
            pygame.draw.line(WIN, (255, 255, 255), (self.x, self.y), (self.x + 100, self.y))
        else:
            pygame.draw.line(WIN, (255, 255, 255), (self.x, self.y), (self.x, self.y + 100))

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    run = True

    # Criando objetos
    roadlines = [RoadLine(230, -75, 'HORIZONTAL'), RoadLine(269, 2, 'VERTICAL'), RoadLine(139, -53, 'VERTICAL'), RoadLine(173, 51, 'HORIZONTAL')]
    stoplights = [Stoplight(-181, -59), Stoplight(-126, 161), Stoplight(106, 139), Stoplight(38, -80)]
    cars = []

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Desenhando objetos na tela
        WIN.fill((0, 0, 0))
        for roadline in roadlines:
            roadline.draw()
        for stoplight in stoplights:
            stoplight.draw()
        for car in cars:
            car.draw()
            car.move()

        # Criando novos carros
        if random.randint(0, 100) < 2:
            direction = random.choice(['EAST', 'WEST', 'NORTH', 'SOUTH'])
            if direction == 'EAST':
                cars.append(Car(-150, -66, direction))
            elif direction == 'WEST':
                cars.append(Car(200, 65, direction))
            elif direction == 'NORTH':
                cars.append(Car(52, -125, direction))
            elif direction == 'SOUTH':
                cars.append(Car(-74, 210, direction))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
