import pygame
import random
import math

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Grid dimensions
GRID_SIZE = 5
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE

# Ball dimensions
BALL_SIZE = CELL_SIZE // 2
HIDDEN_BALL_SIZE = CELL_SIZE // 4

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to create a new random position for the ball
def new_ball_position():
    return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)

# Function to check if two balls collide
def check_collision(ball1_pos, ball2_pos,):
    return manhattan_distance(ball1_pos, ball2_pos) == 0

# Function to calculate Manhattan distance between two points
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Main game loop
def main():
    # Initial ball positions
    user_ball_pos = [GRID_SIZE // 2, GRID_SIZE // 2]
    ball_pos = new_ball_position()

    # Main loop flag
    running = True

    # Game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                # Move the user's ball based on arrow key input
                if event.key == pygame.K_UP:
                    user_ball_pos[1] = max(0, user_ball_pos[1] - 1)
                elif event.key == pygame.K_DOWN:
                    user_ball_pos[1] = min(GRID_SIZE - 1, user_ball_pos[1] + 1)
                elif event.key == pygame.K_LEFT:
                    user_ball_pos[0] = max(0, user_ball_pos[0] - 1)
                elif event.key == pygame.K_RIGHT:
                    user_ball_pos[0] = min(GRID_SIZE - 1, user_ball_pos[0] + 1)

                # Move the hidden ball randomly
                direction = random.choice(['up', 'down', 'left', 'right'])
                if direction == 'up':
                    ball_pos = (ball_pos[0], max(0, ball_pos[1] - 1))
                elif direction == 'down':
                    ball_pos = (ball_pos[0], min(GRID_SIZE - 1, ball_pos[1] + 1))
                elif direction == 'left':
                    ball_pos = (max(0, ball_pos[0] - 1), ball_pos[1])
                elif direction == 'right':
                    ball_pos = (min(GRID_SIZE - 1, ball_pos[0] + 1), ball_pos[1])

        # Calculate the distance between user's ball and hidden ball
        distance = manhattan_distance(user_ball_pos, ball_pos)

        # Check for collision
        if manhattan_distance(user_ball_pos, ball_pos) == 0:
            print("You win!")
            running = False

        # Clear the screen
        screen.fill(BLACK)

        # Draw the grid
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)

        # Draw the user's ball
        pygame.draw.circle(screen, WHITE, (user_ball_pos[0] * CELL_SIZE + CELL_SIZE // 2, user_ball_pos[1] * CELL_SIZE + CELL_SIZE // 2), BALL_SIZE)

        # Draw the hidden ball
        pygame.draw.circle(screen, BLACK, (ball_pos[0] * CELL_SIZE + CELL_SIZE // 2, ball_pos[1] * CELL_SIZE + CELL_SIZE // 2), HIDDEN_BALL_SIZE)

        # Display the distance
        font = pygame.font.Font(None, 36)
        text = font.render("Distance: " + str(distance), True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)

    # Quit pygame
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
