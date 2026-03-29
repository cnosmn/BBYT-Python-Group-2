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

# https://codeshare.io/29N4BB