import pygame

# Define Tetromino shapes using relative coordinates, converted to pixels
TETROMINOES = {
    'T': [(0, 0), (-20, 0), (20, 0), (0, -20)],
    'O': [(0, 0), (0, -20), (20, 0), (20, -20)],
    'J': [(0, 0), (-20, 0), (0, -20), (0, -40)],
    'L': [(0, 0), (20, 0), (0, -20), (0, -40)],
    'I': [(0, 0), (0, 20), (0, -20), (0, -40)],
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

    def get_leftmost_coordinate(self):
        blocks = self.get_blocks()
        min_x = min(block[0] for block in blocks)
        return min_x

    def get_rightmost_coordinate(self):
        blocks = self.get_blocks()
        max_x = max(block[0] for block in blocks) + 20
        return max_x
    
    def adjust_position_after_rotation(self, left_bound, right_bound):
        leftmost = self.get_leftmost_coordinate()
        rightmost = self.get_rightmost_coordinate()

        if leftmost < left_bound:
            self.x += (left_bound - leftmost)
        elif rightmost > right_bound:
            self.x -= (rightmost - right_bound)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.get_leftmost_coordinate() > 100:
            self.x -= 20

        if keys[pygame.K_RIGHT] and self.get_rightmost_coordinate() < 300:
            self.x += 20

        if keys[pygame.K_DOWN]:
            self.y += 20

        pause = False

    def print_blocks(self):
        blocks = self.get_blocks()
        print(blocks[1])
        print(self.get_leftmost_coordinate())
        print(self.get_rightmost_coordinate())
