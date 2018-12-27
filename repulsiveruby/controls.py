import sys

import pygame
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.locals import K_d, K_a, K_w, K_s, K_ESCAPE, K_SPACE


def detectKey(ballMain):
    for event in pygame.event.get():
        if not hasattr(event, "key"):
            continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT or event.key == K_d:
            ballMain.k_right = down * 3
        elif event.key == K_LEFT or event.key == K_a:
            ballMain.k_left = down * 3
        elif event.key == K_UP or event.key == K_w:
            ballMain.k_up = down * 3
        elif event.key == K_DOWN or event.key == K_s:
            ballMain.k_down = down * 3
        elif event.key == K_ESCAPE:
            sys.exit(0)
        elif event.key == K_SPACE:
            return "restart"
    return ""
