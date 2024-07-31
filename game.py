import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
running = True

background = pygame.image.load("assets/background.png")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))

    pygame.draw.rect(screen, "blue", (80, 80, 240, 560))

    pygame.draw.rect(screen, "black", (100, 100, 200, 520))

    for x in range(99, 301, 20):
        pygame.draw.line(screen, "white", (x,100), (x,619))
    for y in range(99, 620, 20):
        pygame.draw.line(screen, "white", (100,y), (299,y))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()