from enum import Enum
from random import random

from Punkt import Punkt
from abc import ABC, abstractmethod


class Organizm(ABC):
    LICZBA_GATUNKOW = 11  # ILOSC GATUNKOW DO ZMIENIANIA
    MINIMALNY_WIEK_ROZMNAZANIA = 0

    class Gatunek(Enum):
        CZLOWIEK = 0
        WILK = 1
        OWCA = 2
        LIS = 3
        ZOLW = 4
        ANTYLOPA = 5
        TRAWA = 6
        MLECZ = 7
        GUARANA = 8
        WILCZE_JAGODY = 9
        BARSZCZ_SOSNOWSKIEGO = 10
        CYBER_OWCA = 11

    def __init__(self, typOrganizmu, swiat, pozycja, tura_urodzenia, sila, inicjatywa, kolor, czy_jest_zwierzeciem):
        self.__typ = typOrganizmu
        self.__swiat = swiat
        self.__pozycja = pozycja
        self.__tura_urodzenia = tura_urodzenia
        self.__sila = sila
        self.__inicjatywa = inicjatywa
        self.__czy_zyje = True
        self.__kolor = kolor
        self.__czy_jest_zwierzeciem = czy_jest_zwierzeciem

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, inny):
        pass

    @abstractmethod
    def nazwa(self):
        pass

    def przesunOrganizm(self, gdzie):
        self.__swiat.getTablica()[self.__pozycja.getY()][self.__pozycja.getX()] = None
        self.__swiat.getTablica()[gdzie.getY()][gdzie.getX()] = self
        self.__pozycja.setX(gdzie.getX())
        self.__pozycja.setY(gdzie.getY())

    # GETERY I SETTERY

    def setCzyZyje(self, zyje):
        self.__czy_zyje = zyje

    def getCzyZyje(self):
        return self.__czy_zyje

    def getTypOrganizmu(self):
        return self.__typ

    def setTypOrganizmu(self, typOrganizmu):
        self.__typ = typOrganizmu

    def getPozycja(self):
        return Punkt(self.__pozycja.getX(), self.__pozycja.getY())

    def setPozycja(self, x, y):
        self.__pozycja.setX(x)
        self.__pozycja.setY(y)

    def getSwiat(self):
        return self.__swiat

    def setSwiat(self, swiat):
        self.__swiat = swiat

    def getTuraUrodzenia(self):
        return self.__tura_urodzenia

    def setTuraUrodzenia(self, tura_urodzenia):
        self.__tura_urodzenia = tura_urodzenia

    def getSila(self):
        return self.__sila

    def setSila(self, sila):
        self.__sila = sila

    def getInicjatywa(self):
        return self.__inicjatywa

    def setInicjatywa(self, inicjatywa):
        self.__inicjatywa = inicjatywa

    def getTyp(self):
        return self.__typ

    def getKolor(self):
        return self.__kolor

    def getCzyJestZwierzeciem(self):
        return self.__czy_jest_zwierzeciem

    @staticmethod
    def czyRoslinaWzmacnia(roslina):
        if roslina.getTypOrganizmu() == Organizm.Gatunek.GUARANA:
            return True
        else:
            return False

    @staticmethod
    def czyRoslinaJestTrujaca(inny):
        if inny.getTypOrganizmu() == Organizm.Gatunek.WILCZE_JAGODY or inny.getTypOrganizmu() == Organizm.Gatunek.BARSZCZ_SOSNOWSKIEGO:
            return True
        else:
            return False
