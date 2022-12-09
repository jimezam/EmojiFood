import pygame, random

class Bug (pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.files = ('1F98B', '1F41B', '1F41C', '1FAB2', '1F997', 
                      '1FAB3', '1F982', '1FAB1', '1F578', '1FAB0')
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
