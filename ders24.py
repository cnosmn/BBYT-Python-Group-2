
# POLİMORFİZM OLMADIGINDA YAPILAN ÇÖZÜM 
# yeni bir ödeme yöntemi geldiğinde yeni bir sınıf oluşturulmalı 
# ayrıca ana programda değişiklik yapılmalı
# bu kötü kod yazım örneğidir 

# class KrediKarti:
#     def kartla_ode(self,miktar):
#         print("kredi kartı ile şu miktar : ",miktar,"ödendi.")

# class Nakit:
#     def nakit_ode(self,miktar):
#         print("nakit ödeme ile şu miktar : ",miktar,"ödendi.")

# class Kripto:
#     def kripto_ode(self,miktar):
#         print("kripto ödeme ile şu miktar : ",miktar,"ödendi.")

# class YemekKarti:
#     def yemek_karti_ode(self,miktar):
#         print("yemek_kartı ödeme ile şu miktar : ",miktar,"ödendi.")


# # isistance(nesne,sınıf_ismi)
# # isistance bize nesnenin o sınıftan üretilip üretilmediğini kontrol eder.
# # eğer üretildiyse True üretilmediyse False değer döndürür.

# # ana program
# def islemi_gerceklestir(odeme_nesnesi,miktar):
#     if isinstance(odeme_nesnesi,KrediKarti): 
#         odeme_nesnesi.kartla_ode(miktar)
#     elif isinstance(odeme_nesnesi,Nakit):
#         odeme_nesnesi.nakit_ode(miktar)
#     elif isinstance(odeme_nesnesi,Kripto):
#         odeme_nesnesi.kripto_ode(miktar)
#     elif isinstance(odeme_nesnesi,YemekKarti):
#         odeme_nesnesi.yemek_karti_ode(miktar)
#     else :
#         print("verdiğiniz nesne hiçbir sınıfa ait değil")
#         print("Odeme Başarısız!")

# kredi = KrediKarti()
# nakit = Nakit()
# kripto = Kripto()
# yemek = YemekKarti()

# islemi_gerceklestir(kredi,"100")
# islemi_gerceklestir(nakit,"150")
# islemi_gerceklestir(kripto,"200")
# islemi_gerceklestir(yemek,"300")



"""
isistance kullanımı : 

class Insan 

class Ogrenci(Insan) 

ogrenci1 = Ogrenci()
ogrenci1 adında Ogrenci sınıfından nesne oluşturduğumda 

isinstance(ogrenci1,Ogrenci) ? True
isistance(ogrenci1,Insan) ? True
"""


#Polimorfizm

class OdemeYontemi:
    def odeme_yap(self,miktar):
        pass

class Kredi(OdemeYontemi):
    def odeme_yap(self,miktar):
        print("kredi kartı ile şu miktar : ",miktar,"ödendi.")

class Cripto(OdemeYontemi):
    def odeme_yap(self,miktar):
        print("kripto ile şu miktar : ",miktar,"ödendi.")

class Nakit(OdemeYontemi):
    def odeme_yap(self,miktar):
        print("nakit ile şu miktar : ",miktar,"ödendi.")

class Yemek(OdemeYontemi):
    def odeme_yap(self,miktar):
        print("yemek ile şu miktar : ",miktar,"ödendi.")
        
class YeniOdeme(OdemeYontemi):
    def odeme_yap(self, miktar):
        print("yeni ödeme ile şu miktar : ",miktar,"ödendi.")

# ana program
def ana_program(nesne,miktar):
    nesne.odeme_yap(miktar)

kredi = Kredi()
nakit = Nakit()
kripto = Cripto()
yemek = Yemek()
yeni_odeme = YeniOdeme()

ana_program(kredi,"100")
ana_program(nakit,"150")
ana_program(kripto,"200")
ana_program(yemek,"300")
ana_program(yeni_odeme,"270")