import pygame
import ResourceManager
import sys

pygame.init()

img_mgr = ResourceManager.IMAGE()
fnt_mgr = ResourceManager.FONT()

general = fnt_mgr.load("general")
ex = fnt_mgr.load("ex")

class StartScreen:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.surfaces = []
        
        text1 = general.render("시작하려면 아무 키나 누르세요", True, (0, 0, 0))
        self.surfaces.append([img_mgr.load("start", "back"), (0, 0)])
        self.surfaces.append([text1, (640 - text1.get_width()/2, 600)])       

    def render(self):
        for data in self.surfaces:
            self.screen.blit(data[0], data[1])

        self.event()

    def update(self):
        pass

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()