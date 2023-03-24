import random

from Organizm import Organizm
from Roslina import Roslina


class Trawa(Roslina):
    __SILA_TRAWY = 0
    __INICJATYWA_TRAWY = 0
    __SZANSA_NA_ROZPRZESTRZENIANIE_TRAWY = 8  # wartosc w procentach
    __KOLOR_TRAWY = "#80eb7c"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.TRAWA, swiat, pozycja, turaUrodzenia, self.__SILA_TRAWY,
                         self.__INICJATYWA_TRAWY, self.__KOLOR_TRAWY, self.__SZANSA_NA_ROZPRZESTRZENIANIE_TRAWY)

    def nazwa(self):
        return "Trawa"


