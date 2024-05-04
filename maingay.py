import pygame
import sys

idx = 0
tmr = 0

WIDTH, HEIGHT = 1280, 720
char = pygame.image.load("resources/img/char/adventurer-idle-2-00.png")
char = pygame.transform.scale(char, (100, 74))

def main():
    global idx, tmr

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()