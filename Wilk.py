from Organizm import Organizm
from Zwierze import Zwierze


class Wilk(Zwierze):
    __ZASIEG_RUCHU_WILKA = 1
    __SZANSA_NA_RUCH_WILKA = 1
    __SILA_WILKA = 9
    __INICJATYWA_WILKA = 5
    __KOLOR_WILKA = "#2688eb"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.WILK, swiat, pozycja, turaUrodzenia, self.__SILA_WILKA,
                         self.__INICJATYWA_WILKA, self.__KOLOR_WILKA, self.__ZASIEG_RUCHU_WILKA,
                         self.__SZANSA_NA_RUCH_WILKA)

    def nazwa(self):
        return "Wilk"