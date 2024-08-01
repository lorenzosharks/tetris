import pygame
from tetronimoes import Tetromino, draw_tetromino, handle_input, shapes

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
running = True

# Constants

current_tetromino = Tetromino(shapes.i_shape, x=100, y=100)

background = pygame.image.load("assets/background.png")

def handle_input(tetromino):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if can_move(tetromino, dx=-20):
            tetromino.x -= 20
    if keys[pygame.K_RIGHT]:
        if can_move(tetromino, dx=20):
            tetromino.x += 20
    if keys[pygame.K_DOWN]:
        if can_move(tetromino, dy=20):
            tetromino.y += 20
    if keys[pygame.K_UP]:
        tetromino.rotate()

def can_move(tetromino, dx=0, dy=0):
    for y, row in enumerate(tetromino.get_current_shape()):
        for x, cell in enumerate(row):
            if cell:
                new_x = tetromino.x + x * 20 + dx
                new_y = tetromino.y + y * 20 + dy
                if new_x < 100 or new_x >= 100 + 200:
                    return False
                if new_y >= 100 + 520:
                    return False
    return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input(current_tetromino)

    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, "blue", (100 - 10, 100 - 10, 200 + 21, 520 + 20))

    pygame.draw.rect(screen, "black", (100, 100, 200, 520))

    for x in range(100, 100 + 200, 20):
        pygame.draw.line(screen, "white", (x, 100), (x, 100 + 520))
    for y in range(100, 100 + 520, 20):
        pygame.draw.line(screen, "white", (100, y), (100 + 200, y))

    draw_tetromino(screen, current_tetromino, 20)  # Draw current Tetromino

    pygame.display.flip()

    clock.tick(10)  # limits FPS to 10

pygame.quit()
