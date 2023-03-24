import random

from Organizm import Organizm


class Roslina(Organizm):
    def __init__(self, typOrganizmu, swiat, pozycja, turaUrodzenia, sila, inicjatywa, kolor, szansa_na_rozprzestrzenianie):
        super().__init__(typOrganizmu, swiat, pozycja, turaUrodzenia, sila, inicjatywa, kolor, False)
        self.__szansa_na_rozprzestrzenianie = szansa_na_rozprzestrzenianie

    def akcja(self):
        tmp = random.randint(0, 99)
        if tmp < self.__szansa_na_rozprzestrzenianie:
            self.rozprzestrzenianie()

    def kolizja(self, inny):
        pass

    def rozprzestrzenianie(self):
        stary = self.getPozycja()
        nowy = self.getSwiat().wolnePoleObok(stary)
        if not nowy == stary:
            nowy_organizm = self.getSwiat().getSpawner().stworzOrganizm(self.getTypOrganizmu(), self.getSwiat(), nowy)
            self.getSwiat().dodajOrganizm(nowy_organizm)
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() + self.nazwa() + " rozprzestrzenil sie na pole [" + str(nowy.getX()) + "," + str(nowy.getY()) + "] \n")

    def getSzansaNaRozprzestrzenianie(self):
        return self.__szansa_na_rozprzestrzenianie
