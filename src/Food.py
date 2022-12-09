import pygame, random

class Food (pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.files = ('1F347', '1F34A', '1F34C', '1F34D', '1F34E', 
                      '1F351', '1F352', '1F353', '1F95D', '1F965')
        self.reset()

    def reset(self):
        index = random.randrange(0, len(self.files))
        self.image = pygame.image.load(f"assets/emoticons/{self.files[index]}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.width
        self.rect.y = random.randrange(self.height - self.rect.height)
        self.speed_x = random.randrange(2, 6)

    def update(self):
        self.rect.x -= self.speed_x
