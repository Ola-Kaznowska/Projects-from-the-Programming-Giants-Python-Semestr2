
import pygame
#zaimportowanie stworzonego pliku
import Element
 
#Utworzenie stałych
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600
#wczytanie obrazów do zmiennych
obraz_tla = pygame.image.load('images/background.png')
obraz_bazy_postaci = pygame.image.load('images/base.png')
 
#zainicjowanie pygame
pygame.init()
#utworzenie obiektów ekranu oraz zegara(FPS)
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
#dodanie obiektu czcionki
pygame.font.init()
moja_czcionka = pygame.font.SysFont('Comic Sans MS', 30)
 
 
#elementy stroju
nakrycie_glowy = Element.NakrycieGlowy()
ubranie_element = Element.UbranieElement()
oczy_element = Element.OczyElement()
bron_element = Element.BronElement()
 
def wypisz_tekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)
 
#główna pętla gry
gra_dziala = True
zapisywanie = False
while gra_dziala:
    for zdarzenie in pygame.event.get():
        #naciśnięcie klawiszy
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierzNastepny()
            if zdarzenie.key == pygame.K_w:
                oczy_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_e:
                ubranie_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_r:
                bron_element.wybierzNastepny()
            if zdarzenie.key == pygame.K_s:
                zapisywanie = True
        #naciśnięcie przycisku X aby zamknąć okno
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
 
    #rysowanie tła
    ekran.blit(obraz_tla, (0, 0))
    #rysowanie bazy postaci
    ekran.blit(obraz_bazy_postaci, (270, 130))
    #rysowanie elementów postaci
    ekran.blit(ubranie_element.wybranyObraz(), (270, 130))
    ekran.blit(oczy_element.wybranyObraz(), (270, 130))
    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(bron_element.wybranyObraz(), (270, 130))
 
    #zapisywanie
    if zapisywanie:
        pygame.image.save(ekran, 'postac.png')
        zapisywanie = False
 
    #wypisanie informacji o wybranym elemencie ekwipunku
    wypisz_tekst(ekran, f'[Q] Glowa: {nakrycie_glowy.wybrany}', (100, 100))
    wypisz_tekst(ekran, f'[W] Oczy: {oczy_element.wybrany}', (100, 140))
    wypisz_tekst(ekran, f'[E] Stroj: {ubranie_element.wybrany}', (100, 180))
    wypisz_tekst(ekran, f'[R] Bron: {bron_element.wybrany}', (100, 220))
    wypisz_tekst(ekran, f'[S] Zapisz', (100, 260))
 
    #wyczyszczenie ekranu
    pygame.display.flip()
    #ustalenie stałego fps na 30
    zegar.tick(30)
 
#koniec pętli while
 
#zamknięcie aplikacji
pygame.quit()