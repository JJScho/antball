import pygame

import consts
import consts as c
import ball

# pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()
screen.fill(c.BLACK)

ball_1 = ball.Ball('Jerry',pygame.Rect( 300, 300, 24, 24), pygame.Vector2(15, 1))
ball_2 = ball.Ball('Fred', pygame.Rect(799, 799, 24, 24), pygame.Vector2(20, 20))
ball_3 = ball.Ball('Hank', pygame.Rect(5, 5, 24, 24), pygame.Vector2(40, 40))

ball_group = pygame.sprite.Group()

ball_group.add([ball_1, ball_2, ball_3])


def collide_if_not_self(left, right):
    if left != right:
        return pygame.sprite.collide_rect(left, right)
    return False


while True:
    clock.tick(c.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill(c.WHITE)
    ball_group.update()

    for ball in ball_group:
        coll = pygame.sprite.spritecollide(ball, ball_group, False, collide_if_not_self)
        if not len(coll) == 0:
            ball2 = coll[0]

            tempmom = ball.momentum.reflect(ball2.momentum)
            ball2.momentum.reflect_ip(ball.momentum)
            ball.momentum = tempmom





    textsurface = myfont.render(f'{ball_1.rect=}, {ball_1.momentum=}', False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    ball_group.draw(screen)
    pygame.display.update()
