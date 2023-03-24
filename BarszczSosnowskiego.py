import random

from Organizm import Organizm
from Punkt import Punkt
from Roslina import Roslina


class BarszczSosnowskiego(Roslina):
    __SILA_BARSZCZU = 10
    __INICJATYWA_BARSZCZU = 0
    __SZANSA_NA_ROZPRZESTRZENIANIE_BARSZCZU = 5  # wartosc w procentach
    __KOLOR_BARSZCZU = "#9505f5"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.BARSZCZ_SOSNOWSKIEGO, swiat, pozycja, turaUrodzenia, self.__SILA_BARSZCZU,
                         self.__INICJATYWA_BARSZCZU, self.__KOLOR_BARSZCZU, self.__SZANSA_NA_ROZPRZESTRZENIANIE_BARSZCZU)

    def nazwa(self):
        return "Barszcz Sosnowskiego"

    def akcja(self):
        tmp = random.randint(0, 99)
        if tmp < self.__SZANSA_NA_ROZPRZESTRZENIANIE_BARSZCZU: self.rozprzestrzenianie()
        x = self.getPozycja().getX()
        y = self.getPozycja().getY()
        for i in range(3):
            for j in range(3):
                tmpX = x + i - 1
                tmpY = y + j - 1
                if self.getSwiat().getRozmiarY() > tmpY > -1 and -1 < tmpX < self.getSwiat().getRozmiarX():
                    cel = Punkt(tmpX, tmpY)
                    if self.getSwiat().getCzyPoleJestZajete(cel):
                        if self.getSwiat().getCoJestNaPolu(cel).getCzyJestZwierzeciem():
                            if not self.getSwiat().getCoJestNaPolu(cel).getTypOrganizmu() == Organizm.Gatunek.CYBER_OWCA:
                                self.getSwiat().setKomentarze(
                                    self.getSwiat().getKomentarze() + self.getSwiat().getCoJestNaPolu(cel).nazwa() + " pojawia sie za blisko Barszczu Sosnowskiego na polu [" + str(self.getSwiat().getCoJestNaPolu(cel).getPozycja().getX()) + "," + str(self.getSwiat().getCoJestNaPolu(cel).getPozycja().getY()) + "] i umiera \n")
                                self.getSwiat().usunOrganizm(self.getSwiat().getCoJestNaPolu(cel))


