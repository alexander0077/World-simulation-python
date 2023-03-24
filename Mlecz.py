import random

from Organizm import Organizm
from Roslina import Roslina


class Mlecz(Roslina):
    __SILA_MLECZA = 0
    __INICJATYWA_MLECZA = 0
    __SZANSA_NA_ROZPRZESTRZENIANIE_MLECZA = 8  # wartosc w procentach
    __KOLOR_MLECZA = "#fffd75"
    __PROBY_ROZPRZESTRZENIENIA_MLECZA = 3

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.MLECZ, swiat, pozycja, turaUrodzenia, self.__SILA_MLECZA,
                         self.__INICJATYWA_MLECZA, self.__KOLOR_MLECZA, self.__SZANSA_NA_ROZPRZESTRZENIANIE_MLECZA)

    def nazwa(self):
        return "Mlecz"

    def akcja(self):
        for i in range(self.__PROBY_ROZPRZESTRZENIENIA_MLECZA):
            tmp = random.randint(0, 99)
            if tmp < self.__SZANSA_NA_ROZPRZESTRZENIANIE_MLECZA:
                self.rozprzestrzenianie()