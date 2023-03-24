from Organizm import Organizm
from Roslina import Roslina


class WilczeJagody(Roslina):
    __SILA_WILCZYCH_JAGOD = 99
    __INICJATYWA_WILCZYCH_JAGOD = 0
    __SZANSA_NA_ROZPRZESTRZENIANIE_WILCZYCH_JAGOD = 5  # wartosc w procentach
    __KOLOR_WILCZYCH_JAGOD = "#ed26c9"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.WILCZE_JAGODY, swiat, pozycja, turaUrodzenia, self.__SILA_WILCZYCH_JAGOD,
                         self.__INICJATYWA_WILCZYCH_JAGOD, self.__KOLOR_WILCZYCH_JAGOD, self.__SZANSA_NA_ROZPRZESTRZENIANIE_WILCZYCH_JAGOD)

    def nazwa(self):
        return "Wilcze Jagody"


