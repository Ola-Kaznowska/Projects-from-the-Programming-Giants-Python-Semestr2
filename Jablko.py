import pygame
import random

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super(Jablko, self).__init__()
        self.obraz = pygame.image.load("images/apple.png")
        self.rect = pygame.Rect(random.randint(0,24)*32, random.randrange(0,24)*32,32,32)