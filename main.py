import pygame
import consts
import consts as c
import ball
import flipper

# pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()
screen.fill(c.BLACK)

ball_1 = ball.Ball('Jerry', pygame.Rect(300, 300, 24, 24), pygame.Vector2(15, 1))
ball_2 = ball.Ball('Fred', pygame.Rect(799, 799, 24, 24), pygame.Vector2(20, 20))
ball_3 = ball.Ball('Hank', pygame.Rect(5, 5, 24, 24), pygame.Vector2(40, 40))

ball_group = pygame.sprite.Group()

ball_group.add([ball_1, ball_2, ball_3])

flipper_1 = flipper.Flipper(pygame.Rect(500, 500, 100, 30), 1)
flipper_2 = flipper.Flipper(pygame.Rect(300, 500, 100, 30), 0)
flipper_group = pygame.sprite.Group()
flipper_group.add(flipper_1, flipper_2)


def collide_if_not_self(left, right):
    if left != right:
        return pygame.sprite.collide_rect(left, right)
    return False


while True:
    clock.tick(c.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
                flipper_1.flipping = True
            if event.key == pygame.K_LSHIFT:
                flipper_2.flipping = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT:
                flipper_1.flipping = False
            if event.key == pygame.K_LSHIFT:
                flipper_2.flipping = False



    screen.fill(c.WHITE)

    ball_group.update()
    ball_group.draw(screen)
    for ball in ball_group:
        coll = pygame.sprite.spritecollide(ball, ball_group, False, collide_if_not_self)
        if not len(coll) == 0:
            ball2 = coll[0]

            tempmom = ball.momentum.reflect(ball2.momentum)
            ball2.momentum.reflect_ip(ball.momentum)
            ball.momentum = tempmom

    flipper_col = (pygame.sprite.groupcollide(ball_group, flipper_group, False, False, collided=None))
    if len(flipper_col) > 0:
        for ball, flipper in flipper_col.items():
            ball.momentum.reflect_ip(pygame.Vector2(-10, -10))

    flipper_group.update()
    flipper_group.draw(screen)

    textsurface = myfont.render(f'{ball_1.rect=}, {ball_1.momentum=}', False, (0, 0, 0))
    textsurface2 = myfont.render(f'{ball_1.calculate_speed()=}', False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    screen.blit(textsurface2, (0, 200))

    pygame.display.update()
