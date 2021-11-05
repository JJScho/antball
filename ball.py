import pygame.sprite
image = pygame.image.load('ball.png')
import consts

class Ball(pygame.sprite.Sprite):
    def __init__(self,name, rect:pygame.Rect, momentum:pygame.Vector2):
        super(Ball, self).__init__()
        self.name = name
        self.image = image
        self.rect = rect
        self.momentum = momentum

    def update(self):
        if self.momentum[1] < consts.MAX_GRAVITY_SPEED:
            self.momentum[1] = self.momentum[1] + consts.GRAVITY
        self.rect.move_ip(self.momentum[0], self.momentum[1])

        if self.rect.bottom > consts.SCREEN_HEIGHT:
            self.rect.bottom = consts.SCREEN_HEIGHT
            self.wall_bounce(horizontal=False)
        if self.rect.top < 0:
            self.rect.top = 0
            self.wall_bounce(horizontal=False)
        if self.rect.left < 0:
            self.rect.left = 0
            self.wall_bounce()
        if self.rect.right > consts.SCREEN_WIDTH:
            self.rect.right = consts.SCREEN_WIDTH
            self.wall_bounce()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def reset_momentum(self):
        self.momentum = pygame.Vector2(0, 0)

    def calculate_speed(self):
        return abs(self.momentum[0]) + abs(self.momentum[1])

    def double_momentum(self):
        self.momentum[0] = self.momentum[0] * 2
        self.momentum[1] = self.momentum[1] * 2

    def reverse_momentum(self, direction):
        if direction == 0:
            self.momentum[0] = self.momentum[0] * consts.ENERGY_LOSS
            self.momentum[1] = self.momentum[1] * 0.99
        else:
            self.momentum[1] = self.momentum[1] * consts.ENERGY_LOSS
            self.momentum[0] = self.momentum[0] * 0.99


    def wall_bounce(self, horizontal=True):
        '''moet vectors gebruiken'''

        if horizontal:
            self.reverse_momentum(0)
        else:
            self.reverse_momentum(1)

