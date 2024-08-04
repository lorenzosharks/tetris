import pygame
import random

# Define Tetromino shapes using relative coordinates, converted to pixels
TETROMINOES = {
    'T': [(0, 0), (-20, 0), (20, 0), (0, -20)],
    'O': [(0, 0), (0, -20), (20, 0), (20, -20)],
    'J': [(0, 0), (-20, 0), (0, -20), (0, -40)],
    'L': [(0, 0), (20, 0), (0, -20), (0, -40)],
    'I': [(0, 0), (0, 20), (0, -20), (0, -40)],  # Vertical orientation initially
    'S': [(0, 0), (-20, 0), (0, -20), (20, -20)],
    'Z': [(0, 0), (20, 0), (0, -20), (-20, -20)]
}

# Class for handling Tetromino blocks
class Tetromino:
    def __init__(self, shape, x, y):
        self.shape = TETROMINOES[shape]
        self.original_shape = TETROMINOES[shape]
        self.x = x
        self.y = y
        self.rotation = 0

    def get_blocks(self):
        return [(self.x + dx, self.y + dy) for dx, dy in self.shape]

    def rotate(self):
        if self.shape != TETROMINOES['O']:  # 'O' shape doesn't need rotation
            self.shape = [(dy, -dx) for dx, dy in self.shape]
            self.rotation = (self.rotation + 1) % 4
            self.adjust_position_after_rotation()

    def get_leftmost_coordinate(self):
        blocks = self.get_blocks()
        min_x = min(block[0] for block in blocks)
        return min_x

    def get_rightmost_coordinate(self):
        blocks = self.get_blocks()
        max_x = max(block[0] for block in blocks)
        return max_x

    def get_bottommost_coordinate(self):
        blocks = self.get_blocks()
        max_y = max(block[1] for block in blocks)
        return max_y

    def adjust_position_after_rotation(self):
        leftmost = self.get_leftmost_coordinate()
        rightmost = self.get_rightmost_coordinate()
        bottommost = self.get_bottommost_coordinate()

        if leftmost < 100:
            self.x += (100 - leftmost)
        elif rightmost > 280:
            self.x -= (rightmost - 280)

        if bottommost >= 500:
            self.y -= (bottommost - 500 + 20)  # Move up if it goes below the screen

    def can_move_left(self, fixed_blocks):
        for x, y in self.get_blocks():
            if x <= 100 or (x - 20, y) in fixed_blocks:
                return False
        return True

    def can_move_right(self, fixed_blocks):
        for x, y in self.get_blocks():
            if x >= 280 or (x + 20, y) in fixed_blocks:
                return False
        return True

    def can_move_down(self, fixed_blocks):
        for x, y in self.get_blocks():
            if (x, y + 20) in fixed_blocks or y + 20 >= 500:
                return False
        return True

    def handle_input(self, fixed_blocks):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.can_move_left(fixed_blocks):
            self.x -= 20

        if keys[pygame.K_RIGHT] and self.can_move_right(fixed_blocks):
            self.x += 20

        if keys[pygame.K_DOWN] and self.can_move_down(fixed_blocks):
            self.y += 20

def create_new_tetromino():
    shapes = list(TETROMINOES.keys())
    shape = random.choice(shapes)
    return Tetromino(shape, 120, 0)

def check_collision(tetromino, fixed_blocks):
    for x, y in tetromino.get_blocks():
        if x < 100 or x >= 300 or y >= 500:
            return True
        if (x, y) in fixed_blocks:
            return True
    return False

def merge_tetromino(tetromino, fixed_blocks):
    for x, y in tetromino.get_blocks():
        fixed_blocks.add((x, y))