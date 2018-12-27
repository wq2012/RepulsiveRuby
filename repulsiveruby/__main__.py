import pygame
import sys

sys.path.append(".")
from repulsiveruby import controls  # noqa: E402
from repulsiveruby import physics  # noqa: E402
from repulsiveruby import resources  # noqa: E402
from repulsiveruby import sprites  # noqa: E402

MS_PER_SECOND = 1000.0
FRAMERATE = 20


class GameStatus(object):
    def __init__(self):
        self.isGameRunning = False
        self.beginTime = 0
        self.endTime = 0
        self.bestRecord = 0


def startOneGame(status):
    if not status.isGameRunning:
        sprites.ballMain.reset()
        sprites.ball1.reset()
        sprites.ball2.reset()
        sprites.ball3.reset()
        sprites.ball1.speedX = -5
        sprites.ball1.speedY = -5
        sprites.ball2.speedX = 5
        sprites.ball2.speedY = -5
        sprites.ball3.speedX = 0
        sprites.ball3.speedY = 5
        status.isGameRunning = True
        status.beginTime = pygame.time.get_ticks()


def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption(resources.CAPTION)
    resources.screen.blit(resources.backgroundImage, (0, 0))
    resources.screen.blit(resources.introImage, (0, 0))
    resources.music.play(-1)

    status = GameStatus()
    startOneGame(status)

    # main loop of game
    while True:
        # get user input
        deltaT = clock.tick(FRAMERATE)
        result = controls.detectKey(sprites.ballMain)
        if result == "restart":
            startOneGame(status)

        # RENDERING
        if not physics.ballGroupCollided(sprites.ballGroup):
            sprites.ballGroup.clear(resources.screen, resources.backgroundImage)
            sprites.ballGroup.clear(resources.screen, resources.introImage)
            sprites.ballGroup.update(deltaT)
            sprites.ballGroup.draw(resources.screen)
            pygame.display.flip()
        else:  # collided
            if status.isGameRunning:
                resources.screen.blit(resources.loseImage, (0, 0))
                status.endTime = pygame.time.get_ticks()
                currentRecord = (
                    status.endTime - status.beginTime) / MS_PER_SECOND
                status.bestRecord = max(status.bestRecord, currentRecord)
                pygame.display.set_caption(
                    "RepulsiveRuby - Your survived for {:.2f}s, "
                    "with best record {:.2f}s".format(
                        currentRecord, status.bestRecord))
                resources.collideSound.play()
            status.isGameRunning = False
            pygame.display.flip()


if __name__ == "__main__":
    main()
