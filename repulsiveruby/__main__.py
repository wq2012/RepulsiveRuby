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


def startOneGame(status, ballGroup):
    if not status.isGameRunning:
        resources.screen.blit(resources.backgroundImage, (0, 0))
        resources.screen.blit(resources.introImage, (0, 0))
        rect = resources.screen.get_rect()
        # balls (ball images are 65*65)
        ballMain = sprites.MainBallSprite(resources.ballMainImage, rect.center)
        ball1 = sprites.RepulsiveBallSprite(
            resources.ball1Image, (200, 250), ballMain)
        ball2 = sprites.RepulsiveBallSprite(
            resources.ball2Image, (600, 150), ballMain)
        ball3 = sprites.RepulsiveBallSprite(
            resources.ball3Image, (500, 500), ballMain)
        ball1.speedX = -5
        ball1.speedY = -5
        ball2.speedX = 5
        ball2.speedY = -5
        ball3.speedX = 0
        ball3.speedY = 5
        ballGroup.empty()
        ballGroup.add(ballMain, ball1, ball2, ball3)

        status.isGameRunning = True
        status.beginTime = pygame.time.get_ticks()


def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption(resources.CAPTION)
    resources.music.play(-1)

    status = GameStatus()
    ballGroup = pygame.sprite.Group()
    startOneGame(status, ballGroup)

    # main loop of game
    while True:
        # get user input
        clock.tick(FRAMERATE)  # return value deltaT currently not used
        result = controls.detectKey(ballGroup.sprites()[0])
        if result == "restart":
            startOneGame(status, ballGroup)

        # rendering
        if not physics.ballGroupCollided(ballGroup):
            ballGroup.clear(resources.screen,
                            resources.backgroundImage)
            ballGroup.clear(resources.screen, resources.introImage)
            ballGroup.update()
            ballGroup.draw(resources.screen)
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
