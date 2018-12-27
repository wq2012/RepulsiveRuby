#screen is 800*600
#ball image is 65*65

#initialization
import pygame, math, sys
import os
from pygame.locals import *
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("RepulsiveRuby v2.0 - developed by Quan Wang")
background = pygame.image.load('images/background.png')
intro = pygame.image.load('images/intro.png')
lose = pygame.image.load('images/lose.png')
screen.blit(background, (0,0))
screen.blit(intro, (0,0))
loseTime=0
GameRunning = False
beginTime=0
endTime=0
music = pygame.mixer.Sound("sound/music.wav")
collideSound = pygame.mixer.Sound("sound/collide.wav")
music.play(-1)

class MainBallSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speedX = self.speedY = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0
    def update(self, deltat):
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
        if x<30:
            x=30
        if x>770:
            x=770
        if y<30:
            y=30
        if y>570:
            y=570
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

class BallSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5
    def __init__(self, image, position, ball1):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speedX = self.speedY = self.speed  = self.d = 0
        self.aRight=self.aDown=0
        self.distance=(self.position[0]-ball1.position[0],self.position[1]-ball1.position[1])
    def update(self, deltat,ball1):
        # SIMULATION
        self.distance=(self.position[0]-ball1.position[0],self.position[1]-ball1.position[1])
        self.d=(self.distance[0]**2+self.distance[1]**2)**0.5
        if self.d<200:
            self.aRight=self.distance[0]/self.d*3
            self.aDown=self.distance[1]/self.d*3
            self.speedX += self.aRight
            self.speedY += self.aDown

        self.speed=(self.speedX**2+self.speedY**2)**0.5

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
        if x<30:
            x=30
            self.speedX*=-1
        if x>770:
            x=770
            self.speedX*=-1
        if y<30:
            y=30
            self.speedY*=-1
        if y>570:
            y=570
            self.speedY*=-1
        self.position = (x, y)
        self.image = self.src_image
        self.rect = self.image.get_rect()
        self.rect.center = self.position

# CREATE BALLS AND RUN

rect = screen.get_rect()
ball1 = MainBallSprite('images/ball1.png', rect.center)
ball2 = BallSprite('images/ball2.png', (200,250),ball1)
ball3 = BallSprite('images/ball3.png', (600,150),ball1)
ball4 = BallSprite('images/ball4.png', (500,500),ball1)
ball1_group = pygame.sprite.RenderPlain(ball1)
ball2_group = pygame.sprite.RenderPlain(ball2)
ball3_group = pygame.sprite.RenderPlain(ball3)
ball4_group = pygame.sprite.RenderPlain(ball4)

def start():
    global GameRunning
    global loseTime
    global beginTime
    global ball1,ball2,ball3,ball4
    global ball1_group,ball2_group,ball3_group,ball4_group
    if GameRunning == False:
        screen.blit(background, (0,0))
        screen.blit(intro, (0,0))
        ball1 = MainBallSprite('images/ball1.png', rect.center)
        ball2 = BallSprite('images/ball2.png', (200,250),ball1)
        ball3 = BallSprite('images/ball3.png', (600,150),ball1)
        ball4 = BallSprite('images/ball4.png', (500,500),ball1)
        ball1_group = pygame.sprite.RenderPlain(ball1)
        ball2_group = pygame.sprite.RenderPlain(ball2)
        ball3_group = pygame.sprite.RenderPlain(ball3)
        ball4_group = pygame.sprite.RenderPlain(ball4)
        ball2.speedX=-5
        ball2.speedY=-5
        ball3.speedX=5
        ball3.speedY=-5
        ball4.speedX=0
        ball4.speedY=5
        loseTime = 0
        GameRunning = True
        beginTime=pygame.time.get_ticks()

def twoBallDistance(ballA,ballB):
    distance=((ballA.position[0]-ballB.position[0])**2+(ballA.position[1]-ballB.position[1])**2)**0.5
    return distance

def collide(ball1,ball2,ball3,ball4):
    collide0=False
    if twoBallDistance(ball1,ball2)<65:
        collide0=True
    if twoBallDistance(ball1,ball3)<65:
        collide0=True
    if twoBallDistance(ball1,ball4)<65:
        collide0=True
    if twoBallDistance(ball2,ball3)<65:
        collide0=True
    if twoBallDistance(ball2,ball4)<65:
        collide0=True
    if twoBallDistance(ball3,ball4)<65:
        collide0=True
    return collide0

start()

while 1:

    # USER INPUT
    deltat = clock.tick(20)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT or event.key == K_d: ball1.k_right = down * 3
        elif event.key == K_LEFT or event.key == K_a: ball1.k_left = down * 3
        elif event.key == K_UP or event.key == K_w: ball1.k_up = down * 3
        elif event.key == K_DOWN or event.key == K_s: ball1.k_down = down * 3
        elif event.key == K_ESCAPE: sys.exit(0)
        elif event.key == K_SPACE: start()

    # RENDERING

    if collide(ball1,ball2,ball3,ball4)==False:

        ball1_group.clear(screen, background)
        ball2_group.clear(screen, background)
        ball3_group.clear(screen, background)
        ball4_group.clear(screen, background)
        ball1_group.clear(screen, intro)
        ball2_group.clear(screen, intro)
        ball3_group.clear(screen, intro)
        ball4_group.clear(screen, intro)
        ball1_group.update(deltat)
        ball2_group.update(deltat,ball1)
        ball3_group.update(deltat,ball1)
        ball4_group.update(deltat,ball1)
        ball1_group.draw(screen)
        ball2_group.draw(screen)
        ball3_group.draw(screen)
        ball4_group.draw(screen)

        #screen.blit(intro, (0,0))
        pygame.display.flip()
    else:
        loseTime+=1
        if loseTime == 1:
            screen.blit(lose,(0,0))
            endTime=pygame.time.get_ticks()
            pygame.display.set_caption("RepulsiveRuby v2.0 - Your record is %.2f s" %((endTime-beginTime)/1000.0) )
            collideSound.play()
        else:
            loseTime=2
        GameRunning = False
        pygame.display.flip()
