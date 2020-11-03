import random
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 102)

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

snake_size = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def show_score(score):
    show = score_font.render(f"Your score: {score}", True, white)
    display.blit(show, [0, 0])


def draw_snake(snake_list):
    for piece in snake_list:
        pygame.draw.rect(display, red, [piece[0], piece[1], snake_size, snake_size])


def message(text, color):
    msg = font_style.render(text, True, color)
    display.blit(msg, [display_width / 4, display_height / 3])


def game_loop():
    x = display_width / 2
    y = display_height / 2

    x_change = 0
    y_change = 0

    x_food = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    y_food = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0

    game_close = False
    game_over = False

    snake_list = []
    snake_lenght = 1

    while not game_over:

        while game_close:
            display.fill(black)
            message("You lost! Press Q - quit, A - play again.", red)
            show_score(snake_lenght - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        game_loop()

        for event in pygame.event.get():
            # print(event)

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change += snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change -= snake_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change += snake_size

        if x < 0 or x >= display_width or y < 0 or y >= display_height:
            game_close = True

        x += x_change
        y += y_change

        display.fill(black)
        snake_piece = [x, y]
        snake_list.append(snake_piece)

        if len(snake_list) > snake_lenght:
            del snake_list[0]
        for piece in snake_list[:-1]:
            if piece == snake_piece:
                game_close = True
        pygame.draw.rect(display, yellow, [x_food, y_food, snake_size, snake_size])
        draw_snake(snake_list)
        show_score(snake_lenght - 1)

        pygame.display.update()

        if x == x_food and y == y_food:
            x_food = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            y_food = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
            snake_lenght += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
