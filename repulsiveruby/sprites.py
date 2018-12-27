import pygame

from repulsiveruby import physics
from repulsiveruby import resources


class MainBallSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5
    RADIUS = 32

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
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
        self.speedX = min(self.speedX, self.MAX_FORWARD_SPEED)
        self.speedX = max(self.speedX, -self.MAX_REVERSE_SPEED)
        self.speedY = min(self.speedY, self.MAX_FORWARD_SPEED)
        self.speedY = max(self.speedY, -self.MAX_REVERSE_SPEED)

        self.direction += (self.k_right + self.k_left)
        x, y = self.position

        x += self.speedX
        y += self.speedY

        # boundary detection
        x = max(x, self.RADIUS)
        x = min(x, resources.SCREEN_W - self.RADIUS)
        y = max(y, self.RADIUS)
        y = min(y, resources.SCREEN_H - self.RADIUS)
        self.position = (x, y)

        self.image = pygame.transform.rotate(self.srcImage, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


class BallSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5
    RADIUS = 32

    def __init__(self, image, position, ballMain):
        pygame.sprite.Sprite.__init__(self)
        self.srcImage = image
        self.initPosition = position
        self.ballMain = ballMain
        self.reset()

    def reset(self):
        self.position = self.initPosition
        self.speedX = self.speedY = self.speed = self.d = 0
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

        self.speedX = min(self.speedX, self.MAX_FORWARD_SPEED)
        self.speedX = max(self.speedX, -self.MAX_REVERSE_SPEED)
        self.speedY = min(self.speedY, self.MAX_FORWARD_SPEED)
        self.speedY = max(self.speedY, -self.MAX_REVERSE_SPEED)

        x, y = self.position
        x += self.speedX
        y += self.speedY

        # boundary detection
        if x < self.RADIUS:
            x = self.RADIUS
            self.speedX *= -1
        if x > resources.SCREEN_W - self.RADIUS:
            x = resources.SCREEN_W - self.RADIUS
            self.speedX *= -1
        if y < self.RADIUS:
            y = self.RADIUS
            self.speedY *= -1
        if y > resources.SCREEN_H - self.RADIUS:
            y = resources.SCREEN_H - self.RADIUS
            self.speedY *= -1
        self.position = (x, y)

        self.image = self.srcImage
        self.rect = self.image.get_rect()
        self.rect.center = self.position


# balls (ball images are 65*65)
rect = resources.screen.get_rect()
ballMain = MainBallSprite(resources.ballMainImage, rect.center)
ball1 = BallSprite(resources.ball1Image, (200, 250), ballMain)
ball2 = BallSprite(resources.ball2Image, (600, 150), ballMain)
ball3 = BallSprite(resources.ball3Image, (500, 500), ballMain)
ballGroup = pygame.sprite.Group(ballMain, ball1, ball2, ball3)
