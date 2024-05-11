import pygame
import sys

pygame.init()

# Images

## GUI

gui_startscreen = pygame.image.load("resources/img/gui/startscreen.png")

## Character

char_atk = [[pygame.image.load(f"resources/img/character/atk/atk1_{i}.png") for i in range(5)], 
            [pygame.image.load(f"resources/img/character/atk/atk2_{i}.png") for i in range(5)], 
            [pygame.image.load(f"resources/img/character/atk/atk3_{i}.png") for i in range(5)]]

for i in range(3):
    for j in range(5):
        caij = char_atk[i][j]
        char_atk[i][j] = pygame.transform.scale(caij, (caij.get_width()*3, caij.get_height()*3))

# Event

EVENT_KEYDOWN = False

# Input

INPUT_KEY = pygame.key.get_pressed()

# Attribute

## Player

p_hitbox_w, p_hitbox_h = 54, 75
p_x, p_y = 100, 100

p_left = False

# Obj

## Player

p_rect = pygame.Rect(p_x, p_y, p_hitbox_w, p_hitbox_h)

# Code

running = True

idx = 0
tmr = 0

WIDTH, HEIGHT = 1600, 900

def main():
    global INPUT_KEY
    global EVENT_KEYDOWN
    global p_x, p_y, p_left
    global running
    global idx, tmr

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                EVENT_KEYDOWN = True
            if event.type == pygame.QUIT:
                running = False

        if idx == 0:
            screen.blit(gui_startscreen, (0, 0))

            if EVENT_KEYDOWN:
                idx = 1

        elif idx == 1:
            screen.blit(char_atk[0][0], p_rect)
            pygame.draw.rect(screen, (255, 0, 0), p_rect)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

    