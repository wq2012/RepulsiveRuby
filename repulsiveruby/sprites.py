import pygame

from repulsiveruby import resources


class MainBallSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5
    RADIUS = 30

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speedX = self.speedY = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, delta_t):
        # SIMULATION
        self.speedY += (-self.k_up + self.k_down)
        self.speedX += (-self.k_left + self.k_right)
        if self.speedX > self.MAX_FORWARD_SPEED:
            self.speedX = self.MAX_FORWARD_SPEED
        if self.speedX < -self.MAX_REVERSE_SPEED:
            self.speedX = -self.MAX_REVERSE_SPEED
        if self.speedY > self.MAX_FORWARD_SPEED:
            self.speedY = self.MAX_FORWARD_SPEED
        if self.speedY < -self.MAX_REVERSE_SPEED:
            self.speedY = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        x, y = self.position

        x += self.speedX
        y += self.speedY
        x = max(x, self.RADIUS)
        x = min(x, resources.SCREEN_W - self.RADIUS)
        y = max(y, self.RADIUS)
        y = min(y, resources.SCREEN_H - self.RADIUS)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


class BallSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5
    RADIUS = 30

    def __init__(self, image, position, ball1):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speedX = self.speedY = self.speed = self.d = 0
        self.aRight = self.aDown = 0
        self.distance = (
            self.position[0]-ball1.position[0],
            self.position[1]-ball1.position[1])

    def update(self, delta_t, ball1):
        # SIMULATION
        self.distance = (
            self.position[0]-ball1.position[0],
            self.position[1]-ball1.position[1])
        self.d = (self.distance[0]**2+self.distance[1]**2)**0.5
        if self.d < 200:
            self.aRight = self.distance[0]/self.d*3
            self.aDown = self.distance[1]/self.d*3
            self.speedX += self.aRight
            self.speedY += self.aDown

        self.speed = (self.speedX**2+self.speedY**2)**0.5

        if self.speedX > self.MAX_FORWARD_SPEED:
            self.speedX = self.MAX_FORWARD_SPEED
        if self.speedX < -self.MAX_REVERSE_SPEED:
            self.speedX = -self.MAX_REVERSE_SPEED
        if self.speedY > self.MAX_FORWARD_SPEED:
            self.speedY = self.MAX_FORWARD_SPEED
        if self.speedY < -self.MAX_REVERSE_SPEED:
            self.speedY = -self.MAX_REVERSE_SPEED
        x, y = self.position
        x += self.speedX
        y += self.speedY
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
        self.image = self.src_image
        self.rect = self.image.get_rect()
        self.rect.center = self.position
