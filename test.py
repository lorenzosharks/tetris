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
    tetromino = Tetromino(shape, 120, 0)
    if check_collision(tetromino, fixed_blocks):
        return None  # Indicates game over
    return tetromino


def check_collision(tetromino, fixed_blocks):
    for x, y in tetromino.get_blocks():
        if x < 100 or x >= 300 or y >= 70:
            return True
        if (x, y) in fixed_blocks:
            return True
    return False

def merge_tetromino(tetromino, fixed_blocks):
    for x, y in tetromino.get_blocks():
        fixed_blocks.add((x, y))

def clear_full_rows(fixed_blocks):
    # Determine the full rows
    rows = set(y for x, y in fixed_blocks)
    full_rows = set()
    for row in rows:
        if all((x, row) in fixed_blocks for x in range(100, 300, 20)):
            full_rows.add(row)
    
    if not full_rows:
        return  # No full rows to clear

    # Number of rows cleared
    lines_cleared = len(full_rows)

    # Remove all blocks in full rows
    for row in full_rows:
        fixed_blocks.difference_update({(x, row) for x in range(100, 300, 20)})

    # Shift down all blocks above the cleared rows
    for x, y in list(fixed_blocks):
        if y < min(full_rows):
            fixed_blocks.remove((x, y))
            fixed_blocks.add((x, y + 20 * lines_cleared))

# pygame setup
# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 760))  # Increase height for the scoreboard
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Tetris')

fixed_blocks = set()
tetromino = create_new_tetromino()
background = pygame.image.load("assets/background.png")

fall = True
start = pygame.time.get_ticks()

score = 0  # Initialize score

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                tetromino.rotate()

    if tetromino is None:
        # Handle game over
        print(f"Game Over! Final Score: {score}")
        running = False
        continue

    tetromino.handle_input(fixed_blocks)

    if fall:
        if not tetromino.can_move_down(fixed_blocks):
            merge_tetromino(tetromino, fixed_blocks)
            lines_cleared = len([row for row in range(100, 500, 20) if all((x, row) in fixed_blocks for x in range(100, 300, 20))])
            score += lines_cleared * 100  # Increase score based on the number of rows cleared
            clear_full_rows(fixed_blocks)  # Clear full rows and shift blocks down
            tetromino = create_new_tetromino()
            if tetromino is None:
                # Handle game over if the new Tetromino collides immediately
                print(f"Game Over! Final Score: {score}")
                running = False
                continue
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

    # Draw the scoreboard area
    pygame.draw.rect(screen, "black", (0, 620, 400, 140))  # Scoreboard background
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (150, 650))  # Display the score text

    pygame.display.flip()
    clock.tick(10)  # limits FPS to 60

pygame.quit()
