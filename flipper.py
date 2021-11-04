import pygame.sprite
image = pygame.image.load('flipper.png')
image = pygame.transform.scale(image, (100, 30))
import consts

class Flipper(pygame.sprite.Sprite):
    def __init__(self, rect:pygame.Rect):
        super(Flipper, self).__init__()
        self.image = image
        self.rect = rect
        self.flipping = False
        self.speed = 1
        self.angle = 0
        self.max_rotation = -40
        self.flipping=False



    def update(self):
        if self.flipping:
            if self.angle > self.max_rotation:
                self.angle = self.angle - 1
                center = self.rect.center
                self.image = pygame.transform.rotate(image, self.angle)
                self.rect.center = center
            else:
                self.image = pygame.transform.rotate(image, self.angle)
        else:
            self.angle = 0
            self.image = image
