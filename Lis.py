import random

from Organizm import Organizm
from Punkt import Punkt
from Zwierze import Zwierze


class Lis(Zwierze):
    __ZASIEG_RUCHU_LISA = 1
    __SZANSA_NA_RUCH_LISA = 1
    __SILA_LISA = 3
    __INICJATYWA_LISA = 7
    __KOLOR_LISA = "#f5bd05"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.LIS, swiat, pozycja, turaUrodzenia, self.__SILA_LISA,
                         self.__INICJATYWA_LISA, self.__KOLOR_LISA, self.__ZASIEG_RUCHU_LISA,
                         self.__SZANSA_NA_RUCH_LISA)

    def nazwa(self):
        return "Lis"

    def akcja(self):
        nowy_punkt = self.nowyPunkt()
        if not nowy_punkt == self.getPozycja():
            self.przesunOrganizm(nowy_punkt)
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() +
                self.nazwa() + " przemieszcza sie na pozycje [" + str(
                    self.getPozycja().getX()) + "," + str(self.getPozycja().getY()) + "] \n")

    def nowyPunkt(self):
        stary_punkt = self.getPozycja()
        czy_jest_wolne_pole = False
        tmp = Punkt(stary_punkt.getX(), stary_punkt.getY())
        for i in range(3):
            for j in range(3):
                tmp.setX(tmp.getX() + j - 1)
                tmp.setY(tmp.getY() + i - 1)
                if self.getSwiat().getRozmiarX() > tmp.getX() > -1 and self.getSwiat().getRozmiarY() > tmp.getY() > -1:
                    if not self.getSwiat().getCzyPoleJestZajete(tmp):
                        czy_jest_wolne_pole = True
                        break

        if not czy_jest_wolne_pole:
            return stary_punkt
        else:
            while True:
                vecX = random.randint(0, 2) - 1
                vecY = random.randint(0, 2) - 1
                if vecX != 0 or vecY != 0:
                    if self.getSwiat().getRozmiarX() > stary_punkt.getX() + vecX > -1 and self.getSwiat().getRozmiarY() > stary_punkt.getY() + vecY > -1:
                        tmp = Punkt(stary_punkt.getX() + vecX, stary_punkt.getY() + vecY)
                        if not self.getSwiat().getCzyPoleJestZajete(tmp):
                            return tmp