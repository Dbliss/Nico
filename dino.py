import pygame
import sys
import random

# Pygame initialization
pygame.init() 

# Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 200
FPS = 60
SCORE_FONT = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (89, 108, 112)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (82, 184, 42)
DARK_RED = (61, 10, 7)
LIGHT_BLUE = (0, 217, 255)
DARK_BLUE = (0, 16, 54)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_JUMP_VELOCITY = -10
PLAYER_GRAVITY = 0.5

# Obstacle settings
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_VELOCITY = 5

jumped_once = True

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Dash")

def draw_player(player_rect):
    pygame.draw.rect(screen, YELLOW, player_rect)

def draw_obstacle(obstacle_rect):
    pygame.draw.rect(screen, GREY, obstacle_rect)

def check_collision(player_rect, obstacles):
    for obstacle_rect in obstacles:
        if player_rect.colliderect(obstacle_rect):
            return True
    return False


def main():
    OBSTACLE_VELOCITY = 5
    SKY_COLOUR = (0, 217, 255)
    FLOOR_COLOUR = (82, 184, 42)
    
    LIGHT_BLUE = (0, 217, 255)
    DARK_BLUE = (0, 16, 54)
    
    LIGHT_GREEN = (82, 184, 42)
    DARK_RED = (61, 10 ,7)

    player_x = 100
    player_y = SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT
    player_velocity = 0

    obstacles = []
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_y == SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT:
                        player_velocity = PLAYER_JUMP_VELOCITY
                    elif player_y > GROUND_HEIGHT and jumped_once:
                        player_velocity = PLAYER_JUMP_VELOCITY
                        jumped_once = False

        # Update player position
        player_y += player_velocity
        player_velocity += PLAYER_GRAVITY
        if player_y > SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT:
            player_y = SCREEN_HEIGHT - GROUND_HEIGHT - PLAYER_HEIGHT
            player_velocity = 0
            jumped_once = True

        # Create ground obstacles at regular intervals
        if random.randint(1, 200) == 1:
            obstacle_x = SCREEN_WIDTH
            obstacle_y = SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        # Create flying obstacles at regular intervals
        if random.randint(1, 100) == 1:
            OBSTACLE_VELOCITY += 0.2
            if OBSTACLE_VELOCITY < 6:
                LIGHT_BLUE = (0, 217, 255)
                FLOOR_COLOUR = (82, 184, 42)
            elif OBSTACLE_VELOCITY < 10:
                LIGHT_BLUE = (0, 101, 150)
                FLOOR_COLOUR = (70, 95, 20)
            else:
                LIGHT_BLUE = (0, 16, 54)
                FLOOR_COLOUR = (50, 75, 10)
            flying_height = random.randint(OBSTACLE_HEIGHT, GROUND_HEIGHT)
            obstacle_x = SCREEN_WIDTH
            obstacle_y = SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT
            obstacles.append(pygame.Rect(obstacle_x, flying_height, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        # Move obstacles
        for obstacle in obstacles[:]:
            obstacle.x -= OBSTACLE_VELOCITY
            if obstacle.right < 0:
                obstacles.remove(obstacle)

        players = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Check for collisions
        if check_collision(players, obstacles):
            pygame.quit()
            sys.exit()

        # Draw everything
        screen.fill(LIGHT_BLUE)
        draw_player(players)
        for obstacle in obstacles:
            draw_obstacle(obstacle)

        # Draw ground
        pygame.draw.rect(screen, FLOOR_COLOUR, pygame.Rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))


        # Inside the game loop, after updating the screen
        score_text = SCORE_FONT.render(f"Score: {OBSTACLE_VELOCITY*10- 50}", True, WHITE)
        screen.blit(score_text, (10, 10))  # Display the score at (10, 10) on the screen

        pygame.display.flip()
        clock.tick(FPS)
        
        

if __name__ == "__main__":
    main()