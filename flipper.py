import pygame as pygame
import pygame.sprite
import pygame
import consts
img1 = pygame.image.load('flipper_1.png')
img2 = pygame.image.load('flipper_2.png')
images = [img1, img2]



class Flipper(pygame.sprite.Sprite):
    def __init__(self, rect:pygame.Rect, img):
        super(Flipper, self).__init__()
        print(f'{img=}')
        self.img = img
        self.image = images[img]
        self.rect = rect
        self.flipping = False
        self.speed = 1
        self.angle = 0
        self.max_rotation = 40
        self.flipping=False



    def update(self):
        if self.flipping:
            if self.angle < self.max_rotation:
                self.angle = self.angle + 1
                center = self.rect.center
                self.image = pygame.transform.rotate(images[self.img], self.angle)
                self.rect.center = center
            else:
                self.image = pygame.transform.rotate(images[self.img], self.angle)
        else:
            if self.angle > 0:
                self.angle = self.angle - 5
                if self.angle < 0:self.angle =0
                self.image = pygame.transform.rotate(images[self.img], self.angle)
