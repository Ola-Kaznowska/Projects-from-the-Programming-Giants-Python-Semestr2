import sys
import pygame

# Inicjalizacja i ustawienia
pygame.init()
szerokosc, wysokosc = 400, 450
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Tamagotchi")

# Kolory
kolor_tla = (200, 200, 200) # jasnoszary
kolor_czarny = (0, 0, 0)
kolor_bialy = (255, 255, 255)
kolor_zielony = (0, 255, 0)
kolor_zolty = (255, 255, 0)
kolor_czerwony = (255, 0, 0)

# Czcionka
czcionka = pygame.font.SysFont("Comic Sans", 20)


# Klasa zwierzątka
class Tamagotchi:
    def __init__(self):
        self.poziom_glodu = 50
        self.poziom_szczescia = 50
    
    def nakarm(self):
        self.poziom_glodu += 10

    def pobaw_sie(self):
        self.poziom_szczescia += 10
        
    def aktualizuj(self):
        self.poziom_glodu -= 0.1
        self.poziom_szczescia -= 0.1


# Funkcje pomocnicze
def okresl_kolor(poziom):
    if poziom > 70:
        return kolor_zielony
    
    if 30 <= poziom <= 70:
        return kolor_zolty
    
    return kolor_czerwony


# Inicjalizacja Tamagotchi
tamagotchi = Tamagotchi()

wesoly = pygame.image.load('assets/happy.jpg')
wesoly = pygame.transform.scale(wesoly, (150, 150))
neutralny = pygame.image.load('assets/neutral.jpg')
neutralny = pygame.transform.scale(neutralny, (150, 150))
smutny = pygame.image.load('assets/sad.jpg')
smutny = pygame.transform.scale(smutny, (150, 150))

# Główna pętla gry
while True:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE: # klawisz Escape
                pygame.quit()  # zamyka okno gry
                sys.exit()     # kończy wykonywanie programu
        elif zdarzenie.type == pygame.QUIT: # przycisk zamykający okno X
            pygame.quit()
            sys.exit()
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            if przycisk_nakarm.collidepoint(zdarzenie.pos):
                tamagotchi.nakarm()
            elif przycisk_pobaw.collidepoint(zdarzenie.pos):
                tamagotchi.pobaw_sie()
            
    tamagotchi.aktualizuj()
    
    ekran.fill(kolor_tla)
    
    nastroj = tamagotchi.poziom_glodu + tamagotchi.poziom_szczescia
    if nastroj > 120:
        ekran.blit(wesoly, (125, 135))
    elif nastroj > 60:
        ekran.blit(neutralny, (125, 135))
    else:
        ekran.blit(smutny, (125, 135))
    
    # Interfejs
    ## szczęście - pasek i napis
    kolor_szczescie = okresl_kolor(tamagotchi.poziom_szczescia)
    pygame.draw.rect(ekran, kolor_szczescie,
        pygame.Rect(50, 50, tamagotchi.poziom_szczescia * 2, 20))
    tekst_szczescie = czcionka.render("Szczęście", True, kolor_czarny)
    ekran.blit(tekst_szczescie, (50, 20))

    ## głód - pasek i napis
    kolor_glod = okresl_kolor(tamagotchi.poziom_glodu)
    pygame.draw.rect(ekran, kolor_glod,
        pygame.Rect(50, 100, tamagotchi.poziom_glodu * 2, 20))
    tekst_glod = czcionka.render("Głód", True, kolor_czarny)
    ekran.blit(tekst_glod, (50, 70))
    
    ## przyciski Nakarm i Pobaw się
    przycisk_nakarm = pygame.Rect(25, 300, 150, 50)
    przycisk_pobaw = pygame.Rect(225, 300, 150, 50)
    pygame.draw.rect(ekran, kolor_bialy, przycisk_nakarm, 3)
    pygame.draw.rect(ekran, kolor_bialy, przycisk_pobaw, 3)
    
    ### teskt przycisków
    tekst_nakarm = czcionka.render("Nakarm", True, kolor_czarny)
    tekst_pobaw = czcionka.render("Pobaw się", True, kolor_czarny)

    tekst_szer_nakarm, tekst_wys_nakarm = tekst_nakarm.get_size()
    tekst_szer_pobaw, tekst_wys_pobaw = tekst_pobaw.get_size()

    ekran.blit(tekst_nakarm, (przycisk_nakarm.x + (przycisk_nakarm.width - tekst_szer_nakarm) // 2, przycisk_nakarm.y + (przycisk_nakarm.height - tekst_wys_nakarm) // 2))
    ekran.blit(tekst_pobaw, (przycisk_pobaw.x + (przycisk_pobaw.width - tekst_szer_pobaw) // 2, przycisk_pobaw.y + (przycisk_pobaw.height - tekst_wys_pobaw) // 2))


    pygame.display.flip()
    pygame.time.Clock().tick(30)
    
    

        