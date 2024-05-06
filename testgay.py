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

    player = pygame.Rect(100, 100, 100, 74)
    gvel = 0
    dj = True
    jumpkeydown = False

    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            player.left -= 6

        if key[pygame.K_RIGHT]:
            player.left += 6    

        if player.bottom < 720:
            gvel += 0.4

        else:
            player.bottom = 720
            gvel = 0
            dj = True

        if key[pygame.K_SPACE]:
            print("SPACEs")
            if player.bottom >= 720:
                gvel -= 10

            else:
                if dj and not jumpkeydown:
                    if gvel > 0:
                        gvel = -10
                    
                    else:
                        gvel -= 5
                    
                    dj = False

            jumpkeydown = True

        if not key[pygame.K_SPACE]:
            jumpkeydown = False


        player.top += gvel

        screen.blit(char, player)

        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    main()