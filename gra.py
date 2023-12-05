import pygame
import random
import time
from Kierunek import Kierunek
from Waz import Waz
from Jablko import Jablko
 
#szerokość i wysokość ekranu
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608
Punkty = 0
 
#stworzenie tla
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0, 20), random.randrange(0,20), random.randrange(0,20))
       
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))
 
#ustawienia
pygame.init()
pygame.font.init()
#obiekt ekranu i zegara
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
#obiekt czcionki
moja_czcionka = pygame.font.SysFont('Comic Sans MS', 24)
 
#Wąż
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)
 
#jabłka
jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)
 
gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_w:
                waz.zmien_kierunek(Kierunek.GORA)
            if zdarzenie.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)
            if zdarzenie.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)
            if zdarzenie.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)
 
        elif zdarzenie.type == PORUSZ_WEZEM:
            waz.aktualizuj()
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        
    #sprawdzenie czy glowa weza jest na jablku
    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablko = Jablko()
        jablka.add(jablko)
        #SCORE += 1
    
    #rysowanie tła
    ekran.blit(tlo, (0, 0))
    #rysowanie segmentow
    waz.rysuj_segmenty(ekran)
    #rysowanie glłowy węża
    ekran.blit(waz.obraz, waz.rect)
    #rysowanie jablek
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)
    #wyswietlenie wyniku
    tekst_z_wynikiem = moja_czcionka.render(f'Wynik: {Punkty}', False, (0, 0, 0))
    ekran.blit(tekst_z_wynikiem, (16, 16))
    #sprawdź czy koniec gry
    if waz.sprawdz_kolizje():
        tekst_z_przegrana = moja_czcionka.render('Przegrana', False, (200,0,0))
        ekran.blit(tekst_z_przegrana, (SZEROKOSC_EKRANU/2-50, WYSOKOSC_EKRANU/2))
        gra_dziala = False
    
    pygame.display.flip()
    zegar.tick(30)
 
time.sleep(3)
pygame.quit()