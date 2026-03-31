# polimorfizm -> çok biçimlilik
# metotların farklı şekillerde davranmasıdır.
# aynı isimdeki metotların farklı sınıflarda farklı şekillerde davranmasıdır.

# 1. örnek bildirim sistemi
# 2. RPG oyun karakter yetenekleri
# 3. ödeme sistemi

# 1. örnek  - bildirim sistemi

# bildirim : bilgilendirme metni

class Bildirim:
    """ ana class """
    def __init__(self,gonderen,baslik,icerik):
        self.__gonderen = gonderen
        self.__baslik = baslik
        self.__icerik = icerik

    @property
    def gonderen(self):
        return self.__gonderen
    
    @property
    def baslik(self):
        return self.__baslik
    
    @property
    def icerik(self):
        return self.__icerik
     
    def gonder(self):
        print("Gönderen : ",self.__gonderen + "\n" + self.__baslik +"\n" + self.__icerik)
        
class EpostaBildirim(Bildirim):
    def __init__(self,gonderen,baslik,icerik,alici_maili):
        super().__init__(gonderen,baslik,icerik)
        self.__alici_maili = alici_maili
        
    # polimorfizm - override
    def gonder(self):
        # super().gonder() 
        # print("ALICI MAİL : ",self.__alici_maili)
        print("Gönderen : ",super().gonderen + "\n" + "Alıcı :",self.__alici_maili +"\n" + super().baslik +"\n" + super().icerik)
        # üst sınıfta private olarak tanımlanan özellikler alt sınıfta direk erişilemez,
        # üst sınıftan get metodunun yazılması lazım alt sınıfta özelliğe erişmek için
        
class SmsBildirimi(Bildirim):
    def __init__(self,gonderen,baslik,icerik,alici_numara):
        super().__init__(gonderen,baslik,icerik)
        self.__alici_numara = alici_numara
        
    # polimorfizm - override
    def gonder(self):
        print("Gönderen : ",self.__gonderen + "\n" + "Alıcı :",self.__alici_numara +"\n" + self.__baslik +"\n" + self.__icerik)

class PushBildirimi(Bildirim):
    def __init__(self,gonderen,baslik,icerik,alici_uygulama):
        super().__init__(gonderen,baslik,icerik)
        self.__alici_uygulama = alici_uygulama
        
    # polimorfizm - override
    def gonder(self):
        print("Gönderen : ",self.__gonderen + "\n" + "Alıcı :",self.__alici_uygulama +"\n" + self.__baslik +"\n" + self.__icerik)
       
        

bildirim = Bildirim("Osman can","ders hatırlatması","saat 20:00'da BBYT dersi başlayacak!")
eposta_bildirim = EpostaBildirim("Osman can","ders hatırlatması","saat 20:00'da BBYT dersi başlayacak!","acikatolye@gmail.com")
sms_bildirim = SmsBildirimi("Osman can","ders hatırlatması","saat 20:00'da BBYT dersi başlayacak!","+905125122412")
push_bildirim = PushBildirimi("Osman can","ders hatırlatması","saat 20:00'da BBYT dersi başlayacak!","Whatsapp")
bildirim.gonder()
print("================================")
eposta_bildirim.gonder()
# print("================================")
# sms_bildirim.gonder()
# print("================================")
# push_bildirim.gonder()
# print("================================")




