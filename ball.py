import pygame.sprite

import consts


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.image = pygame.image.load('ball.png')
        self.rect = pygame.Rect(300, 300, 32, 32)
        self.momentum = pygame.Vector2(5, 1)



    def update(self):
        if self.momentum[1] < consts.MAX_GRAVITY_SPEED:

            self.momentum[1] = self.momentum[1] + consts.GRAVITY

        self.rect.move_ip(self.momentum[0], self.momentum[1])

        if self.rect.bottom > consts.SCREEN_WIDE:
            self.rect.bottom = consts.SCREEN_WIDE
            self.bounce(horizontal=False)
        if self.rect.top < 0:
            self.rect.top = 0
            self.bounce(horizontal=False)
        if self.rect.left < 0:
            self.rect.left = 0
            self.bounce()
        if self.rect.right > consts.SCREEN_WIDTH:
            self.rect.right = consts.SCREEN_WIDTH
            self.bounce()



    def bounce(self, horizontal=True):
        energy_loss = -0.9
        if horizontal:
            self.momentum[0] = self.momentum[0] * energy_loss
            self.momentum[1] = self.momentum[1] * 0.99
        else:
            self.momentum[1] = self.momentum[1] * energy_loss
            self.momentum[0] = self.momentum[0] * 0.99