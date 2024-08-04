import pygame
from tetronimoes import Tetromino

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Tetris')


tetromino = Tetromino('I', 120, 140)  # Create a T-shaped tetromino at position (5, 5)

background = pygame.image.load("assets/background.png")

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                tetromino.rotate()
                tetromino.adjust_position_after_rotation(left_bound=100, right_bound=300)
                tetromino.print_blocks()

    tetromino.handle_input()

    screen.blit(background, (0,0))

    pygame.draw.rect(screen, "blue", (90, 90, 221, 420))

    pygame.draw.rect(screen, "black", (100, 100, 200, 400))

    for x in range(100, 300, 20):
        pygame.draw.line(screen, "white", (x,100), (x,499))
    for y in range(100, 500, 20):
        pygame.draw.line(screen, "white", (100,y), (299,y))

    pygame.draw.line(screen, "white", (299,100), (299,499))
    pygame.draw.line(screen, "white", (100,499), (299,499))

    for x, y in tetromino.get_blocks():
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()