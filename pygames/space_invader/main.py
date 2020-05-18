import pygame
import random
import math
from pygame import mixer

# https://www.flaticon.com/
# http://freepik.com/

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode(size=(800, 600))

# Title
pygame.display.set_caption("My Random Game")
# game screen icon
icon = pygame.image.load('sports-and-competition.png')
pygame.display.set_icon(icon)

background = pygame.image.load("background.jpg")


mixer.music.load('Fantasy_Game_Background.mp3')
mixer.music.play(-1)

bullet_sound = mixer.Sound('Gunshot.wav')
collision_sound = mixer.Sound('collision.wav')

# player img
player_img = pygame.image.load("space_shooter.png")
player_X = 370
player_Y = 480
player_X_change = 0
player_speed: float = 4

# enemy img
# enemy_img = pygame.image.load("enemy_spaceship_0.png")
# enemy_X = random.randint(0, 800 - 64)
# enemy_Y = random.randint(50, 150)
# enemy_X_change = 0
enemy_Y_change = 40

# enemy_img = []
enemy_X = []
enemy_Y = []
enemy_img = []
enemy_count = 6

enemy_speed = [random.uniform(2, 3) for i in range(enemy_count)]

for i in range(enemy_count):
    enemy_img.append(pygame.image.load("enemy_spaceship_" + str(i) + ".png"))
    enemy_X.append(random.randint(0, 800 - 64))
    enemy_Y.append(random.randint(50, 150))

# bullet img
bullet_img = pygame.image.load("bullet.png")
bullet_X = player_X
bullet_Y = player_Y
# bullet_X_change = 0
bullet_Y_change = 0
bullet_speed: float = 5
bullet_state = "ready"

score = 0
font = pygame.font.Font('freesansbold.ttf', 50)
game_over_font = pygame.font.Font('freesansbold.ttf', 80)


def show_score():
    score_text = font.render("Score : " + str(score), True, (250, 200, 0))
    screen.blit(score_text, (10, 10))


def game_over_text():
    game_text = game_over_font.render("GAME OVER", True, (250, 200, 0))
    screen.blit(game_text, (200, 250))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(i, x, y):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y - 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(pow(enemyX - bulletX, 2) + pow(enemyY - bulletY, 2))
    return distance < 20


# create a loop for continuous display and break it based on event in pygame
# Game Loop
running = True
while running:
    # RGB Value
    screen.fill((10, 0, 50))
    # Blitting on every loop will ake the process little slow, so increase the speed to adjust
    screen.blit(background, (0, 0))

    # player_X += 0.1
    # should put something on screen after the background is drawn else fill will cover other things
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # print("Left Key Pressed")
                player_X_change = player_speed * -1
            if event.key == pygame.K_RIGHT:  # print("Right Key is pressed")
                player_X_change = player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state in "ready":
                    bullet_X = player_X
                    bullet_sound.play()
                    fire_bullet(bullet_X, bullet_Y)
        if event.type == pygame.KEYUP:  # print("Key Released")
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_X_change = 0

    player_X += player_X_change

    if player_X <= 0:
        player_X = 0
    if player_X >= 736:  # 736 = 800 - 64(img size)
        player_X = 736

    for i in range(enemy_count):
        if enemy_Y[i] > 440:
            for j in range(enemy_count):
                enemy_Y[j] = 4000
            game_over_text()
            break

        if enemy_X[i] <= 0 or enemy_X[i] >= 736:
            enemy_speed[i] = enemy_speed[i] * -1
            enemy_Y[i] += enemy_Y_change

        if is_collision(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y):
            collision_sound.play()
            bullet_Y = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemy_X[i] = random.randint(0, 800 - 64)
            enemy_Y[i] = random.randint(50, 150)
            # enemy_X_change = enemy_speed

        enemy_X[i] += enemy_speed[i]

        enemy(i, enemy_X[i], enemy_Y[i])

    if bullet_Y <= 0:
        bullet_Y = 480
        bullet_state = "ready"

    if bullet_state in "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_speed

    player(player_X, player_Y)
    show_score()
    # enemy(enemy_X, enemy_Y)
    # screen will not update so need to do it So display should update always
    pygame.display.update()
