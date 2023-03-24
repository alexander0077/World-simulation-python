import random
from math import floor
import os
from tkinter import Button, Entry, Tk

from Organizm import Organizm
from Punkt import Punkt
from Spawn import Spawn


class Swiat:
    ZAPELNIENIE_SWIATA_NA_WEJSCIU = 20

    def __init__(self, rozmiar_X, rozmiar_Y):  # konstruktor NOWEGO swiata
        self.__tablica = None
        self.__rozmiar_X = rozmiar_X
        self.__rozmiar_Y = rozmiar_Y
        self.__numer_tury = 0
        self.__czy_koniec_gry = False
        self.__czy_czlowiek_zyje = True
        self.__organizmy = list()
        self.__komentarze = ""
        self.__czlowiek = None
        self.__spawner = Spawn()
        self.__swiat = self

        self.__tablica = [[None for i in range(rozmiar_X)] for j in range(rozmiar_Y)]

        for i in range(rozmiar_Y):
            for j in range(rozmiar_X):
                self.__tablica[i][j] = None

        self.generujSwiat()

    def generujSwiat(self):
        tmp = self.__spawner.stworzOrganizm(Organizm.Gatunek.WILK, self.__swiat, Punkt(0, 0))
        self.dodajOrganizm(tmp)
        tmp = self.__spawner.stworzOrganizm(Organizm.Gatunek.WILK, self.__swiat, Punkt(1, 0))
        self.dodajOrganizm(tmp)
        tmp = self.__spawner.stworzOrganizm(Organizm.Gatunek.WILK, self.__swiat, Punkt(0, 1))
        self.dodajOrganizm(tmp)
        tmp = self.__spawner.stworzOrganizm(Organizm.Gatunek.WILK, self.__swiat, Punkt(2, 0))
        self.dodajOrganizm(tmp)
        tmp = self.__spawner.stworzOrganizm(Organizm.Gatunek.WILK, self.__swiat, Punkt(2, 1))
        self.dodajOrganizm(tmp)
        # PREZENTACJA ROZMNAZANIA DODAC 5 WILKOW W ROGU

        ile_organizmow = floor(self.__rozmiar_X * self.__rozmiar_Y * self.ZAPELNIENIE_SWIATA_NA_WEJSCIU / 100)
        spawn_pozycja = self.losujWolnePole()

        tmp = self.__spawner.stworzOrganizm(Organizm.Gatunek.CZLOWIEK, self.__swiat, spawn_pozycja)
        self.dodajOrganizm(tmp)
        self.__czlowiek = tmp

        for i in range(ile_organizmow):
            spawn_pozycja = self.losujWolnePole()
            if spawn_pozycja.getX() == self.__rozmiar_X + 1 and spawn_pozycja.getY() == self.__rozmiar_Y + 1:
                return
            else:
                tmp = self.__spawner.stworzOrganizm(self.losowyTyp(), self.__swiat, spawn_pozycja)
                self.dodajOrganizm(tmp)
                self.__komentarze += (
                            tmp.nazwa() + " pojawil sie na polu: [" + str(tmp.getPozycja().getX()) + "," + str(
                        tmp.getPozycja().getY()) + "] \n")

    def losujWolnePole(self):
        wolne_pole = 1
        i = 0
        j = 0
        tmp = Punkt(0, 0)

        while i < self.__rozmiar_Y and wolne_pole != 0:
            while j < self.__rozmiar_X and wolne_pole == 0:
                if self.__tablica[i][j] is None:
                    wole_pole = wolne_pole + 1
                j = j + 1
            i = i + 1

        if wolne_pole != 0:
            q = 0
            while q == 0:
                x = random.randint(0, self.__rozmiar_X - 1)
                y = random.randint(0, self.__rozmiar_Y - 1)
                if self.__tablica[x][y] is None:
                    tmp.setY(x)
                    tmp.setX(y)
                    q = 1
        else:
            tmp.setY(self.__rozmiar_Y + 1)
            tmp.setX(self.__rozmiar_X + 1)

        return tmp

    def wykonajTure(self):
        self.sortujVector()
        for i in range(len(self.__organizmy)):
            if self.__organizmy[i].getCzyZyje() and self.__organizmy[i].getTuraUrodzenia() < self.__numer_tury:
                self.__organizmy[i].akcja()

        for i in range(len(self.__organizmy) - 1, -1, -1):
            if not self.__organizmy[i].getCzyZyje():
                del self.__organizmy[i]

        self.__numer_tury += 1
        # print(self.getKomentarze())
        # self.__komentarze = ""

    def sortujVector(self):
        self.__organizmy.sort(key=lambda org: org.getInicjatywa(), reverse=True)

    def czyJestWolnePoleObok(self, pole):
        for i in range(3):
            for j in range(3):
                y = pole.getY() + j - 1
                x = pole.getX() + i - 1
                if self.__rozmiar_Y > y > -1 and -1 < x < self.__rozmiar_X:
                    if self.__tablica[y][x] is None:
                        return True
        return False

    def wolnePoleObok(self, poleWejsciowe):
        wolne_pole = self.czyJestWolnePoleObok(poleWejsciowe)
        if wolne_pole:
            q = 0
            while q == 0:
                x = random.randint(0, 2) - 1 + poleWejsciowe.getX()
                y = random.randint(0, 2) - 1 + poleWejsciowe.getY()
                if self.__rozmiar_Y > y > -1 and -1 < x < self.__rozmiar_X:
                    if self.__tablica[y][x] is None:
                        return Punkt(x, y)
        return poleWejsciowe

    def usunOrganizm(self, organizm):
        self.__tablica[organizm.getPozycja().getY()][organizm.getPozycja().getX()] = None
        organizm.setCzyZyje(False)
        if organizm.getTypOrganizmu() == Organizm.Gatunek.CZLOWIEK:
            self.__czlowiek = None
            self.__czy_czlowiek_zyje = False

    def dodajOrganizm(self, organizm):
        self.__organizmy.append(organizm)
        self.__tablica[organizm.getPozycja().getY()][organizm.getPozycja().getX()] = organizm

    def losowyTyp(self):
        tmp = random.randint(1, Organizm.LICZBA_GATUNKOW)  # losowy typ oprocz czlowieka
        if tmp == 1:
            return Organizm.Gatunek.WILK
        elif tmp == 2:
            return Organizm.Gatunek.OWCA
        elif tmp == 3:
            return Organizm.Gatunek.LIS
        elif tmp == 4:
            return Organizm.Gatunek.ZOLW
        elif tmp == 5:
            return Organizm.Gatunek.ANTYLOPA
        elif tmp == 6:
            return Organizm.Gatunek.TRAWA
        elif tmp == 7:
            return Organizm.Gatunek.MLECZ
        elif tmp == 8:
            return Organizm.Gatunek.GUARANA
        elif tmp == 9:
            return Organizm.Gatunek.WILCZE_JAGODY
        elif tmp == 10:
            return Organizm.Gatunek.BARSZCZ_SOSNOWSKIEGO
        elif tmp == 11:
            return Organizm.Gatunek.CYBER_OWCA
        elif tmp == 0:
            return Organizm.Gatunek.CZLOWIEK

    def refactorEnum(self, tmp):
        if tmp == "Gatunek.WILK":
            return Organizm.Gatunek.WILK
        elif tmp == "Gatunek.OWCA":
            return Organizm.Gatunek.OWCA
        elif tmp == "Gatunek.LIS":
            return Organizm.Gatunek.LIS
        elif tmp == "Gatunek.ZOLW":
            return Organizm.Gatunek.ZOLW
        elif tmp == "Gatunek.ANTYLOPA":
            return Organizm.Gatunek.ANTYLOPA
        elif tmp == "Gatunek.TRAWA":
            return Organizm.Gatunek.TRAWA
        elif tmp == "Gatunek.MLECZ":
            return Organizm.Gatunek.MLECZ
        elif tmp == "Gatunek.GUARANA":
            return Organizm.Gatunek.GUARANA
        elif tmp == "Gatunek.WILCZE_JAGODY":
            return Organizm.Gatunek.WILCZE_JAGODY
        elif tmp == "Gatunek.BARSZCZ_SOSNOWSKIEGO":
            return Organizm.Gatunek.BARSZCZ_SOSNOWSKIEGO
        elif tmp == "Gatunek.CYBER_OWCA":
            return Organizm.Gatunek.CYBER_OWCA
        elif tmp == "Gatunek.CZLOWIEK":
            return Organizm.Gatunek.CZLOWIEK

    def saveSwiat(self, nazwa_pliku):
        file = open("zapisane_gry/" + nazwa_pliku + ".txt", "w")
        file.write(str(self.__rozmiar_X) + " " + str(self.__rozmiar_Y) + " " + str(self.__numer_tury) + " " +
                   str(self.__czy_czlowiek_zyje) + " " + str(self.__czy_koniec_gry) + '\n')
        for organizm in self.__organizmy:
            file.write(str(organizm.getTypOrganizmu()) + " " + str(organizm.getPozycja().getX()) + " " + str(organizm.getPozycja().getY()) + " ")
            file.write(str(organizm.getSila()) + " " + str(organizm.getTuraUrodzenia()) + " " + str(organizm.getCzyZyje()) + " ")
            if organizm.getTypOrganizmu() == Organizm.Gatunek.CZLOWIEK:
                file.write(str(organizm.getKierunekRuchu()) + " " + str(organizm.getCzyChceUzycSupermocy()) + " " + str(organizm.getDataUzyciaSuperMocy()) + " " + str(organizm.getCzySupermocDziala()))
            file.write('\n')

        file.close()

    def wczytajSwiat(self, nazwa_pliku):
        if os.path.isfile("zapisane_gry/" + nazwa_pliku + ".txt"):
            file = open("zapisane_gry/" + nazwa_pliku + ".txt", "r")
            self.__tablica = []
            self.__organizmy.clear()
            info = file.readline()
            info = info.split(' ')
            self.__rozmiar_X = int(info[0])
            self.__rozmiar_Y = int(info[1])
            self.__numer_tury = int(info[2])
            self.__czy_czlowiek_zyje = bool(info[3])
            self.__czy_koniec_gry = bool(info[4])
            self.__tablica = [[None for i in range(self.__rozmiar_X)] for j in range(self.__rozmiar_Y)]
            for i in range(self.__rozmiar_Y):
                for j in range(self.__rozmiar_X):
                    self.__tablica[i][j] = None
            eof = True
            while eof:
                info = file.readline()
                if not info:
                    eof = False #oznaczenie konca pliku
                else:
                    info = info.split(' ')
                    typ = self.refactorEnum(str(info[0]))
                    x = int(info[1])
                    y = int(info[2])
                    tmpOrganizm = self.__spawner.stworzOrganizm(typ, self, Punkt(x, y))
                    tmpOrganizm.setSila(int(info[3]))
                    tmpOrganizm.setTuraUrodzenia(int(info[4]))
                    tmpOrganizm.setCzyZyje(bool(info[5]))
                    if tmpOrganizm.getTypOrganizmu() == Organizm.Gatunek.CZLOWIEK:
                        tmpOrganizm.setKierunekRuchu(int(info[6]))
                        tmpOrganizm.setCzyChceUzycSupermocy(bool(info[7]))
                        tmpOrganizm.setDataUzyciaSuperMocy(int(info[8]))
                        tmpOrganizm.setCzySupermocDziala(bool(info[9]))
                    self.dodajOrganizm(tmpOrganizm)
            file.close()
        else:
            print("Plik nie istnieje")

    # GETERY I SETERY

    def setKomentarze(self, nowy):
        self.__komentarze = nowy

    def getKomentarze(self):
        return self.__komentarze

    def setRozmiarX(self, rozmiar_X):
        self.__rozmiar_X = rozmiar_X

    def setRozmiarY(self, rozmiar_Y):
        self.__rozmiar_Y = rozmiar_Y

    def getRozmiarX(self):
        return self.__rozmiar_X

    def getRozmiarY(self):
        return self.__rozmiar_Y

    def getCzyKoniecGry(self):
        return self.__czy_koniec_gry

    def setCzyKoniecGry(self, czy):
        self.__czy_koniec_gry = czy

    def getNumerTury(self):
        return self.__numer_tury

    def setNumerTury(self, numer):
        self.__numer_tury = numer

    def getCzyCzlowiekZyje(self):
        return self.__czy_czlowiek_zyje

    def setCzyCzlowiekZyje(self, czy_czlowiek_zyje):
        self.__czy_czlowiek_zyje = czy_czlowiek_zyje

    def setCzyKoniecGry(self, czy_jest_koniec_gry):
        self.__czy_koniec_gry = czy_jest_koniec_gry

    def getTablica(self):
        return self.__tablica

    def getCzyPoleJestZajete(self, stary_punkt):
        if self.__tablica[stary_punkt.getY()][stary_punkt.getX()] is None:
            return False
        else:
            return True

    def getCoJestNaPolu(self, pole):
        return self.__tablica[pole.getY()][pole.getX()]

    def getCzlowiek(self):
        return self.__czlowiek

    def getOrganizmy(self):
        return self.__organizmy

    def getSpawner(self):
        return self.__spawner

    def czyJestBarszczNaPlanszy(self):
        for organizm in self.__organizmy:
            if organizm.getTypOrganizmu() == Organizm.Gatunek.BARSZCZ_SOSNOWSKIEGO:
                return True
        return False
