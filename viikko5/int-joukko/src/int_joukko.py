KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = KAPASITEETTI if kapasiteetti is None else kapasiteetti
        self.kasvatuskoko = OLETUSKASVATUS if kasvatuskoko is None else kasvatuskoko

        self.__tarkasta_arvot()

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def __tarkasta_arvot(self):
        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla luonnollinen luku")
        
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            raise Exception("kasvatuskoon tulee olla luonnollinen luku")

    def kuuluu(self, luku):
        return luku in self.lukujono
    
    def taysi(self):
        return self.alkioiden_lkm == len(self.lukujono)

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

        if self.taysi():
            taulukko_old = self.lukujono
            self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.lukujono)

    def poista(self, poistettava):
        if poistettava in self.lukujono:
            kohta = self.lukujono.index(poistettava)
            self.lukujono[kohta] = 0

            for j in range(kohta, self.alkioiden_lkm - 1):
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = 0

            self.alkioiden_lkm -= 1

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            tulos.lisaa(b_taulu[i])

        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if a_taulu[i] in b_taulu:
                tulos.lisaa(a_taulu[i])
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if a_taulu[i] not in b_taulu:
                tulos.lisaa(a_taulu[i])
        return tulos

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            return f"{{{(", ".join(map(str, self.to_int_list())))}}}"

