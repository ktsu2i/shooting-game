import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen dimensions
WIDTH = 480
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Shooting Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_img = pygame.Surface((50, 40))
player_img.fill((0, 255, 0))  # Green color
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10
player_speed = 5

# Bullet settings
bullet_img = pygame.Surface((5, 10))
bullet_img.fill((255, 0, 0))  # Red color
bullet_speed = -10  # Bullets move upward

# Enemy settings
enemy_img = pygame.Surface((30, 30))
enemy_img.fill((0, 0, 255))  # Blue color
enemy_speed = 3

# Lists to manage bullets and enemies
bullets = []
enemies = []

# Set the game's frame rate
clock = pygame.time.Clock()

# Function to spawn an enemy at a random x position above the screen
def spawn_enemy():
    enemy_rect = enemy_img.get_rect()
    enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)
    enemy_rect.y = random.randint(-100, -40)
    return enemy_rect

# Create initial enemies
for _ in range(5):
    enemies.append(spawn_enemy())

running = True
while running:
    clock.tick(240)  # 60 frames per second

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Process key inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed
    # Fire a bullet when the space key is pressed
    if keys[pygame.K_SPACE]:
        # Create a bullet at the player's current position
        bullet_rect = bullet_img.get_rect()
        bullet_rect.centerx = player_rect.centerx
        bullet_rect.bottom = player_rect.top
        bullets.append(bullet_rect)

    # Update bullets
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        # Remove the bullet if it moves off the screen
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Update enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        # If the enemy moves off the bottom of the screen, respawn it at the top
        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            enemies.append(spawn_enemy())

    # Check for collisions between bullets and enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies.append(spawn_enemy())
                break

    # Draw everything on the screen
    screen.fill(BLACK)
    screen.blit(player_img, player_rect)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    pygame.display.flip()

pygame.quit()
