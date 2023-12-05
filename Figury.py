PI = 3.1415


class Figura():
    def wysPole(self):
        print(self.pole)
    
    def wysObwod(self):
        print(self.obwod)


class Kolo(Figura):
    def __init__(self, r):
        self.promien = r
        self.pole = PI * r * r
        self.obwod = 2 * PI * r

class Prostokat(Figura):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pole = x*y
        self.obwod = 2*x + 2*y
    
kolo1 = Kolo(4)
kolo1.wysObwod()
kolo1.wysPole()

kolo2 = Kolo(123)
kolo2.wy
kolo1 = Kolo(4)
kolo1.wysObwod()
kolo1.wysPole()

kolo2 = Kolo(123)
kolo2.wysObwod()
kolo2.wysPole()

pros1 = Prostokat(12, 5)
pros1.wysObwod()
pros1.wysPole()

pros2 = Prostokat(123, 178)
pros2.wysObwod()
pros2.wysPole()