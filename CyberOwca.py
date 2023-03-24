import math

from Organizm import Organizm
from Punkt import Punkt
from Zwierze import Zwierze


class CyberOwca(Zwierze):
    __ZASIEG_RUCHU_CYBER_OWCY = 1
    __SZANSA_NA_RUCH_CYBER_OWCY = 1
    __SILA_CYBER_OWCY = 11
    __INICJATYWA_CYBER_OWCY = 4
    __KOLOR_CYBER_OWCY = "#8bf7f0"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.CYBER_OWCA, swiat, pozycja, turaUrodzenia, self.__SILA_CYBER_OWCY,
                         self.__INICJATYWA_CYBER_OWCY, self.__KOLOR_CYBER_OWCY, self.__ZASIEG_RUCHU_CYBER_OWCY,
                         self.__SZANSA_NA_RUCH_CYBER_OWCY)

    def nazwa(self):
        return "Cyber Owca"

    def liczOdleglosc(self, druga):
        x = (self.getPozycja().getX() - druga.getX()) ** 2
        y = (self.getPozycja().getY() - druga.getY()) ** 2
        return math.sqrt(x + y)

    def nowyPunktDlaCyberOwcy(self, stary_punkt):
        tmp = Punkt(0, 0)
        tmpDist = self.getSwiat().getRozmiarX() * self.getSwiat().getRozmiarY()
        for organizm in self.getSwiat().getOrganizmy():
            if organizm.getTypOrganizmu() == Organizm.Gatunek.BARSZCZ_SOSNOWSKIEGO:
                nowyDist = self.liczOdleglosc(organizm.getPozycja())
                if nowyDist < tmpDist:
                    tmpDist = nowyDist
                    tmp = organizm.getPozycja()
        roznicaX = tmp.getX() - stary_punkt.getX()
        roznicaY = tmp.getY() - stary_punkt.getY()
        if roznicaX ** 2 > roznicaY ** 2:
            if roznicaX > 0:
                stary_punkt.setX(stary_punkt.getX() + 1)
            else:
                stary_punkt.setX(stary_punkt.getX() - 1)
        else:
            if roznicaY > 0:
                stary_punkt.setY(stary_punkt.getY() + 1)
            else:
                stary_punkt.setY(stary_punkt.getY() - 1)

        return stary_punkt

    def nowyPunkt(self, stary_punkt):
        if self.getSwiat().czyJestBarszczNaPlanszy():
            return self.nowyPunktDlaCyberOwcy(stary_punkt)
        else:
            return super().nowyPunkt(stary_punkt)
