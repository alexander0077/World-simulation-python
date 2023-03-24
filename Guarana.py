from Organizm import Organizm
from Roslina import Roslina


class Guarana(Roslina):
    __SILA_GUARANY = 0
    __INICJATYWA_GUARANY = 0
    __SZANSA_NA_ROZPRZESTRZENIANIE_GUARANY = 5  # wartosc w procentach
    __KOLOR_GUARANY = "#cca0db"

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.GUARANA, swiat, pozycja, turaUrodzenia, self.__SILA_GUARANY,
                         self.__INICJATYWA_GUARANY, self.__KOLOR_GUARANY, self.__SZANSA_NA_ROZPRZESTRZENIANIE_GUARANY)

    def nazwa(self):
        return "Guarana"


