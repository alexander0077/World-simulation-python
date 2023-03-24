import random

from Organizm import Organizm
from Punkt import Punkt


class Zwierze(Organizm):

    def __init__(self, typOrganizmu, swiat, pozycja, turaUrodzenia, sila, inicjatywa, kolor, zasieg_ruchu,
                 szansa_na_ruch):
        super().__init__(typOrganizmu, swiat, pozycja, turaUrodzenia, sila, inicjatywa, kolor, True)
        self.__zasieg_ruchu = zasieg_ruchu
        self.__szansa_na_ruch = szansa_na_ruch

    def akcja(self):
        tmp = random.randint(0, self.getSzansaNaRuch() - 1)
        if tmp == 0:
            for i in range(self.getZasiegRuchu()):
                nowy_punkt = self.nowyPunkt(self.getPozycja())

                if self.getSwiat().getCzyPoleJestZajete(nowy_punkt):
                    if self.czyMozeUciecOdWalki(nowy_punkt):
                        self.ucieczkaOdWalki(nowy_punkt)
                    else:
                        self.kolizja(self.getSwiat().getCoJestNaPolu(nowy_punkt))
                else:
                    self.przesunOrganizm(nowy_punkt)
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() +
                        self.nazwa() + " przemieszcza sie na pozycje [" + str(
                            self.getPozycja().getX()) + "," + str(self.getPozycja().getY()) + "] \n")

    def kolizja(self, inny):
        if inny.getTypOrganizmu() == self.getTyp():
            if self.getTyp() != Organizm.Gatunek.CZLOWIEK:
                self.rozmnazanie(inny)
        else:
            if self.czyOdbijeAtak(inny):
                self.odbijAtak(inny)
            elif self.getSila() < inny.getSila():
                if self.czyRoslinaJestTrujaca(inny):
                    self.zwierzeSieStrulo(inny)
                else:
                    self.getSwiat().usunOrganizm(self)
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() + inny.nazwa() + " (sila: " + str(
                            inny.getSila()) + ") zabija " + self.nazwa() + " (sila: " + str(
                            self.getSila()) + ") na polu " + "[" + str(inny.getPozycja().getX()) + "," + str(
                            inny.getPozycja().getY()) + "] \n")
            else:
                tmp = inny.getPozycja()
                if inny.getCzyJestZwierzeciem():
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() + self.nazwa() + " (sila: " + str(
                            self.getSila()) + ") zabija " + inny.nazwa() + " (sila: " + str(
                            inny.getSila()) + ") na polu " + "[" + str(tmp.getX()) + "," + str(tmp.getY()) + "] \n")
                else:
                    self.getSwiat().setKomentarze(
                        self.getSwiat().getKomentarze() + self.nazwa() + " zjada " +
                        inny.nazwa() + " na polu [" + str(tmp.getX()) + "," + str(tmp.getY()) + "]")
                    if self.czyRoslinaWzmacnia(inny): self.organizmSieWzmacnia()
                    self.getSwiat().setKomentarze(self.getSwiat().getKomentarze() + "\n")

                self.getSwiat().usunOrganizm(inny)
                self.przesunOrganizm(tmp)

    def rozmnazanie(self, inny):
        nr_tury = self.getSwiat().getNumerTury()
        swiat = self.getSwiat()
        nowe_pole = Punkt(-1, -1)
        if nr_tury - self.getTuraUrodzenia() > self.MINIMALNY_WIEK_ROZMNAZANIA and nr_tury - inny.getTuraUrodzenia() > self.MINIMALNY_WIEK_ROZMNAZANIA:
            if self.getSwiat().czyJestWolnePoleObok(self.getPozycja()):
                if swiat.czyJestWolnePoleObok(self.getPozycja()):
                    tmp = random.randint(0, 1)
                    if tmp == 0:
                        nowe_pole = swiat.wolnePoleObok(self.getPozycja())
                    else:
                        nowe_pole = swiat.wolnePoleObok(inny.getPozycja())
                else:
                    nowe_pole = swiat.wolnePoleObok(self.getPozycja())
            elif not swiat.czyJestWolnePoleObok(self.getPozycja()):
                self.getSwiat().setKomentarze(
                    self.getSwiat().getKomentarze() +
                    self.nazwa() + " nie moze sie rozmnozyc bo nie ma miejsca wokol pola [" + str(
                        self.getPozycja().getX()) + "," + str(self.getPozycja().getY())
                    + "] oraz [" + str(inny.getPozycja().getX()) + "," + str(inny.getPozycja().getY()) + "] \n")
            else:
                nowe_pole = swiat.wolnePoleObok(inny.getPozycja())
        else:
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() + self.nazwa() + " nie moze sie rozmnozyc bo jeden z organizmow jest "
                                                                 "za mlody na polu " + "[ "
                + str(self.getPozycja().getX()) + "," + str(self.getPozycja().getY()) + "] \n")
        if nowe_pole.getX() > -1:
            tmp = self.getSwiat().getSpawner().stworzOrganizm(self.getTypOrganizmu(), self.getSwiat(), nowe_pole)
            swiat.dodajOrganizm(tmp)
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() + self.nazwa() + " narodzil sie na polu [" + str(
                    nowe_pole.getX()) + "," + str(nowe_pole.getY()) + "] \n")

    def nowyPunkt(self, stary_punkt):
        q = 0
        while q == 0:
            vecX = random.randint(-1, 1)
            vecY = random.randint(-1, 1)
            if self.getSwiat().getRozmiarX() - 1 >= stary_punkt.getX() + vecX >= 0 and self.getSwiat().getRozmiarY() - 1 >= stary_punkt.getY() + vecY >= 0 and vecY != 0 and vecX != 0:
                    stary_punkt.setX(stary_punkt.getX() + vecX)
                    stary_punkt.setY(stary_punkt.getY() + vecY)
                    q = 1

        return stary_punkt

    def ucieczkaOdWalki(self, nowy_punkt):
        tmp = random.randint(0, 1)
        if tmp == 0:
            self.kolizja(self.getSwiat().getCoJestNaPolu(nowy_punkt))
        else:
            nowy_punkt_po_uniku = self.getSwiat().wolnePoleObok(nowy_punkt)
            self.przesunOrganizm(nowy_punkt_po_uniku)
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() + "Antylopa unika walki z " + self.getSwiat().getCoJestNaPolu(
                    nowy_punkt).nazwa() + " na polu [" + str(nowy_punkt.getX()) + "," + str(
                    nowy_punkt.getY()) + "] i ucieka na pole " + "[" + str(self.getPozycja().getX()) + "," + str(
                    self.getPozycja().getY()) + "] \n")

    def organizmSieWzmacnia(self):
        self.setSila(self.getSila() + 3)
        self.getSwiat().setKomentarze(
            self.getSwiat().getKomentarze() + ", jego sila wzrasta o 3 i wynosi: " + str(self.getSila()))

    def czyMozeUciecOdWalki(self, nowy_punkt):
        if self.getTypOrganizmu() == Organizm.Gatunek.ANTYLOPA and self.getSwiat().getCoJestNaPolu(nowy_punkt).getCzyJestZwierzeciem(): return True
        return False

    def czyOdbijeAtak(self, inny):
        if inny.getTypOrganizmu() == Organizm.Gatunek.ZOLW and self.getSila() < 5:
            return True
        else:
            if inny.getTypOrganizmu() == Organizm.Gatunek.CZLOWIEK:
                if self.getSwiat().getCzlowiek().getCzySupermocDziala(): return True
        return False

    def odbijAtak(self, inny):
        if inny.getTypOrganizmu() == Organizm.Gatunek.ZOLW:
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() + "Zolw odbil " + self.nazwa() + " na polu [" + str(
                    self.getPozycja().getX()) + "," + str(self.getPozycja().getY()) + "] \n")
        else:
            nowy = self.getSwiat().wolnePoleObok(
                inny.getPozycja())  # nie musimy wywolywac wczesniej czy wolne pole istnieje bo na pewno istnieje
            self.przesunOrganizm(nowy)
            self.getSwiat().setKomentarze(
                self.getSwiat().getKomentarze() + "Czlowiek za pomoca Tarczy Alzura odbil " +
                    self.nazwa() + " na pole [" + str(nowy.getX()) + "," + str(nowy.getY()) + "] \n")

    def zwierzeSieStrulo(self, inny):
        self.getSwiat().usunOrganizm(self)
        self.getSwiat().usunOrganizm(inny)
        self.getSwiat().setKomentarze(
            self.getSwiat().getKomentarze() +self.nazwa() + " zjada trujace " +
                inny.nazwa() + " na polu " + "[" + str(self.getPozycja().getX()) + "," + str(
                self.getPozycja().getY()) + "] i umiera \n")

    # GETTERY I SETTERY

    def getZasiegRuchu(self):
        return self.__zasieg_ruchu

    def setZasiegRuchu(self, zasieg):
        self.__zasieg_ruchu = zasieg

    def getSzansaNaRuch(self):
        return self.__szansa_na_ruch

    def setSzansaNaRuch(self, szansa):
        self.__szansa_na_ruch = szansa
