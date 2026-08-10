import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

snake = [(300, 200)]
direction = (20, 0)

food = (
    random.randrange(0, WIDTH, 20),
    random.randrange(0, HEIGHT, 20)
)

clock = pygame.time.Clock()
running = True
score = 0

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                direction = (0, -20)

            elif event.key == pygame.K_DOWN:
                direction = (0, 20)

            elif event.key == pygame.K_LEFT:
                direction = (-20, 0)

            elif event.key == pygame.K_RIGHT:
                direction = (20, 0)

    head_x, head_y = snake[0]

    new_head = (
        head_x + direction[0],
        head_y + direction[1]
    )

    snake.insert(0, new_head)

    if new_head == food:

        score += 1

        food = (
            random.randrange(0, WIDTH, 20),
            random.randrange(0, HEIGHT, 20)
        )

    else:
        snake.pop()

    if (
        new_head[0] < 0 or
        new_head[0] >= WIDTH or
        new_head[1] < 0 or
        new_head[1] >= HEIGHT
    ):
        running = False

    if new_head in snake[1:]:
        running = False

    screen.fill(BLACK)

    for part in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (part[0], part[1], 20, 20)
        )

    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], 20, 20)
    )

    # Score
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

    clock.tick(10)

pygame.quit()