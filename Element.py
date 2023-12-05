import pygame
 
#klasa pomocnicza obraz
class Obraz(pygame.sprite.Sprite):
    def __init__(self, sciezka):
        super().__init__()
        self.obraz = pygame.image.load(sciezka)
 
#klasa bazowa
class Element():
    def __init__(self, typ):
        #wskaźnik wybranego elementu ubioru
        self.wybrany = 0
        #lista obrazów
        self.listaObrazow = []
        #użycie pętli aby zaczytać wszystkie obrazu z folderu
        for i in range(1, 4):
            sciezka = f'images/{typ}{i}.png'
            wczytany_obraz = Obraz(sciezka)
            self.listaObrazow.append(wczytany_obraz)
    
    def wybierzNastepny(self):
        self.wybrany += 1
        if self.wybrany > 2:
            self.wybrany = 0
    
    def wybranyObraz(self):
        return self.listaObrazow[self.wybrany].obraz
 
 
class NakrycieGlowy(Element):
    def __init__(self):
        super().__init__('head')
 
class UbranieElement(Element):
    def __init__(self):
        super().__init__('body')
        
class OczyElement(Element):
    def __init__(self):
        super().__init__('eye')
        
class BronElement(Element):
    def __init__(self):
        super().__init__('weapon')