

# Hastane Otomasyonu

# randevu
# hasta
# doktor
# polikinlik
# bölüm
# tahlil
# hastanePersoneli
# ilaç

"""
RANDEVU SİSTEMİ

class Insan
isim
soyisim
cinsiyet
yaş

class Doktor : Insan
alan
ünvan
musaitlik -> {"pazartesi":[9,10,11,12,14,15,16,17]}

class Hasta : Insan
randevu_listesi
alerjiler
tc_no
boy
kilo

"""

# https://codeshare.io/aVnxq9

class Insan:
    def __init__(self,
    isim,
    soyisim,
    cinsiyet,
    yas    ):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__cinsiyet = cinsiyet
        self.__yas = yas
    
    def bilgileri_goster(self):
        print("isim: ", self.__isim)
        print("soyisim: ", self.__soyisim)
        print("cinsiyet: ", self.__cinsiyet)
        print("yas: ", self.__yas)
        
insan1 = Insan("osman","can","erkek",10)

class Doktor(Insan):
    def __init__(self, isim,soyisim, cinsiyet, yas,alan,unvan,musaitlik):
        super().__init__(isim,soyisim,cinsiyet,yas)
        self.__alan = alan
        self.__unvan = unvan
        self.__musaitlik = musaitlik

class Hasta(Insan):
    def __init__(self, isim,soyisim,cinsiyet, yas,randevu_listesi,alerjiler,tc_no):
        super().__init__(isim,soyisim,cinsiyet,yas)
        self.__randevu_listesi = randevu_listesi
        self.__alerjiler = alerjiler
        self.__tc_no = tc_no

    


