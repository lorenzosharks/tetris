import pygame as pg

vec = pg.math.Vector2

# Define Tetromino shapes using relative coordinates
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

# Class for handling Tetromino blocks
class Tetromino:
    def __init__(self, shape, x, y):
        self.shape = TETROMINOES[shape]
        self.x = x
        self.y = y
        self.rotation = 0

    def get_blocks(self):
        return [(self.x + dx, self.y + dy) for dx, dy in self.shape]

    def rotate(self):
        if self.shape != TETROMINOES['O']:  # 'O' shape doesn't need rotation
            self.shape = [(dy, -dx) for dx, dy in self.shape]
            self.rotation = (self.rotation + 1) % 4

def handle_input(self):
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        self.x -= 1

    if keys[pg.K_RIGHT]:
        self.x += 1

    if keys[pg.K_DOWN]:
        self.y += 1

    if keys[pg.K_UP]:
        self.rotate()

# Initialize Pygame
pg.init()
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()

# Example usage of the Tetromino class
tetromino = Tetromino('I', 5, 5)  # Create a T-shaped tetromino at position (5, 5)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black
    for x, y in tetromino.get_blocks():
        pg.draw.rect(screen, (255, 255, 255), (x * 20, y * 20, 20, 20))  # Draw each block as a white square

    handle_input(tetromino)

    pg.display.flip()
    clock.tick(10)

pg.quit()