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

def start():
    global GameRunning
    global loseTime
    global beginTime
    if not GameRunning:
        resources.screen.blit(resources.background, (0, 0))
        resources.screen.blit(resources.intro, (0, 0))
        sprites.ball1.reset()
        sprites.ball2.reset()
        sprites.ball3.reset()
        sprites.ball4.reset()
        sprites.ball2.speedX = -5
        sprites.ball2.speedY = -5
        sprites.ball3.speedX = 5
        sprites.ball3.speedY = -5
        sprites.ball4.speedX = 0
        sprites.ball4.speedY = 5
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
            sprites.ball1.k_right = down * 3
        elif event.key == K_LEFT or event.key == K_a:
            sprites.ball1.k_left = down * 3
        elif event.key == K_UP or event.key == K_w:
            sprites.ball1.k_up = down * 3
        elif event.key == K_DOWN or event.key == K_s:
            sprites.ball1.k_down = down * 3
        elif event.key == K_ESCAPE:
            sys.exit(0)
        elif event.key == K_SPACE:
            start()

    # RENDERING

    if not physics.collide(sprites.ball1, sprites.ball2, sprites.ball3,
                           sprites.ball4):

        sprites.ball_group.clear(resources.screen, resources.background)
        sprites.ball_group.clear(resources.screen, resources.intro)
        sprites.ball_group.update(delta_t)
        sprites.ball_group.draw(resources.screen)

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
