import pygame
import sys

idx = 0
tmr = 0

WIDTH, HEIGHT = 1600, 900
tower = [pygame.image.load(f"./resources/img/tower/{i+1}.png") for i in range(6)]
pats = [pygame.image.load(f"./resources/img/tower/pats.png")]
back = [pygame.image.load(f"./resources/img/back/1.png")]

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

        if idx < 1:
            screen.blit(back[0], (0, 0))

        if idx == 0:
            screen.blit(pats[0], (450, 200))
            if key[pygame.K_SPACE] == 1:
                idx = 0.5

        if idx == 0.5:
            tmr += 1
            if tmr < 30:
                screen.blit(tower[tmr//5], (450, 200))

        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    main()