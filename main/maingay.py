import pygame
import sys

idx = 0
tmr = 0

WIDTH, HEIGHT = 1280, 720

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

        ScreenManager.StartScreen(screen).render()
 
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()