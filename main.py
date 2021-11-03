import pygame

import consts
import consts as c
import ball
# pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)


screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_WIDE))
clock = pygame.time.Clock()
screen.fill(c.BLACK)

mainball = ball.Ball()


ball_group = pygame.sprite.Group()

ball_group.add(mainball)

while True:
    clock.tick(c.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill(c.WHITE)
    ball_group.update()
    textsurface = myfont.render(f'{mainball.rect=}, {mainball.momentum=}', False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    ball_group.draw(screen)
    pygame.display.update()
