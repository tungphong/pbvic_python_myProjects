import pygame
from random import randint

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
clock = pygame.time.Clock()

TUBE_WIDTH = 50
BLUE = (0, 0, 255)
TUBE_VELOCITY = 2
TUBE_GAP = 150

# Bird color
RED = (255, 0, 0)
BIRD_X = 50
bird_y = 400
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAViTY = 0.2


tube1_x = 0
tube2_x = 200
tube3_x = 400
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)
tube1_height = randint(100, 400)

while running:
    clock.tick(60)
    screen.fill(GREEN)

    # Draw tube
    pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

    # Draw tube inverse
    pygame.draw.rect(screen, BLUE, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - (TUBE_GAP - tube1_height)))
    pygame.draw.rect(screen, BLUE, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - (TUBE_GAP + tube2_height)))
    pygame.draw.rect(screen, BLUE, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - (TUBE_GAP + tube3_height)))

    # Move the tubes to the left
    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    # Draw a birst
    pygame.draw.rect(screen, RED, (BIRD_X, bird_y, BIRD_WIDTH, BIRD_HEIGHT))

    # Bird falling
    bird_y += bird_drop_velocity
    bird_drop_velocity += GRAViTY



    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
        tube1_height = randint(100, 400)
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
        tube2_height = randint(100, 400)
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550
        tube3_height = randint(100, 400)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()