lista = [1,2,3,4,5] #lista
list.append(10)


for e in lista:
    print(e)
    
    
    
    
    osoba = { #słownik
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "wiek": 30,
        "adres": {
        "ulica": "Kwiatowa",
        "nr": 43,
        "miasto": "Krakow"
        
        },
        "telefon": "436887658787",
        "liczby": [1,2,3,4]
    }
    
    
    
    osoba ["wiek"] = 22
    osoba ["telefon"] = "46633886678"
    print(osoba["adres"])
    
    
    
    
    
    for klucz, wartosc in osoba.items():
        print(klucz, wartosc)
    
    
    
    
     