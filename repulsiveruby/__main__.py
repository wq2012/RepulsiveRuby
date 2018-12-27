# screen is 800*600
# ball image is 65*65

# initialization
import pygame
import sys
import os
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.locals import K_d, K_a, K_w, K_s, K_ESCAPE, K_SPACE

from repulsiveruby import physics
from repulsiveruby import sprites


current_script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_script_dir, "images")
sounds_dir = os.path.join(current_script_dir, "sounds")
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
os.environ["SDL_VIDEO_WINDOW_POS"] = "100,100"
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("RepulsiveRuby v2.0 - developed by Quan Wang")
background = pygame.image.load(images_dir + "/background.png")
intro = pygame.image.load(images_dir + "/intro.png")
lose = pygame.image.load(images_dir + "/lose.png")
screen.blit(background, (0, 0))
screen.blit(intro, (0, 0))
loseTime = 0
GameRunning = False
beginTime = 0
endTime = 0
music = pygame.mixer.Sound(sounds_dir + "/music.wav")
collideSound = pygame.mixer.Sound(sounds_dir + "/collide.wav")
music.play(-1)


# CREATE BALLS AND RUN


rect = screen.get_rect()
ball1 = sprites.MainBallSprite(images_dir + "/ball1.png", rect.center)
ball2 = sprites.BallSprite(images_dir + "/ball2.png", (200, 250), ball1)
ball3 = sprites.BallSprite(images_dir + "/ball3.png", (600, 150), ball1)
ball4 = sprites.BallSprite(images_dir + "/ball4.png", (500, 500), ball1)
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
        screen.blit(background, (0, 0))
        screen.blit(intro, (0, 0))
        ball1 = sprites.MainBallSprite(images_dir + "/ball1.png", rect.center)
        ball2 = sprites.BallSprite(
            images_dir + "/ball2.png", (200, 250), ball1)
        ball3 = sprites.BallSprite(
            images_dir + "/ball3.png", (600, 150), ball1)
        ball4 = sprites.BallSprite(
            images_dir + "/ball4.png", (500, 500), ball1)
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
    deltat = clock.tick(20)
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

        ball1_group.clear(screen, background)
        ball2_group.clear(screen, background)
        ball3_group.clear(screen, background)
        ball4_group.clear(screen, background)
        ball1_group.clear(screen, intro)
        ball2_group.clear(screen, intro)
        ball3_group.clear(screen, intro)
        ball4_group.clear(screen, intro)
        ball1_group.update(deltat)
        ball2_group.update(deltat, ball1)
        ball3_group.update(deltat, ball1)
        ball4_group.update(deltat, ball1)
        ball1_group.draw(screen)
        ball2_group.draw(screen)
        ball3_group.draw(screen)
        ball4_group.draw(screen)

        # screen.blit(intro, (0,0))
        pygame.display.flip()
    else:
        loseTime += 1
        if loseTime == 1:
            screen.blit(lose, (0, 0))
            endTime = pygame.time.get_ticks()
            pygame.display.set_caption(
                "RepulsiveRuby v2.0 - Your record is %.2f s" % (
                    (endTime-beginTime)/1000.0))
            collideSound.play()
        else:
            loseTime = 2
        GameRunning = False
        pygame.display.flip()
