from Organizm import Organizm
from Punkt import Punkt
from Zwierze import Zwierze


class Zolw(Zwierze):
    __ZASIEG_RUCHU_ZOLWIA = 1
    __SZANSA_NA_RUCH_ZOLWIA = 4
    __SILA_ZOLWIA = 2
    __INICJATYWA_ZOLWIA = 1
    __KOLOR_ZOLWIA = "#017d37"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.ZOLW, swiat, pozycja, turaUrodzenia, self.__SILA_ZOLWIA,
                         self.__INICJATYWA_ZOLWIA, self.__KOLOR_ZOLWIA, self.__ZASIEG_RUCHU_ZOLWIA,
                         self.__SZANSA_NA_RUCH_ZOLWIA)

    def nazwa(self):
        return "Zolw"
