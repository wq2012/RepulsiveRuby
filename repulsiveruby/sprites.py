from __future__ import print_function
import pygame

from repulsiveruby import physics
from repulsiveruby import resources


class BaseBallSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = (0, 0)
        self.direction = 0
        self.speedX = 0
        self.speedY = 0
        self.accelerationX = 0
        self.accelerationY = 0
        self.maxSpeed = 15
        self.radius = 32

    def updateSpeed(self):
        self.speedX += self.accelerationX
        self.speedY += self.accelerationY
        currentSpeed = physics.norm((self.speedX, self.speedY))
        if currentSpeed > self.maxSpeed:
            self.speedX = self.speedX / currentSpeed * self.maxSpeed
            self.speedY = self.speedY / currentSpeed * self.maxSpeed

    def updatePosition(self, bounce):
        x, y = self.position
        x += self.speedX
        y += self.speedY

        # boundary detection
        if x < self.radius:
            x = self.radius
            if bounce:
                self.speedX *= -1
        if x > resources.SCREEN_W - self.radius:
            x = resources.SCREEN_W - self.radius
            if bounce:
                self.speedX *= -1
        if y < self.radius:
            y = self.radius
            if bounce:
                self.speedY *= -1
        if y > resources.SCREEN_H - self.radius:
            y = resources.SCREEN_H - self.radius
            if bounce:
                self.speedY *= -1
        self.position = (x, y)


class MainBallSprite(BaseBallSprite):

    def __init__(self, image, position):
        BaseBallSprite.__init__(self)
        self.srcImage = image
        self.position = position
        self.k_left = 0
        self.k_right = 0
        self.k_down = 0
        self.k_up = 0

    def update(self, deltaT):
        # update speed according to key
        self.accelerationX = (-self.k_left + self.k_right)
        self.accelerationY = (-self.k_up + self.k_down)
        self.updateSpeed()

        # update position
        self.updatePosition(False)

        # update image and rect
        self.direction += (self.k_right + self.k_left)
        self.image = pygame.transform.rotate(self.srcImage, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


class RepulsiveBallSprite(BaseBallSprite):

    def __init__(self, image, position, ballMain):
        BaseBallSprite.__init__(self)
        self.srcImage = image
        self.position = position
        self.ballMain = ballMain

    def update(self, deltaT):
        # SIMULATION
        vecToMain = (
            self.position[0] - self.ballMain.position[0],
            self.position[1] - self.ballMain.position[1])
        distanceToMain = physics.norm(vecToMain)
        if distanceToMain < 200:
            self.accelerationX = vecToMain[0] / distanceToMain * 3
            self.accelerationY = vecToMain[1] / distanceToMain * 3
        else:
            self.accelerationX = 0
            self.accelerationY = 0

        self.updateSpeed()

        # update position
        self.updatePosition(True)

        # update image and rect
        self.direction += (self.speedX + self.speedY) / 2
        self.image = pygame.transform.rotate(self.srcImage, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
