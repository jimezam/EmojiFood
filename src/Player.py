import pygame
from pygame.locals import *

class Player (pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.files = ('1F9D1-1F3FB-200D-1F384')
        self.step = 8
        self.reset()

    def reset(self):
        self.image = pygame.image.load(
            f"assets/emoticons/{self.files}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = (self.height - self.rect.height)/2

    def move(self, keys):
        if(keys[K_LEFT] and self.rect.x > 0):
            self.rect.x -= self.step

        if(keys[K_RIGHT] and self.rect.x < self.width - self.rect.width):
            self.rect.x += self.step

        if(keys[K_UP] and self.rect.y > 0):
            self.rect.y -= self.step

        if(keys[K_DOWN] and self.rect.y < self.height - self.rect.height):
            self.rect.y += self.step

    def moveTo(self, centerX, centerY):
        self.rect.center = (centerX, centerY)