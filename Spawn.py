from Antylopa import Antylopa
from BarszczSosnowskiego import BarszczSosnowskiego
from CyberOwca import CyberOwca
from Czlowiek import Czlowiek
from Guarana import Guarana
from Mlecz import Mlecz
from Organizm import Organizm
from Trawa import Trawa
from WilczeJagody import WilczeJagody
from Wilk import Wilk
from Owca import Owca
from Lis import Lis
from Zolw import Zolw


class Spawn:
    def stworzOrganizm(self, typ, swiat, pozycja):
        if typ is Organizm.Gatunek.WILK:
            return Wilk(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.OWCA:
            return Owca(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.LIS:
            return Lis(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.ZOLW:
            return Zolw(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.ANTYLOPA:
            return Antylopa(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.TRAWA:
            return Trawa(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.MLECZ:
            return Mlecz(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.GUARANA:
            return Guarana(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.WILCZE_JAGODY:
            return WilczeJagody(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.BARSZCZ_SOSNOWSKIEGO:
            return BarszczSosnowskiego(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.CZLOWIEK:
            return Czlowiek(swiat, pozycja, swiat.getNumerTury())
        elif typ is Organizm.Gatunek.CYBER_OWCA:
            return CyberOwca(swiat, pozycja, swiat.getNumerTury())
