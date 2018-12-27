import pygame
import sys
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.locals import K_d, K_a, K_w, K_s, K_ESCAPE, K_SPACE

sys.path.append(".")
from repulsiveruby import physics  # noqa: E402
from repulsiveruby import resources  # noqa: E402
from repulsiveruby import sprites  # noqa: E402


clock = pygame.time.Clock()
pygame.display.set_caption("RepulsiveRuby v2.0 - developed by Quan Wang")

resources.screen.blit(resources.background, (0, 0))
resources.screen.blit(resources.intro, (0, 0))
loseTime = 0
GameRunning = False
beginTime = 0
endTime = 0

resources.music.play(-1)


# CREATE BALLS AND RUN


rect = resources.screen.get_rect()
ball1 = sprites.MainBallSprite(
    resources.images_dir + "/ball1.png", rect.center)
ball2 = sprites.BallSprite(resources.images_dir +
                           "/ball2.png", (200, 250), ball1)
ball3 = sprites.BallSprite(resources.images_dir +
                           "/ball3.png", (600, 150), ball1)
ball4 = sprites.BallSprite(resources.images_dir +
                           "/ball4.png", (500, 500), ball1)
ball1_group = pygame.sprite.RenderPlain(ball1)
ball2_group = pygame.sprite.RenderPlain(ball2)
ball3_group = pygame.sprite.RenderPlain(ball3)
ball4_group = pygame.sprite.RenderPlain(ball4)


def start():
    global GameRunning
    global loseTime
    global beginTime
    global ball1, ball2, ball3, ball4
    global ball1_group, ball2_group, ball3_group, ball4_group
    if not GameRunning:
        resources.screen.blit(resources.background, (0, 0))
        resources.screen.blit(resources.intro, (0, 0))
        ball1 = sprites.MainBallSprite(
            resources.images_dir + "/ball1.png", rect.center)
        ball2 = sprites.BallSprite(
            resources.images_dir + "/ball2.png", (200, 250), ball1)
        ball3 = sprites.BallSprite(
            resources.images_dir + "/ball3.png", (600, 150), ball1)
        ball4 = sprites.BallSprite(
            resources.images_dir + "/ball4.png", (500, 500), ball1)
        ball1_group = pygame.sprite.RenderPlain(ball1)
        ball2_group = pygame.sprite.RenderPlain(ball2)
        ball3_group = pygame.sprite.RenderPlain(ball3)
        ball4_group = pygame.sprite.RenderPlain(ball4)
        ball2.speedX = -5
        ball2.speedY = -5
        ball3.speedX = 5
        ball3.speedY = -5
        ball4.speedX = 0
        ball4.speedY = 5
        loseTime = 0
        GameRunning = True
        beginTime = pygame.time.get_ticks()


start()

while 1:

    # USER INPUT
    delta_t = clock.tick(20)
    for event in pygame.event.get():
        if not hasattr(event, "key"):
            continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT or event.key == K_d:
            ball1.k_right = down * 3
        elif event.key == K_LEFT or event.key == K_a:
            ball1.k_left = down * 3
        elif event.key == K_UP or event.key == K_w:
            ball1.k_up = down * 3
        elif event.key == K_DOWN or event.key == K_s:
            ball1.k_down = down * 3
        elif event.key == K_ESCAPE:
            sys.exit(0)
        elif event.key == K_SPACE:
            start()

    # RENDERING

    if not physics.collide(ball1, ball2, ball3, ball4):

        ball1_group.clear(resources.screen, resources.background)
        ball2_group.clear(resources.screen, resources.background)
        ball3_group.clear(resources.screen, resources.background)
        ball4_group.clear(resources.screen, resources.background)
        ball1_group.clear(resources.screen, resources.intro)
        ball2_group.clear(resources.screen, resources.intro)
        ball3_group.clear(resources.screen, resources.intro)
        ball4_group.clear(resources.screen, resources.intro)
        ball1_group.update(delta_t)
        ball2_group.update(delta_t)
        ball3_group.update(delta_t)
        ball4_group.update(delta_t)
        ball1_group.draw(resources.screen)
        ball2_group.draw(resources.screen)
        ball3_group.draw(resources.screen)
        ball4_group.draw(resources.screen)

        # resources.screen.blit(resources.intro, (0,0))
        pygame.display.flip()
    else:
        loseTime += 1
        if loseTime == 1:
            resources.screen.blit(resources.lose, (0, 0))
            endTime = pygame.time.get_ticks()
            pygame.display.set_caption(
                "RepulsiveRuby v2.0 - Your record is %.2f s" % (
                    (endTime-beginTime)/1000.0))
            resources.collideSound.play()
        else:
            loseTime = 2
        GameRunning = False
        pygame.display.flip()
