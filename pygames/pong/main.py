import pygame
import random
import math
from pygame import mixer
import pygame.freetype  # Import the freetype module.

# https://www.flaticon.com/
# http://freepik.com/

# initialize pygame
pygame.init()

# create screen
SCREEN_X = 800
SCREEN_Y = 600
DISP_SURFACE = pygame.display.set_mode(size=(SCREEN_X, SCREEN_Y))
BG_COLOR = (10, 0, 50)
DISP_SURFACE.fill(BG_COLOR)
# Title
pygame.display.set_caption("My Random Game")
# game screen icon
icon = pygame.image.load('sports-and-competition.png')
pygame.display.set_icon(icon)

# background = pygame.image.load("background.jpg")

ball_radius = 10
ball_x = random.randint(0 + ball_radius, SCREEN_X - ball_radius)
ball_y = random.randint(0 + ball_radius, 150)
ball_speed = 0.3
BALL_COLOR = (255, 255, 255)

PADDLE_COLOR = (255, 255, 255)

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
PADDLE_Y = SCREEN_Y - PADDLE_HEIGHT
PADDLE_X = 250
PADDLE_SPEED = 0.6
PADDLE_X_CHANGE = 0

score = 0
font = pygame.font.Font('freesansbold.ttf', 50)
game_over_font = pygame.font.Font('freesansbold.ttf', 80)
angle = random.randint(40, 70)


# GAME_FONT = pygame.freetype.Font("freesansbold.ttf", 24)

def show_score():
    score_text = font.render("Score : " + str(score), True, (250, 200, 0))
    DISP_SURFACE.blit(score_text, (10, 10))
    # GAME_FONT.render_to(DISP_SURFACE, (10, 10), str(score), (0, 0, 0))


def game_over_text():
    game_text = game_over_font.render("GAME OVER", True, (250, 200, 0))
    DISP_SURFACE.blit(game_text, (200, 250))


def paddle_draw(x, clr=False):
    paddle_clr = BG_COLOR
    if clr:
        paddle_clr = PADDLE_COLOR
    pygame.draw.rect(DISP_SURFACE, paddle_clr, (x, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))


def circle_draw(x, y, clr=False):
    ball_clr = BG_COLOR
    if clr:
        ball_clr = BALL_COLOR
    pygame.draw.circle(DISP_SURFACE, ball_clr, (int(x), int(y)), ball_radius)


DISP_SURFACE.fill(BG_COLOR)
# create a loop for continuous display and break it based on event in pygame
# Game Loop
running = True
while running:

    circle_draw(ball_x, ball_y)
    paddle_draw(PADDLE_X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PADDLE_X_CHANGE = -1 * PADDLE_SPEED

            if event.key == pygame.K_RIGHT:
                PADDLE_X_CHANGE = PADDLE_SPEED

        if event.type == pygame.KEYUP:  # print("Key Released")
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                PADDLE_X_CHANGE = 0

    PADDLE_X += PADDLE_X_CHANGE

    if PADDLE_X < 0:
        PADDLE_X = 0
    if PADDLE_X > SCREEN_X - PADDLE_WIDTH:
        PADDLE_X = SCREEN_X - PADDLE_WIDTH

    paddle_draw(PADDLE_X, True)
    ball_x += math.cos(math.radians(angle)) * ball_speed
    ball_y += math.sin(math.radians(angle)) * ball_speed

    circle_draw(ball_x, ball_y, True)

    # if ball_x > SCREEN_X - ball_radius \
    #         or ball_x < ball_radius \
    #         or ball_y > SCREEN_Y - ball_radius \
    #         or ball_y < ball_radius:
    #     angle = 180 - angle
    #     if angle > 360:
    #         angle -= 360

    if ball_x > SCREEN_X - ball_radius:
        # print("Hitting Right Side")
        if angle < 90:
            angle = 180 - angle
        else:
            angle = 180 + 360 - angle
        # print("New Angle: " + str(angle))
    if ball_x < ball_radius:
        # print("Hitting Left Side")
        if 180 < angle < 270:
            angle = 360 - (angle - 180)
        else:  # 90 < angle <= 180:
            angle = 180 - angle
    # print("New Angle: " + str(angle))

    if abs(PADDLE_Y - ball_radius - ball_y) < 1 \
            and PADDLE_X - ball_radius <= ball_x <= PADDLE_X + PADDLE_WIDTH + ball_radius:
        angle = 360 - angle + random.randint(-30,30)
		
        ball_speed *= 1.05
        print(ball_speed)
        score += 1
    if ball_y + ball_radius > PADDLE_Y+5:
        print("paddle x", PADDLE_X, "ball_x", ball_x, "ball_y", ball_y)
        game_over_text()
        running = False
    # if ball_y > PADDLE_Y:
    #     game_over_text()
    # print("Hitting Down Side")
    # if 90 < angle < 180:

    # angle = 360 - angle
    # elif angle < 90:

    # print("Old Angle: " + str(angle))
    # angle += 90
    # print("New Angle: " + str(angle))
    if ball_y < ball_radius:
        #  print("Hitting Up Side")
        # if 270 < angle < 360:
        angle = 360 - angle
    #  print("New Angle: " + str(angle))
    # if angle > 360:
    #     angle -= 360

    # enemy(enemy_X, enemy_Y)
    # screen will not update so need to do it So display should update always
    show_score()
    pygame.display.update()
