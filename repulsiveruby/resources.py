import pygame
import os

current_script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(current_script_dir, "images")
sounds_dir = os.path.join(current_script_dir, "sounds")

# initialization
pygame.init()

# screen is 800*600
pygame.mixer.pre_init(44100, 16, 2, 4096)
os.environ["SDL_VIDEO_WINDOW_POS"] = "100,100"
screen = pygame.display.set_mode((800, 600))

# images
background = pygame.image.load(images_dir + "/background.png")
intro = pygame.image.load(images_dir + "/intro.png")
lose = pygame.image.load(images_dir + "/lose.png")

# sounds
music = pygame.mixer.Sound(sounds_dir + "/music.wav")
collideSound = pygame.mixer.Sound(sounds_dir + "/collide.wav")

# ball image is 65*65
