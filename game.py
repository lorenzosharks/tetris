import pygame
from tetronimoes import Tetromino, draw_tetromino, handle_input, shapes


# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
running = True

current_tetromino = Tetromino(shapes.l_shape, x=100, y=100)

background = pygame.image.load("assets/background.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input(current_tetromino)

    screen.blit(background, (0,0))

    pygame.draw.rect(screen, "blue", (90, 90, 221, 540))

    pygame.draw.rect(screen, "black", (100, 100, 200, 520))

    for x in range(100, 300, 20):
        pygame.draw.line(screen, "white", (x,100), (x,619))
    for y in range(100, 620, 20):
        pygame.draw.line(screen, "white", (100,y), (299,y))

    pygame.draw.line(screen, "white", (299,100), (299,619))
    pygame.draw.line(screen, "white", (100,619), (299,619))


    draw_tetromino(screen, current_tetromino, 20)  # Draw current Tetromino


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()