

class Insan:
    #constructor -> yapıcı fonksiyon
    def __init__(self,isim,soyisim,cinsiyet,tc):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__cinsiyet = cinsiyet
        self.__tc = tc
    
    def bilgileri_goster(self):
        print("isim : ",self.__isim)
        print("soyisim : ",self.__soyisim)
        print("cinsiyet : ",self.__cinsiyet)
        print("tc : ",self.__tc)

class Ogrenci(Insan):
    def __init__(self,isim,soyisim,cinsiyet,tc,ogrenciNo,sinif):
        super().__init__(isim,soyisim,cinsiyet,tc)
        self.__ogrenciNo = ogrenciNo
        self.__sinif = sinif

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("ogrenciNo : ",self.__ogrenciNo)
        print("sınıf : ",self.__sinif)
    
class Ogretmen(Insan):
    def __init__(self,isim,soyisim,cinsiyet,tc,brans,deneyim):
        super().__init__(isim,soyisim,cinsiyet,tc)
        self.__brans = brans
        self.__deneyim = deneyim

    def bilgileri_goster(self):
        super().bilgileri_goster()
        print("branş : ",self.__brans)
        print("deneyim : ",self.__deneyim)

ogrenci = Ogrenci("alim","yenilmezcan","erkek","122234234","332","9-E")
ogretmen = Ogretmen("osman","can","erkek","1489","BM","3")
insan = Insan("emir","sipahi","erkek","2346686")

insan.bilgileri_goster()
print("============================")
ogrenci.bilgileri_goster()
print("============================")
ogretmen.bilgileri_goster()