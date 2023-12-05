import pygame
import copy
 
class Segment(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("images/segment.png")
        self.pozycja = pygame.Rect(-32, -32, 32, 32)
        self.ostatnia_pozycja = None
 
    def przesun(self, nowa_pozycja):
        self.ostatnia_pozycja = copy.deepcopy(self.pozycja)
        self.pozycja = copy.deepcopy(nowa_pozycja)