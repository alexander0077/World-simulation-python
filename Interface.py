from tkinter import Tk

import tkinter as tk

from Punkt import Punkt
from Swiat import Swiat


class Interface:
    __SZEROKOSC_EKRANU = 900
    __WYSOKOSC_EKRANU = 600
    __SZEROKOSC_PRZYCISKU_MENU = 40
    __ODLEGLOSC_OD_PRAWEJ_KRAWEDZI_PRZYCISKU_MENU = 310
    __BACKGROUD_COLOR = '#adad9a'
    __BUTTONS_COLOR = '#d1c75a'
    __WYSOKOSC_PRZYCISKU = 4

    __NONE = 99
    __GORA = 101
    __DOL = 102
    __PRAWO = 103
    __LEWO = 104

    def __init__(self):
        self.rozmiar_X = 20
        self.rozmiar_Y = 20
        screen = Tk()
        screen.title('Programowanie Obiektowe - Projekt 3 - Aleksander Sarzyniak')
        screen.geometry(str(self.__SZEROKOSC_EKRANU) + "x" + str(self.__WYSOKOSC_EKRANU))
        screen.resizable(False, False)
        self.mainMenu(screen)


    def mainMenu(self, screen):
        for widgets in screen.winfo_children():
            widgets.destroy()
        screen.configure(bg=self.__BACKGROUD_COLOR)
        button_nowa_gra = tk.Button(screen, text="Nowa gra", fg="black", command=lambda: self.nowaGra(screen), height=self.__WYSOKOSC_PRZYCISKU, width=self.__SZEROKOSC_PRZYCISKU_MENU, bg=self.__BUTTONS_COLOR)
        button_nowa_gra.place(x=self.__ODLEGLOSC_OD_PRAWEJ_KRAWEDZI_PRZYCISKU_MENU, y=125)

        button_wczytaj_gre = tk.Button(screen, text="Wczytaj gre", fg="black", command=lambda: self.open_game(screen), height=self.__WYSOKOSC_PRZYCISKU,
                                    width=self.__SZEROKOSC_PRZYCISKU_MENU, bg=self.__BUTTONS_COLOR)
        button_wczytaj_gre.place(x=self.__ODLEGLOSC_OD_PRAWEJ_KRAWEDZI_PRZYCISKU_MENU, y=250)

        button_wyjdz = tk.Button(screen, text="Wyjdź", fg="black", command=quit, height=self.__WYSOKOSC_PRZYCISKU,
                                    width=self.__SZEROKOSC_PRZYCISKU_MENU, bg=self.__BUTTONS_COLOR)
        button_wyjdz.place(x=self.__ODLEGLOSC_OD_PRAWEJ_KRAWEDZI_PRZYCISKU_MENU, y=375)

        screen.mainloop()

    def nowaGra(self, screen):
        def podajSzerokosc():
            powiadomienie2 = tk.Tk()
            powiadomienie2.title('Podaj szerokość nowego świata')
            canvas1 = tk.Canvas(powiadomienie2, width=200, height=100)
            canvas1.pack()
            entry1 = tk.Entry(powiadomienie2)
            canvas1.create_window(100, 50, window=entry1)

            def zamknij():
                self.rozmiar_Y = int(entry1.get())
                powiadomienie2.destroy()
                self.rysujPlansze(screen)

            button_wczytaj_gre = tk.Button(powiadomienie2, text="Wprowadź wysokość", fg="black", command=zamknij,
                                           height=1,
                                           width=20, bg="white")
            button_wczytaj_gre.place(x=30, y=10)
            powiadomienie2.mainloop()

        powiadomienie = tk.Tk()
        powiadomienie.title('Podaj szerokość nowego świata')
        canvas1 = tk.Canvas(powiadomienie, width=200, height=100)
        canvas1.pack()
        entry1 = tk.Entry(powiadomienie)
        canvas1.create_window(100, 50, window=entry1)
        def zamknij():
            self.rozmiar_X = int(entry1.get())
            powiadomienie.destroy()
            podajSzerokosc()
        button_wczytaj_gre = tk.Button(powiadomienie, text="Wprowadź szerokość", fg="black", command=zamknij,
                                       height=1,
                                       width=20, bg="white")
        button_wczytaj_gre.place(x=30, y=10)
        powiadomienie.mainloop()

    def drawOrganizmy(self, screen, swiat, plansza):
        plansza.create_rectangle(0, 0, 600, 600, fill="white")
        dlugosc_jednego_x = 600 / swiat.getRozmiarX()
        dlugosc_jednego_y = 600 / swiat.getRozmiarY()
        for i in range(swiat.getRozmiarY()):
            for j in range(swiat.getRozmiarX()):
                if swiat.getCzyPoleJestZajete(Punkt(j, i)) and swiat.getCoJestNaPolu(Punkt(j, i)).getCzyZyje():
                    plansza.create_rectangle(dlugosc_jednego_x * j, dlugosc_jednego_y * i, dlugosc_jednego_x * (j+1), dlugosc_jednego_y * (i+1), fill=swiat.getCoJestNaPolu(Punkt(j, i)).getKolor())


    def drawLegenda(self, screen, swiat, legenda):
        button = tk.Button(legenda, text="Człowiek", bg="#f50505", width=17, height=1)
        button.place(x=10, y=10)
        button = tk.Button(legenda, text="Trawa", bg="#80eb7c", width=17, height=1)
        button.place(x=160, y=10)
        button = tk.Button(legenda, text="Wilk", bg="#2688eb", width=17, height=1)
        button.place(x=10, y=35)
        button = tk.Button(legenda, text="Mlecz", bg="#fffd75", width=17, height=1)
        button.place(x=160, y=35)
        button = tk.Button(legenda, text="Owca", bg="#e1eff0", width=17, height=1)
        button.place(x=10, y=60)
        button = tk.Button(legenda, text="Guarana", bg="#cca0db", width=17, height=1)
        button.place(x=160, y=60)
        button = tk.Button(legenda, text="Lis", bg="#f5bd05", width=17, height=1)
        button.place(x=10, y=85)
        button = tk.Button(legenda, text="Wilcze Jagody", bg="#ed26c9", width=17, height=1)
        button.place(x=160, y=85)
        button = tk.Button(legenda, text="Zółw", bg="#017d37", width=17, height=1)
        button.place(x=10, y=110)
        button = tk.Button(legenda, text="Barszcz Sosnowskiego", bg="#9505f5", width=17, height=1)
        button.place(x=160, y=110)
        button = tk.Button(legenda, text="Antylopa", bg="#52462b", width=17, height=1)
        button.place(x=10, y=135)
        button = tk.Button(legenda, text="Cyberowca", bg="#8bf7f0", width=17, height=1)
        button.place(x=160, y=135)
        button = tk.Button(legenda, text="Zapisz świat", bg="white", width=17, height=1, command=lambda : self.save(swiat))
        button.place(x=10, y=170)
        button = tk.Button(legenda, text="Wyjdz", bg="white", width=17, height=1, command=lambda: self.mainMenu(screen))
        button.place(x=160, y=170)

        T = tk.Text(legenda, height=24, width=36)
        T.insert(tk.END, swiat.getKomentarze())
        T.place(y=205, x=3)
        swiat.setKomentarze("")

    def odtworzSwiat(self, nazwa_pliku, screen):
        for widgets in screen.winfo_children():
            widgets.destroy()
        swiat = Swiat(self.rozmiar_X, self.rozmiar_Y)
        swiat.wczytajSwiat(nazwa_pliku)
        self.drawMapa(screen, swiat)

    def open_game(self, screen):
        input = Tk()
        e = tk.Entry(input)
        e.pack()

        def callback(screen):
            nazwa_pliku = e.get()
            self.odtworzSwiat(nazwa_pliku, screen)
            input.destroy()

        b = tk.Button(input, text="Confirm", command=lambda: callback(screen))
        b.pack()

    def save(self, swiat):
        input = Tk()
        e = tk.Entry(input)
        e.pack()

        def callback():
            nazwa_pliku = e.get()
            swiat.saveSwiat(nazwa_pliku)
            input.destroy()

        b = tk.Button(input, text="Confirm", command=callback)
        b.pack()

    def drawMapa(self, screen, swiat):
        plansza = tk.Canvas(screen, width=600, height=600)
        plansza.place(x=0, y=0)
        legenda = tk.Canvas(screen, width=300, height=600)
        legenda.place(x=600, y=0)
        screen.configure(bg="white")
        self.drawOrganizmy(screen, swiat, plansza)
        self.drawLegenda(screen, swiat, legenda)


        running = True

        def left():
            if swiat.getCzyCzlowiekZyje():
                swiat.getCzlowiek().setKierunekRuchu(self.__LEWO)
            swiat.wykonajTure()
            self.drawOrganizmy(screen, swiat, plansza)
            self.drawLegenda(screen, swiat, legenda)

        def right():
            if swiat.getCzyCzlowiekZyje():
                swiat.getCzlowiek().setKierunekRuchu(self.__PRAWO)
            swiat.wykonajTure()
            self.drawOrganizmy(screen, swiat, plansza)
            self.drawLegenda(screen, swiat, legenda)

        def up():
            if swiat.getCzyCzlowiekZyje():
                swiat.getCzlowiek().setKierunekRuchu(self.__GORA)
            swiat.wykonajTure()
            self.drawOrganizmy(screen, swiat, plansza)
            self.drawLegenda(screen, swiat, legenda)

        def down():
            if swiat.getCzyCzlowiekZyje():
                swiat.getCzlowiek().setKierunekRuchu(self.__DOL)
            swiat.wykonajTure()
            self.drawOrganizmy(screen, swiat, plansza)
            self.drawLegenda(screen, swiat, legenda)

        def moc():
            swiat.getCzlowiek().setCzyChceUzycSupermocy(True)
            swiat.wykonajTure()
            self.drawOrganizmy(screen, swiat, plansza)
            self.drawLegenda(screen, swiat, legenda)

        def next():
            swiat.wykonajTure()
            self.drawOrganizmy(screen, swiat, plansza)
            self.drawLegenda(screen, swiat, legenda)

        while running:
            screen.bind("<Right>", lambda ev: right())
            screen.bind("<Up>", lambda ev: up())
            screen.bind("<Down>", lambda ev: down())
            screen.bind("<Left>", lambda ev: left())
            screen.bind("<n>", lambda ev: moc())
            screen.bind("<Return>", lambda ev: next())
            screen.mainloop()



    def rysujPlansze(self, screen):
        def clear_frame():
            for widgets in screen.winfo_children():
                widgets.destroy()

            swiat = Swiat(self.rozmiar_X, self.rozmiar_Y)
            self.drawMapa(screen, swiat)

        clear_frame()




