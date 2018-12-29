from __future__ import print_function
import pygame

from repulsiveruby import physics
from repulsiveruby import resources


class BaseBallSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedX = 0
        self.speedY = 0
        self.maxSpeed = 15
        self.radius = 32

    def constrainSpeed(self):
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
        self.initPosition = position
        self.reset()

    def reset(self):
        self.position = self.initPosition
        self.speedX = self.speedY = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, deltaT):
        # SIMULATION
        self.speedY += (-self.k_up + self.k_down)
        self.speedX += (-self.k_left + self.k_right)
        self.constrainSpeed()

        self.direction += (self.k_right + self.k_left)
        self.updatePosition(False)

        self.image = pygame.transform.rotate(self.srcImage, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


class RepulsiveBallSprite(BaseBallSprite):

    def __init__(self, image, position, ballMain):
        BaseBallSprite.__init__(self)
        self.srcImage = image
        self.initPosition = position
        self.ballMain = ballMain
        self.reset()

    def reset(self):
        self.position = self.initPosition
        self.speedX = self.speedY = self.speed = self.d = 0
        self.direction = 0
        self.aRight = self.aDown = 0
        self.distance = (
            self.position[0] - self.ballMain.position[0],
            self.position[1] - self.ballMain.position[1])

    def update(self, deltaT):
        # SIMULATION
        self.distance = (
            self.position[0] - self.ballMain.position[0],
            self.position[1] - self.ballMain.position[1])
        self.d = physics.norm((self.distance[0], self.distance[1]))
        if self.d < 200:
            self.aRight = self.distance[0] / self.d * 3
            self.aDown = self.distance[1] / self.d * 3
            self.speedX += self.aRight
            self.speedY += self.aDown

        self.speed = physics.norm((self.speedX, self.speedY))

        self.constrainSpeed()
        self.updatePosition(True)

        self.direction += (self.speedX + self.speedY) / 2
        self.image = pygame.transform.rotate(self.srcImage, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
