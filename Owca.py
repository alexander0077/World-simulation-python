from Organizm import Organizm
from Zwierze import Zwierze


class Owca(Zwierze):
    __ZASIEG_RUCHU_OWCY = 1
    __SZANSA_NA_RUCH_OWCY = 1
    __SILA_OWCY = 4
    __INICJATYWA_OWCY = 4
    __KOLOR_OWCY = "#e1eff0"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.OWCA, swiat, pozycja, turaUrodzenia, self.__SILA_OWCY,
                         self.__INICJATYWA_OWCY, self.__KOLOR_OWCY, self.__ZASIEG_RUCHU_OWCY,
                         self.__SZANSA_NA_RUCH_OWCY)

    def nazwa(self):
        return "Owca"