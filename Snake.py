import random
import time
import pygame
pygame.init()

window_x, window_y = 720, 480
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((window_x, window_y))
clock = pygame.time.Clock()
