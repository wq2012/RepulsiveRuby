from __future__ import print_function
import pygame
import os

# constants
SCREEN_W = 800
SCREEN_H = 600
CAPTION = "RepulsiveRuby - developed by Quan Wang"

current_script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_script_dir, "images")
sounds_dir = os.path.join(current_script_dir, "sounds")

# initialization
pygame.init()

pygame.mixer.pre_init(44100, 16, 2, 4096)
os.environ["SDL_VIDEO_WINDOW_POS"] = "100,100"
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# images
backgroundImage = pygame.image.load(os.path.join(images_dir, "background.png"))
introImage = pygame.image.load(os.path.join(images_dir, "intro.png"))
loseImage = pygame.image.load(os.path.join(images_dir, "lose.png"))
iconImage = pygame.image.load(os.path.join(images_dir, "icon.png"))
ballMainImage = pygame.image.load(os.path.join(images_dir, "ball_main.png"))
ball1Image = pygame.image.load(os.path.join(images_dir, "ball1.png"))
ball2Image = pygame.image.load(os.path.join(images_dir, "ball2.png"))
ball3Image = pygame.image.load(os.path.join(images_dir, "ball3.png"))
pygame.display.set_icon(iconImage)

# sounds
music = pygame.mixer.Sound(os.path.join(sounds_dir, "music.wav"))
collideSound = pygame.mixer.Sound(os.path.join(sounds_dir, "collide.wav"))
