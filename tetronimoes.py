import pygame

# Define Tetromino shapes using relative coordinates, converted to pixels
TETROMINOES = {
    'T': [(0, 0), (-20, 0), (20, 0), (0, -20)],
    'O': [(0, 0), (0, -20), (20, 0), (20, -20)],
    'J': [(0, 0), (-20, 0), (0, -20), (0, -2*20)],
    'L': [(0, 0), (20, 0), (0, -20), (0, -2*20)],
    'I': [(0, 0), (0, 20), (0, -20), (0, -2*20)],
    'S': [(0, 0), (-20, 0), (0, -20), (20, -20)],
    'Z': [(0, 0), (20, 0), (0, -20), (-20, -20)]
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

    def print_blocks(self):
        print("Tetromino blocks at rotation {}: {}".format(self.rotation, self.get_blocks()))
        print(type(self.get_blocks()))
        blocks = self.get_blocks()
        print(blocks[1])

# Function to handle user input for moving and rotating the Tetromino
def handle_input(tetromino):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        tetromino.x -= 20
    if keys[pygame.K_RIGHT]:
        tetromino.x += 20
    if keys[pygame.K_DOWN]:
        tetromino.y += 20
    if keys[pygame.K_UP]:
        tetromino.rotate()
        tetromino.print_blocks()