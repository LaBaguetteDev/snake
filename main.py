import pygame
import random


def app():
    # Couleurs
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)

    # Taille écran
    dis_width = 600
    dis_height = 400

    # Vitesse
    clock = pygame.time.Clock()
    snake_speed = 15
    # Taille
    snake_block = 10

    # Initialisation
    pygame.init()
    dis = pygame.display.set_mode((dis_width, dis_height))

    # Display
    pygame.display.update()
    pygame.display.set_caption('Snake par LaBaguetteDev')
    # Message
    font_style = pygame.font.SysFont("bahnschrift", 20)
    score_font = pygame.font.SysFont(None, 35)

    def snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

    def score(score):
        value = score_font.render(str(score), True, green)
        dis.blit(value, [0, 0])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 25, dis_height / 4])

    def game_loop():
        # Variables de jeu
        game_over = False
        game_close = False
        x1 = dis_width / 2
        y1 = dis_height / 2
        x1_change = 0
        y1_change = 0
        snake_list = []
        snake_length = 1
        # Nourriture
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                dis.fill(black)
                message("Vous avez perdu ! Appuyez sur Q-Quitter ou R-Recommencer", red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:

                        # Quitter
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        # Recommencer
                        if event.key == pygame.K_r:
                            game_loop()

            for event in pygame.event.get():
                # Quitter
                if event.type == pygame.QUIT:
                    game_over = True

                if event.type == pygame.KEYDOWN:
                    # Gauche
                    if event.key == pygame.K_LEFT:
                        if x1_change != snake_block:
                            x1_change = -snake_block
                            y1_change = 0
                    # Droite
                    elif event.key == pygame.K_RIGHT:
                        if x1_change != -snake_block:
                            x1_change = snake_block
                            y1_change = 0
                    # Haut
                    elif event.key == pygame.K_UP:
                        if y1_change != snake_block:
                            x1_change = 0
                            y1_change = -snake_block
                    # Bas
                    elif event.key == pygame.K_DOWN:
                        if y1_change != -snake_block:
                            x1_change = 0
                            y1_change = snake_block
            # Game Over
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change

            dis.fill(black)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            snake(snake_block, snake_list)
            score(snake_length-1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                snake_length += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    game_loop()


if __name__ == '__main__':
    app()
