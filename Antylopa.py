import random

from Organizm import Organizm
from Punkt import Punkt
from Zwierze import Zwierze


class Antylopa(Zwierze):
    __ZASIEG_RUCHU_ANTYLOPY = 1
    __SZANSA_NA_RUCH_ANTYLOPY = 1
    __SILA_ANTYLOPY = 3
    __INICJATYWA_ANTYLOPY = 7
    __KOLOR_ANTYLOPY = "#52462b"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.ANTYLOPA, swiat, pozycja, turaUrodzenia, self.__SILA_ANTYLOPY,
                         self.__INICJATYWA_ANTYLOPY, self.__KOLOR_ANTYLOPY, self.__ZASIEG_RUCHU_ANTYLOPY,
                         self.__SZANSA_NA_RUCH_ANTYLOPY)

    def nazwa(self):
        return "Antylopa"