import pygame
import sys

idx = 0

WIDTH, HEIGHT = 1600, 900
tower = [pygame.image.load(f"./resources/img/tower/{i+1}.png") for i in range(6)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        if idx == 0:
            pass
            
        

if __name__ == "__main__":
    main()