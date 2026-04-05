# oop özel kelimeler
"""
init - yapıcı fonksiyon
encapsulation - 
polimorfizm - override
inhertitance - Kalıtım
abstraction - nesne üretilemiyor (şablon) -kalıtım alınabilir
super()  -> 
class
self
get-set metotları
public()-private(__)-protected(_)
@property
@özellik_ismi.setter
    
"""


class Ogrenci:
    
    def __init__(self,ad):
        self.ad = ad
        
    def odev_yap(self):
        print("ödev yapılıyor!")
        self.ad
        self.bilgi_goster()
    
    def bilgi_goster(self):
        return "osman"
    
    def okula_git():
        print("okula gidiliyor!")
        
    def ortalama_hesapla(konusma,yazili,dinleme):
        ortalama = (konusma * 0.25) + (yazili * 0.5) + (dinleme * 0.25)
        return ortalama
    
    def gecti_mi(ortalama):
        if ortalama > 50:
            print("gecti")
        else : 
            print("kaldı") 

# self ibaresi olan metotlar sadece nesneler kullanabilir
# self olmayanlar için direk class ismi ile kullanılabilir.

#Ogrenci.odev_yap()

ogrenci1 = Ogrenci()
ogrenci1.odev_yap()

sonuc = Ogrenci.ortalama_hesapla(70,67,80)
print("sonuc : ",sonuc)
Ogrenci.gecti_mi(sonuc)


# abstract class
