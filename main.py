# Stwórz klasę Postac, która będzie klasą bazową dla klasy Przeciwnik i Gracz. W klasie Przeciwnik losujemy jego parametry oraz nazwę. W klasie przeciwnik 
#   powinny znaleść się metody odpowiadające za odpoczynek oraz za walkę.



from random import randint, choice
 
class Postac:
  def __init__(self):
    self.nazwa = ""
    self.zycie = 1
    self.max_zycie = 1
 
  def atakuj(self, przeciwnik):
    
    atak = randint(0, 3)
 
    if atak == 0: 
        print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}.")
    else: 
        print (f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadając {atak} obrazen")
        przeciwnik.zycie -= atak
 
 
class Przeciwnik(Postac):
    def __init__(self, gracz):
        super().__init__()
        self.nazwa = choice(['goblin', 'szkielet', 'zombie'])
        self.zycie = randint(1, gracz.zycie)
        
class Gracz(Postac):
    def __init__(self):
        super().__init__()
        self.zycie = 10
        self.max_zycie = 10
        self.nazwa = input('Podaj imie gracza: ')
    
    def odpoczynek(self):
        print(f'{self.nazwa} odpoczywa, zycie: {self.zycie}/{self.max_zycie}')
        self.zycie += 1
        if self.zycie > self.max_zycie:
            self.zycie = self.max_zycie
 
    def walka(self, przeciwnik):
        walka = True
        while walka:
            print(f'zycie gracza: {self.zycie}')
            print(f'zycie {przeciwnik.nazwa}: {przeciwnik.zycie}')
            akcja_walki = input('Akcja (atak, uciekaj): ')
            if akcja_walki == 'atak':
                self.atakuj(przeciwnik)
                if przeciwnik.zycie <= 0:
                    print(f'{self.nazwa} zabija {przeciwnik.nazwa}')
                    return True
                przeciwnik.atakuj(self)
            elif akcja_walki == 'uciekaj':
                print(f'{self.nazwa} ucieka')
                przeciwnik.atakuj(self)
                walka = False
            else:
                print('Nieznana akcja')
            
            if self.zycie <= 0:
                print(f'{self.nazwa} ginie')
                return False
        return True
 
gracz = Gracz()
gra = True
while gra:
    akcja = input('akcja (zwiedzaj, odpocznij): ')
 
    if akcja == 'zwiedzaj':
        if randint(0, 1) == 0:
            print(f'{gracz.nazwa} znalazl jaskinie')
        else:
            przeciwnik = Przeciwnik(gracz)
            print(f'{gracz.nazwa} natrafił na {przeciwnik.nazwa}')
            gra = gracz.walka(przeciwnik)       
    elif akcja == 'odpocznij':
        gracz.odpoczynek()
    else:
        print('Nieznana akcja')


   
 

            
            
    