

# Abstract Class - Method

# encapsulation
# inheritence
# polimorfizm
# abstraction - soyutlama


# nesne üretilemeyen sınıflar 
# -> genel bir şablon için gerekli 
# nesne üretmiceksiniz ama nesne üreteceğiniz sınıfların ortak özelliklerini birleştirmek için 


# evimizde farklı internete bağlanan akıllı cihazlar var. bunlara mobilden çalıştırma bildirim gönderiyoruz.
# herbir cihazın çalışma metodu farklı olucak. 


# geleneksel yöntem ile abstract class oluşturma
"""
class AkilliCihaz:
    def __init__(self,cihaz_adi):
        self.cihaz_adi = cihaz_adi

    def calistir(self):
        pass
    
    def durum_bilgisi(self):
        pass
    

class Klima(AkilliCihaz):
    def __init__(self,cihaz_adi):
        super().__init__(cihaz_adi)
        
    def calistir(self):
        print(self.cihaz_adi,"klima 22 dereceye ayarlanıyor.")
        
    def durum_bilgisi(self):
        print(self.cihaz_adi,"iyi bir şekilde soğutuyor.")

class Lamba(AkilliCihaz):
    def __init__(self,cihaz_adi):
        super().__init__(cihaz_adi)
        
    def calistir(self):
        print(self.cihaz_adi,"Işıklar %50 parlaklık arttırıldı.")
    
    def durum_bilgisi(self):
        print(self.cihaz_adi,"güzel bir şekilde aydınlatıyor.")



evKlimasi = Klima("Beko KLM10T")
evKlimasi.calistir()
evKlimasi.durum_bilgisi()
print("============================================")
evLambasi = Lamba("philips LMB3A+")
evLambasi.calistir()
evLambasi.durum_bilgisi()
"""

# kütüphane kullanarak abstract class kullanımı
from abc import ABC,abstractmethod

class AkilliCihaz(ABC):
    def __init__(self,cihaz_adi):
        self.cihaz_adi = cihaz_adi

    @abstractmethod
    def calistir(self):
        #her cihaz kendi calistir metodunu kullanması için
        pass
    
    def durum_bilgisi(self):
        return "cihaz adi : " + self.cihaz_adi
    

class Klima(AkilliCihaz):
    def __init__(self,cihaz_adi):
        super().__init__(cihaz_adi)
        
    def calistir(self):
        print(self.cihaz_adi,"klima 22 dereceye ayarlanıyor.")
        
    def durum_bilgisi(self):
        print(self.cihaz_adi,"iyi bir şekilde soğutuyor.")

class Lamba(AkilliCihaz):
    def __init__(self,cihaz_adi):
        super().__init__(cihaz_adi)
        
    def calistir(self):
        print(self.cihaz_adi,"Işıklar %50 parlaklık arttırıldı.")
    
    def durum_bilgisi(self):
        print(self.cihaz_adi,"güzel bir şekilde aydınlatıyor.")



evKlimasi = Klima("Beko KLM10T")
evKlimasi.calistir()
evKlimasi.durum_bilgisi()
print("============================================")
evLambasi = Lamba("philips LMB3A+")
evLambasi.calistir()
evLambasi.durum_bilgisi()



# pdf -> word   , word -> pdf  , png -> jpg,jpeg,svg , pptx -> pdf

class DosyaIslemi(ABC):
    
    def __init__(self,dosya_turu):
        self.dosya_turu = dosya_turu
    
    @abstractmethod
    def dosyayi_oku(self,dosya_yolu):
        pass
    
    @abstractmethod
    def dosya_turunu_yaz(self):
        pass
    
class PdfIsleyici(DosyaIslemi):
    def __init__(self,dosya_yolu,dosya_turu):
        super().__init__(dosya_turu)
        self.dosya_yolu = dosya_yolu
        
    def dosyayi_oku(self):
        print(self.dosya_yolu,"hedefinden pdf dosyası okundu! okunan dosyanın turu:",self.dosya_turu)
    
    def dosya_turunu_yaz(self):
        print("dosya turu :",self.dosya_turu)

class ExcelIsleyici(DosyaIslemi):
    def __init__(self,dosya_yolu,dosya_turu):
        super().__init__(dosya_turu)
        self.dosya_yolu = dosya_yolu

    def dosyayi_oku(self):
        print(self.dosya_yolu,"hedefinden excel dosyası okundu! veritabanına aktarıldı. okunan dosyanın turu:",self.dosya_turu)

    def dosya_turunu_yaz(self):
        print("dosya turu :",self.dosya_turu)

dosya1 = PdfIsleyici("/Masaüstü/belgelerim","PDF")
dosya1.dosyayi_oku()
dosya1.dosya_turunu_yaz()


print(dosya1.__str__())
