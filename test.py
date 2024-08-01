import pygame

# Define Tetromino Shapes and their rotations
i_shape = [
    [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0]]
]

square_shape = [
    [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]],
]

t_shape = [
    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    
    [[0, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],

    [[0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],
    
    [[0, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]]
]

l_shape = [
    [[0, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]],
    
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0]],
     
    [[1, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    
    [[0, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]]
]

reverse_l_shape = [
    [[0, 0, 0, 0],
     [1, 1, 1, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 0]],
    
    [[1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],
     
    [[0, 0, 1, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
    
    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]]
]

bolt_shape = [
    [[0, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]],
    
    [[0, 1, 1, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
]

reverse_bolt_shape = [
    [[0, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],
    
    [[1, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
]
# Tetromino class to handle shapes, positions, and rotations
class Tetromino:
    def __init__(self, shape, x=0, y=0):
        self.shape = shape
        self.x = x
        self.y = y
        self.rotation = 0
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)
    
    def get_current_shape(self):
        return self.shape[self.rotation]

# Function to draw the Tetromino
def draw_tetromino(surface, tetromino, block_size):
    shape = tetromino.get_current_shape()
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    surface,
                    (255, 255, 255),  # White color
                    pygame.Rect(
                        (tetromino.x + x) * block_size,
                        (tetromino.y + y) * block_size,
                        block_size,
                        block_size
                    )
                )

# Function to handle user input for moving and rotating the Tetromino
def handle_input(tetromino):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tetromino.x -= 1
    if keys[pygame.K_RIGHT]:
        tetromino.x += 1
    if keys[pygame.K_DOWN]:
        tetromino.y += 1
    if keys[pygame.K_UP]:
        tetromino.rotate()

# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 600))
    clock = pygame.time.Clock()
    block_size = 30

    tetromino = Tetromino(reverse_bolt_shape, x=3, y=0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input(tetromino)

        screen.fill((0, 0, 0))  # Clear the screen
        draw_tetromino(screen, tetromino, block_size)
        
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
