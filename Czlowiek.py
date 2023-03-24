from Organizm import Organizm
from Zwierze import Zwierze


class Czlowiek(Zwierze):
    __ZASIEG_RUCHU_CZLOWIEKA = 1
    __SZANSA_NA_RUCH_CZLOWIEKA = 4
    __SILA_CZLOWIEKA = 5
    __INICJATYWA_CZLOWIEKA = 4
    __KOLOR_CZLOWIEKA = "#f50505"
    __NONE = 99
    __GORA = 101
    __DOL = 102
    __PRAWO = 103
    __LEWO = 104
    __CZAS_LADOWANIA_SUPERMOCY = 5
    __CZAS_DZIALANIA_SUPERMOCY = 5

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(Organizm.Gatunek.CZLOWIEK, swiat, pozycja, turaUrodzenia, self.__SILA_CZLOWIEKA,
                         self.__INICJATYWA_CZLOWIEKA, self.__KOLOR_CZLOWIEKA, self.__ZASIEG_RUCHU_CZLOWIEKA,
                         self.__SZANSA_NA_RUCH_CZLOWIEKA)
        self.__data_uzycia_supermocy = -11
        self.__czy_supermoc_dziala = False
        self.__chce_uzyc_supermocy = False
        self.__kierunek_ruchu = self.__NONE

    def nazwa(self):
        return "Czlowiek"

    def nowyPunkt(self, stary_punkt):
        q = 0
        vecX = 0
        vecY = 0
        while q == 0:
            if self.__kierunek_ruchu == self.__GORA:
                vecY = -1
            elif self.__kierunek_ruchu == self.__DOL:
                vecY = 1
            elif self.__kierunek_ruchu == self.__LEWO:
                vecX = -1
            elif self.__kierunek_ruchu == self.__PRAWO:
                vecX = 1
            else:
                pass
            if self.getSwiat().getRozmiarX() - 1 >= stary_punkt.getX() + vecX >= 0 and self.getSwiat().getRozmiarY() - 1 >= stary_punkt.getY() + vecY >= 0:
                stary_punkt.setX(stary_punkt.getX() + vecX)
                stary_punkt.setY(stary_punkt.getY() + vecY)
                q = 1
            else:
                q = 1
        return stary_punkt

    def akcja(self):
        if self.__chce_uzyc_supermocy:
            self.handlerMocy()
            self.__chce_uzyc_supermocy = False
        else:
            if self.getSwiat().getCzyCzlowiekZyje():
                nowy_punkt = self.nowyPunkt(self.getPozycja())

                if self.getSwiat().getCzyPoleJestZajete(nowy_punkt):
                    self.kolizja(self.getSwiat().getCoJestNaPolu(nowy_punkt))
                else:
                    self.przesunOrganizm(nowy_punkt)
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() +
                        self.nazwa() + " przemieszcza sie na pozycje [" + str(self.getPozycja().getX()) + "," + str(
                            self.getPozycja().getY()) + "] \n")

                if self.getSwiat().getNumerTury() - self.__data_uzycia_supermocy < self.__CZAS_DZIALANIA_SUPERMOCY:
                    if self.__czy_supermoc_dziala:
                        self.getSwiat().setKomentarze(
                            self.getSwiat().getKomentarze() +
                            "Tarcza Alzura jest jeszcze dostepna przez " + str(
                                self.__CZAS_DZIALANIA_SUPERMOCY - self.getSwiat().getNumerTury() + self.__data_uzycia_supermocy) + " rund \n")
                elif self.getSwiat().getNumerTury() - self.__data_uzycia_supermocy == self.__CZAS_DZIALANIA_SUPERMOCY:
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() + "Tarcza Alzura wlasnie przestala dzialac \n")
                    self.__czy_supermoc_dziala = False

    def handlerMocy(self):
        kiedy_uzyta_ostatnio = self.getSwiat().getNumerTury() - self.__data_uzycia_supermocy

        if self.getSwiat().getCzyCzlowiekZyje():
            if not self.__czy_supermoc_dziala:
                if kiedy_uzyta_ostatnio >= self.__CZAS_DZIALANIA_SUPERMOCY + self.__CZAS_LADOWANIA_SUPERMOCY:
                    self.__czy_supermoc_dziala = True
                    self.__data_uzycia_supermocy = self.getSwiat().getNumerTury()
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() + "Tarcza Alzura zostala wlaczona \n")
                else:
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() + "Tarcza Alzura bedzie dostepna za " + str(
                            self.__CZAS_LADOWANIA_SUPERMOCY + self.__CZAS_DZIALANIA_SUPERMOCY - kiedy_uzyta_ostatnio) + " ruchow \n")
            else:
                self.getSwiat().setKomentarze(
                    self.getSwiat().getKomentarze() + "Czlowiek nie moze uzyc supermocy, moc juz dziala \n")
        else:
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() + "Czlowiek nie moze uzyc supermocy, bo nie zyje \n")

    def setKierunekRuchu(self, gdzie):
        self.__kierunek_ruchu = gdzie

    def setCzyChceUzycSupermocy(self, czy):
        self.__chce_uzyc_supermocy = czy

    def getCzyChceUzycSupermocy(self):
        return self.__chce_uzyc_supermocy

    def getCzySupermocDziala(self):
        return self.__czy_supermoc_dziala

    def setCzySupermocDziala(self, set):
        self.__czy_supermoc_dziala = set

    def getKierunekRuchu(self):
        return self.__kierunek_ruchu

    def getDataUzyciaSuperMocy(self):
        return self.__data_uzycia_supermocy

    def setDataUzyciaSuperMocy(self, kiedy):
        self.__data_uzycia_supermocy = kiedy
