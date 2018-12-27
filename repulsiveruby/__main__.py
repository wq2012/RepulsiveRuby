import pygame
import sys
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.locals import K_d, K_a, K_w, K_s, K_ESCAPE, K_SPACE

sys.path.append(".")
from repulsiveruby import physics  # noqa: E402
from repulsiveruby import resources  # noqa: E402
from repulsiveruby import sprites  # noqa: E402


class GameStatus(object):
    def __init__(self):
        self.isGameRunning = False
        self.beginTime = 0
        self.endTime = 0
        self.loseTime = 0


def startOneGame(status):
    if not status.isGameRunning:
        resources.screen.blit(resources.background, (0, 0))
        resources.screen.blit(resources.intro, (0, 0))
        sprites.ball_main.reset()
        sprites.ball1.reset()
        sprites.ball2.reset()
        sprites.ball3.reset()
        sprites.ball1.speedX = -5
        sprites.ball1.speedY = -5
        sprites.ball2.speedX = 5
        sprites.ball2.speedY = -5
        sprites.ball3.speedX = 0
        sprites.ball3.speedY = 5
        status.loseTime = 0
        status.isGameRunning = True
        status.beginTime = pygame.time.get_ticks()


def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption(resources.CAPTION)
    resources.screen.blit(resources.background, (0, 0))
    resources.screen.blit(resources.intro, (0, 0))
    resources.music.play(-1)

    status = GameStatus()
    startOneGame(status)

    while True:
        # USER INPUT
        delta_t = clock.tick(20)
        for event in pygame.event.get():
            if not hasattr(event, "key"):
                continue
            down = event.type == KEYDOWN
            if event.key == K_RIGHT or event.key == K_d:
                sprites.ball_main.k_right = down * 3
            elif event.key == K_LEFT or event.key == K_a:
                sprites.ball_main.k_left = down * 3
            elif event.key == K_UP or event.key == K_w:
                sprites.ball_main.k_up = down * 3
            elif event.key == K_DOWN or event.key == K_s:
                sprites.ball_main.k_down = down * 3
            elif event.key == K_ESCAPE:
                sys.exit(0)
            elif event.key == K_SPACE:
                startOneGame(status)

        # RENDERING
        if not physics.ballGroupCollided(sprites.ball_group):
            sprites.ball_group.clear(resources.screen, resources.background)
            sprites.ball_group.clear(resources.screen, resources.intro)
            sprites.ball_group.update(delta_t)
            sprites.ball_group.draw(resources.screen)

            # resources.screen.blit(resources.intro, (0,0))
            pygame.display.flip()
        else:
            status.loseTime += 1
            if status.loseTime == 1:
                resources.screen.blit(resources.lose, (0, 0))
                status.endTime = pygame.time.get_ticks()
                pygame.display.set_caption(
                    "RepulsiveRuby - Your record is %.2f s" % (
                        (status.endTime - status.beginTime) / 1000.0))
                resources.collideSound.play()
            else:
                status.loseTime = 2
            status.isGameRunning = False
            pygame.display.flip()


if __name__ == "__main__":
    main()
