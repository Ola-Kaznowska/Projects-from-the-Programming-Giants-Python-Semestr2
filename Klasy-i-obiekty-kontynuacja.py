class Samochod:
    marka = "Seat"
    model = ""
    licznik = 0

    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        Samochod.licznik += 1

s = Samochod("Audi", "a4")
sa = Samochod("Audi", "a4")
saa = Samochod("Audi", "a4")


print(Samochod.licznik)