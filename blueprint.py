import random
import time
import pygame
pygame.init()

window_x, window_y = 1080, 720
screen = (window_x, window_y)
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((window_x, window_y))
score = 0
clock = pygame.time.Clock()

step = 10
snake = [(200, 200), (190, 200), (180, 200), (170, 200)]
direction_x, direction_y = 1, 0
font = pygame.font.SysFont("Arial", 30)
change_to = (direction_x, direction_y)

fruit_x, fruit_y = random.randrange(
    0, window_x, step), random.randrange(0, window_y, step)
fruit_pos = (fruit_x, fruit_y)

state = "Playing"
running = True
while running:
    for event in pygame.event.get():
        if state == "Playing":
            if event.type == pygame.QUIT:
                state = "Game_Over"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "Game_Over"
                if event.key == pygame.K_UP:
                    if direction_y != 1:
                        change_to = 0, -1
                if event.key == pygame.K_DOWN:
                    if direction_y != -1:
                        change_to = 0, 1
                if event.key == pygame.K_RIGHT:
                    if direction_x != -1:
                        change_to = 1, 0
                if event.key == pygame.K_LEFT:
                    if direction_x != 1:
                        change_to = -1, 0
        elif state == "Game_Over":
            if event.key == pygame.K_r:
                score = 0
                change_to = (1, 0)
                snake = [(200, 200), (190, 200), (180, 200), (170, 200)]
                direction_x, direction_y = 1, 0
                fruit_pos = fruit_x, fruit_y = random.randrange(
                    0, window_x, step), random.randrange(0, window_y, step)
                state = "Playing"
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))

    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    restart_text = font.render(
        "Press 'R' to restart or 'ESC' to quit the game.", True, (255, 255, 255))

    if state == "Playing":
        if change_to[0] != direction_x or change_to[1] != direction_y:
            direction_x, direction_y = change_to

        head_x, head_y = snake[0]
        new_head = (head_x + direction_x * step, head_y + direction_y * step)
        snake.insert(0, new_head)

        if new_head in snake[1:]:
            state = "Game_Over"
        x, y = snake[0]
        if x < 0 or x >= window_x or y < 0 or y >= window_y:
            state = "Game_Over"
        if snake[0] == fruit_pos:
            score += 1
            fruit_pos = (random.randrange(
                0, window_x, step), random.randrange(0, window_y, step))
        else:
            snake.pop()

    if state == "Game_Over":
        screen.blit(game_over_text, (window_x//2 - 80, window_y//2 - 40))
        screen.blit(restart_text, (window_x//2 - 240, window_y//2))

    for seg in snake:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(
            seg[0], seg[1], step, step))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
        fruit_pos[0], fruit_pos[1], step, step))

    show_score = font.render(f"Score: {score} Pts", True, (254, 253, 252))
    screen.blit(show_score, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
