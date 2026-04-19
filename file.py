import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 100
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100
FPS = 60

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Car Racing Game')

# Load images
car_image = pygame.image.load('car.png')  # Add your own car image
obstacle_image = pygame.image.load('obstacle.png')  # Add your own obstacle image
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))
obstacle_image = pygame.transform.scale(obstacle_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

# Game variables
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10
obstacles = []
score = 0
clock = pygame.time.Clock()

def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    return [x, 0]  # Start at top of screen

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle[0], obstacle[1]))

def handle_collisions(car_rect, obstacles):
    for obstacle in obstacles:
        if car_rect.colliderect(pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT)):
            return True
    return False

running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - CAR_WIDTH:
        car_x += 5

    # Create new obstacles
    if random.randint(1, 30) == 1:  # Adjust frequency
        obstacles.append(create_obstacle())
    
    # Move obstacles down
    for obstacle in obstacles:
        obstacle[1] += 5
        if obstacle[1] > SCREEN_HEIGHT:
            obstacles.remove(obstacle)
            score += 1  # Increase score for avoiding a car
    
    draw_obstacles(obstacles)
    screen.blit(car_image, (car_x, car_y))
    
    # Check for collisions
    if handle_collisions(pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT), obstacles):
        print("Game Over! Score: ", score)
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
