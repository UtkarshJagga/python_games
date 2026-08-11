
import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

BLACK = (15, 15, 20)
DARK_GREEN = (0, 120, 60)
GREEN = (0, 200, 100)
LIGHT_GREEN = (80, 255, 150)

RED = (220, 50, 50)
LIGHT_RED = (255, 100, 100)

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (30, 30, 35)
YELLOW = (255, 220, 50)

font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 70)
medium_font = pygame.font.Font(None, 45)

snake = []
direction = (CELL_SIZE, 0)
next_direction = direction

food = None

score = 0
high_score = 0

game_state = "START"

def create_food():
    """Create food at a position not occupied by the snake."""

    while True:

        position = (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
        )

        if position not in snake:
            return position


def reset_game():
    """Reset the game."""

    global snake
    global direction
    global next_direction
    global food
    global score

    snake = [
        (300, 200),
        (280, 200),
        (260, 200)
    ]

    direction = (CELL_SIZE, 0)
    next_direction = direction

    score = 0

    food = create_food()


def draw_grid():
    """Draw background grid."""

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen,
            DARK_GRAY,
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(
            screen,
            DARK_GRAY,
            (0, y),
            (WIDTH, y)
        )


def draw_snake():
    """Draw the snake."""

    for index, part in enumerate(snake):

        x, y = part

        if index == 0:

            # Snake head
            pygame.draw.rect(
                screen,
                LIGHT_GREEN,
                (x, y, CELL_SIZE, CELL_SIZE),
                border_radius=5
            )

            # Eyes
            pygame.draw.circle(
                screen,
                BLACK,
                (x + 6, y + 6),
                2
            )

            pygame.draw.circle(
                screen,
                BLACK,
                (x + 14, y + 6),
                2
            )

        else:

            pygame.draw.rect(
                screen,
                GREEN,
                (x, y, CELL_SIZE, CELL_SIZE),
                border_radius=4
            )


def draw_food():
    """Draw the food."""

    x, y = food

  
    pygame.draw.circle(
        screen,
        RED,
        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
        9
    )

    pygame.draw.circle(
        screen,
        LIGHT_RED,
        (x + 7, y + 6),
        3
    )


def draw_score():
    """Display score."""

    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    high_score_text = font.render(
        f"High Score: {high_score}",
        True,
        YELLOW
    )

    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 35))


def draw_start_screen():
    """Display start screen."""

    screen.fill(BLACK)

    title = big_font.render(
        "SNAKE",
        True,
        LIGHT_GREEN
    )

    instruction = medium_font.render(
        "Press SPACE to Start",
        True,
        WHITE
    )

    controls = font.render(
        "Arrow Keys / WASD to move",
        True,
        GRAY
    )

    screen.blit(
        title,
        title.get_rect(center=(WIDTH // 2, 120))
    )

    screen.blit(
        instruction,
        instruction.get_rect(center=(WIDTH // 2, 220))
    )

    screen.blit(
        controls,
        controls.get_rect(center=(WIDTH // 2, 270))
    )


def draw_game_over():
    """Display game over screen."""

    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)

    screen.blit(overlay, (0, 0))

    game_over = big_font.render(
        "GAME OVER",
        True,
        RED
    )

    score_text = medium_font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    restart_text = font.render(
        "Press R to Restart",
        True,
        LIGHT_GREEN
    )

    quit_text = font.render(
        "Press ESC to Quit",
        True,
        GRAY
    )

    screen.blit(
        game_over,
        game_over.get_rect(center=(WIDTH // 2, 120))
    )

    screen.blit(
        score_text,
        score_text.get_rect(center=(WIDTH // 2, 190))
    )

    screen.blit(
        restart_text,
        restart_text.get_rect(center=(WIDTH // 2, 250))
    )

    screen.blit(
        quit_text,
        quit_text.get_rect(center=(WIDTH // 2, 290))
    )

reset_game()

running = True


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_state == "START":

                if event.key == pygame.K_SPACE:
                    reset_game()
                    game_state = "PLAYING"
            elif game_state == "PLAYING":

                if event.key in (pygame.K_UP, pygame.K_w):

                    if direction != (0, CELL_SIZE):
                        next_direction = (0, -CELL_SIZE)

                elif event.key in (pygame.K_DOWN, pygame.K_s):

                    if direction != (0, -CELL_SIZE):
                        next_direction = (0, CELL_SIZE)

                elif event.key in (pygame.K_LEFT, pygame.K_a):

                    if direction != (CELL_SIZE, 0):
                        next_direction = (-CELL_SIZE, 0)

                elif event.key in (pygame.K_RIGHT, pygame.K_d):

                    if direction != (-CELL_SIZE, 0):
                        next_direction = (CELL_SIZE, 0)

                elif event.key == pygame.K_p:

                    game_state = "PAUSED"

            elif game_state == "PAUSED":

                if event.key == pygame.K_p:
                    game_state = "PLAYING"

            elif game_state == "GAME_OVER":

                if event.key == pygame.K_r:

                    reset_game()
                    game_state = "PLAYING"

                elif event.key == pygame.K_ESCAPE:

                    running = False

    if game_state == "PLAYING":

        direction = next_direction

        head_x, head_y = snake[0]

        new_head = (
            head_x + direction[0],
            head_y + direction[1]
        )

        snake.insert(0, new_head)

        if new_head == food:

            score += 1

            if score > high_score:
                high_score = score

            food = create_food()

        else:

            snake.pop()

        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
        ):

            game_state = "GAME_OVER"


        if new_head in snake[1:]:

            game_state = "GAME_OVER"

    if game_state == "START":

        draw_start_screen()

    else:

        screen.fill(BLACK)

        draw_grid()

        draw_snake()
        draw_food()
        draw_score()

        if game_state == "PAUSED":

            pause_text = big_font.render(
                "PAUSED",
                True,
                YELLOW
            )

            instruction = font.render(
                "Press P to Continue",
                True,
                WHITE
            )

            screen.blit(
                pause_text,
                pause_text.get_rect(
                    center=(WIDTH // 2, 170)
                )
            )

            screen.blit(
                instruction,
                instruction.get_rect(
                    center=(WIDTH // 2, 230)
                )
            )

        elif game_state == "GAME_OVER":

            draw_game_over()

    pygame.display.update()

    if game_state == "PLAYING":

        speed = min(20, 10 + score // 3)

        clock.tick(speed)

    else:

        clock.tick(30)


pygame.quit()

