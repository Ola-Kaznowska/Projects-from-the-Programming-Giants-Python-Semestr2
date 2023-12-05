import pygame
import copy
from Kierunek import Kierunek
from Segment import Segment
 
class Waz(pygame.sprite.Sprite):
    def __init__(self):
        #oryginalny obraz glowy
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        #obraz pomocniczny, bedzie sie on zmienial przy zmienie kierunku gracza
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        #wspolrzednie glowy
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))
        #zmienne odpowiedzialne za kierunek, oraz nowy wyznaczony kierunek
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA
        #zapisana ostatnia pozycja weza, uzyjemy jej do zmiany pozycji segmentow
        self.ostatnia_pozycja = self.rect
        #informacje o dodaniu nowego segmentu oraz ich lista
        self.dodaj_segment = False
        self.segmenty = []
 
    def zmien_kierunek(self, kierunek):
        zmiana_mozliwa = True
        if kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:
            zmiana_mozliwa = False
        if kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False
        if kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False
        if zmiana_mozliwa: 
            self.nowy_kierunek = kierunek
 
    def sprawdz_kolizje(self):
        #ugryzienie ogona
        for segment in self.segmenty:
            if self.rect.topleft == segment.pozycja.topleft:
                return True
 
        #wyjscie poza ekran
        if self.rect.top < 0 or self.rect.top >= 608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True
        
        return False
 
    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value*-90))
 
        self.ostatnia_pozycja = copy.deepcopy(self.rect)
        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32, 0)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 32)
        
        #poruszanie segmentami
        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostatnia_pozycja)
 
        #dodawanie nowego segmentu
        if self.dodaj_segment:
            nowy_segment = Segment()
 
            nowa_pozycja = None
            if len(self.segmenty) > 0:
                nowa_pozycja = copy.deepcopy(self.segmenty[-1].pozycja)
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
            nowy_segment.pozycja = nowa_pozycja
            self.segmenty.append(nowy_segment)
            self.dodaj_segment = False
    
    def rysuj_segmenty(self, ekran):
        for segment in self.segmenty:
            ekran.blit(segment.obraz, segment.pozycja)
 
    def jedz_jablko(self):
        self.dodaj_segment = True