import pygame
import os

img_path = os.getcwd() + "/resources/img"
font_path = os.getcwd() + "/resources/font"

class IMAGE:
    def __init__(self):
        self.image_cache = {}

        for dir in os.listdir(img_path):
            self.image_cache[dir] = {}
            for file in os.listdir(f"{img_path}/{dir}"):
                self.image_cache[dir][file.split(".")[0]] = pygame.image.load(f"{img_path}/{dir}/{file}")

    def load(self, type, name):
        return self.image_cache[type][name]
    
class FONT:
    def __init__(self):
        self.font_cache = {}

        for file in os.listdir(font_path):
            self.font_cache[file.split(".")[0]] = pygame.font.Font(f"{font_path}/{file}", 30)

    def load(self, type):
        return self.font_cache[type]

