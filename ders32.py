import json
import os
from abc import ABC,abstractmethod


# temel bir hastane otomasyon projesi olucak
# sınıflar : kisi ,hasta ,doktor

class Kisi(ABC):
    def __init__(self,id,ad,soyad):
        self.id = id
        self.ad = ad
        self.soyad = soyad
    
    @abstractmethod
    def bilgi_yazdir(self):
        pass
    
    def to_dictionary(self):
        return {
            "id":self.id,
            "ad":self.ad,
            "soyad":self.soyad,
            "rol":self.__class__.__name__
            }
        
# alt sınıflar
class Hasta(Kisi):
    def __init__(self,id,ad,soyad,sikayet):
        super().__init__(id,ad,soyad)
        self.sikayet = sikayet
    
    def bilgi_yazdir(self):
        return "hasta id: "+str(self.id)+" ad: "+self.ad+" soyad: "+self.soyad+" Şikayet: "+self.sikayet
    
    def to_dictionary(self):
        sozluk_veri = super().to_dictionary()
        sozluk_veri["sikayet"] = self.sikayet
        return sozluk_veri
    
class Doktor(Kisi):
    def __init__(self,id,ad,soyad,uzmanlik):
        super().__init__(id,ad,soyad)
        self.uzmanlik = uzmanlik
    
    def bilgi_yazdir(self):
        return "doktor id: "+str(self.id)+" ad: "+self.ad+" soyad: "+self.soyad+" uzmanlık: "+self.uzmanlik
    
    def to_dictionary(self):
        sozluk_veri = super().to_dictionary()
        sozluk_veri["uzmanlik"] = self.uzmanlik
        return sozluk_veri


# sistem yönetimi

class HastaneYonetimi:
    def __init__(self,dosya_yolu="hastane.json"):
        self.dosya_yolu = dosya_yolu
        self.kayitlar = self.kayitlari_yukle()
        
    
    def kayitlari_yukle(self):
        if os.path.exists(self.dosya_yolu):
            with open(self.dosya_yolu,"r",encoding="utf-8") as dosya:
                veri_listesi = json.load(dosya)
                nesneler = []
                for veri in veri_listesi:
                    if veri["rol"] == "Hasta":
                        nesneler.append(Hasta(veri["id"],veri["ad"],veri["soyad"],veri["sikayet"]))
                    else:
                        nesneler.append(Doktor(veri["id"],veri["ad"],veri["soyad"],veri["uzmanlik"]))
                return nesneler
        else:
            return {}
        
    def kaydet(self):
        liste = []
        for i in self.kayitlar:
            liste.append(i.to_dictionary())
        
        #verileri kaydet
        with open(self.dosya_yolu,"w",encoding="utf-8") as dosya:
            json.dump(liste,dosya,indent=4,ensure_ascii=False)
    
    def ekle(self,kisi):
        self.kayitlar.append(kisi)
        self.kaydet()
        print("başarılı bir şekilde kayıt eklendi. kayıt bilgiler: ",kisi.ad)
    
    def sil(self,id):
        
        veriler = []
        for k in self.kayitlar:
            if k.id != id:
                veriler.append(k)
        self.kayitlar = veriler.copy()
        
        #self.kayitlar = [k for k in self.kayitlar if k.id != id]
        self.kaydet()
    
    def listele(self):
        for k in self.kayitlar:
            print(k.bilgi_yazdir())
            print("-------------------------------------------")
            
            
# kullanım

if __name__ == "__main__":
    sistem = HastaneYonetimi()
    
    if not sistem.kayitlar:
        sistem.ekle(Doktor(1,"can","yılmaz","beyin cerrahı"))
        sistem.ekle(Hasta(1,"osman","can","Baş ağrısı"))
    sistem.listele()