import pygame
from tetronimoes import Tetromino, create_new_tetromino, check_collision, merge_tetromino

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Tetris')

fixed_blocks = set()
tetromino = create_new_tetromino()
background = pygame.image.load("assets/background.png")

fall = True
start = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                tetromino.rotate()

    tetromino.handle_input(fixed_blocks)

    if fall:
        if not tetromino.can_move_down(fixed_blocks):
            merge_tetromino(tetromino, fixed_blocks)
            tetromino = create_new_tetromino()
            while check_collision(tetromino, fixed_blocks):
                tetromino.y -= 20  # Adjust position if the new Tetromino collides immediately
        else:
            tetromino.y += 20

        fall = False
        start = pygame.time.get_ticks()

    if not fall:
        second_start = pygame.time.get_ticks()
        elapsed = second_start - start
        if elapsed > 500:
            fall = True

    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, "blue", (90, 90, 221, 420))
    pygame.draw.rect(screen, "black", (100, 100, 200, 400))

    for x in range(100, 300, 20):
        pygame.draw.line(screen, "white", (x, 100), (x, 499))
    for y in range(100, 500, 20):
        pygame.draw.line(screen, "white", (100, y), (299, y))

    pygame.draw.line(screen, "white", (299, 100), (299, 499))
    pygame.draw.line(screen, "white", (100, 499), (299, 499))

    for x, y in fixed_blocks:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))

    for x, y in tetromino.get_blocks():
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))

    pygame.display.flip()
    clock.tick(10)  # limits FPS to 60

pygame.quit()
