# encapsulation - kapsülleme
# inheritence - kalıtım
# polimorfizm - çok biçimlilik
# abstraction - soyutlama


# ucmak()
# yüzme()
# saldırmak()

# uzuv


class Hayvan:
    def __init__(self,beslenme_turu,cinsiyet,agirlik):
        self.beslenme_turu = beslenme_turu
        self.cinsiyet = cinsiyet
        self.agirlik = agirlik

    def ses_cikar(self):
        print("ses çıkarıldı")

class Kus(Hayvan):
    def __init__(self,beslenme_turu,cinsiyet,agirlik):
        super().__init__(beslenme_turu,cinsiyet,agirlik)

    # override
    def ses_cikar(self):
        print("ötme sesi çıkarıldı")

class Aslan(Hayvan):
    def __init__(self,beslenme_turu,cinsiyet,agirlik):
        super().__init__(beslenme_turu,cinsiyet,agirlik)

    def ses_cikar(self):
        print("kükreme sesi")

class Balik(Hayvan):
    def __init__(self,beslenme_turu,cinsiyet,agirlik):
        super().__init__(beslenme_turu,cinsiyet,agirlik)

    def ses_cikar(self):
        print("sonar sesi çıkarıldı")

kus1 = Kus("hepçil","dişi","1.5")
aslan1 = Aslan("etçil","erkek","200")
balik1 = Balik("hepçil","hermafrodit","0.5")

kus1.ses_cikar()
# aslan1.ses_cikar()
# balik1.ses_cikar()

# https://codeshare.io/29N4BB
