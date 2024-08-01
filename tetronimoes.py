import pygame
import time

# Class to define Tetromino shapes
class shapes:
    i_shape = [
        [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        
        [[1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0],
         [1, 0, 0, 0]]
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

    reverse_l_shape = [
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

    l_shape = [
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
        [[0, 1, 1, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        
        [[1, 0, 0, 0],
         [1, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
    ]

    reverse_bolt_shape = [
        [[1, 1, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        
        [[0, 0, 1, 0],
         [0, 1, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0]]
    ]

    @classmethod
    def get_shape(cls, shape_name):
        return getattr(cls, shape_name, None)

# Tetromino class to handle shapes, positions, and rotations
# class Tetromino:
#     def __init__(self, shape, x=0, y=0):
#         self.shape = shape
#         self.x = x
#         self.y = y
#         self.rotation = 0
#         self.last_rotation_time = time.time()  # Initialize with the current time
#         self.rotation_delay = 0.5  # Rotation delay in seconds
    
#     def rotate(self):
#         current_time = time.time()
#         if current_time - self.last_rotation_time > self.rotation_delay:
#             self.rotation = (self.rotation + 1) % len(self.shape)
#             self.last_rotation_time = current_time  # Update the last rotation time
    
#     def get_current_shape(self):
#         return self.shape[self.rotation]

class Tetromino:
    def __init__(self, shape, x=0, y=0):
        self.shape = shape
        self.x = x
        self.y = y
        self.rotation = 0
        self.last_rotation_time = time.time()
        self.rotation_delay = 0.5
        self.last_move_down_time = pygame.time.get_ticks()
        self.drop_speed = 500
    
    def rotate(self):
        new_rotation = (self.rotation + 1) % len(self.shape)
        if self.can_move(dx=0, dy=0, new_rotation=new_rotation):
            self.rotation = new_rotation
    
    def move_down(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_down_time > self.drop_speed:
            if self.can_move(dx=0, dy=20):
                self.y += 20
                self.last_move_down_time = current_time
    
    def get_current_shape(self):
        return self.shape[self.rotation]
    
    def can_move(self, dx=0, dy=0, new_rotation=None):
        if new_rotation is None:
            new_rotation = self.rotation
        
        shape = self.shape[new_rotation]
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.x + x * 20 + dx
                    new_y = self.y + y * 20 + dy
                    if new_x < 100 or new_x >= 100 + 300:
                        return False
                    if new_y >= 100 + 520:
                        return False
        return True

    
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
                        tetromino.x + x * block_size,
                        tetromino.y + y * block_size,
                        block_size,
                        block_size
                    )
                )

# Function to handle user input for moving and rotating the Tetromino
def handle_input(tetromino):
    keys = pygame.key.get_pressed()
    if not tetromino.x < 100:
        if keys[pygame.K_LEFT]:
            tetromino.x -= 20

    if not tetromino.x > 300:
        if keys[pygame.K_RIGHT]:
            tetromino.x += 20

    if keys[pygame.K_DOWN]:
        tetromino.y += 20

    if keys[pygame.K_UP]:
        tetromino.rotate()
