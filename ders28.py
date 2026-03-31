"""
Karakter (ana class )
-isim       public string
-can        public int
-aclik      public float
-stamina    public int

yetenek_kullan() -> yetenek kullanıldı.

Savasci( Kahraman )
-silah     public string

yetenek_kullan() -> savaşçı karakterine göre bir şeyler yazsın


Buyucu( Kahraman )
-mana     public float

yetenek_kullan() -> Buyucu karakterine göre bir şeyler yazsın


Sifaci( Kahraman )
-iyilestirme_katsayisi public float

yetenek_kullan() -> Sifaci karakterine göre bir şeyler yazsın
"""



class Karakter:
    def __init__(self,isim,can,aclik,stamina):
        self.isim = isim
        self.can = can
        self.aclik = aclik
        self.stamina = stamina
    
    def yetenek_kullan(self):
        raise NotImplementedError("Her Kahraman kendi Yeteneğini tanımlamalı!")
    
class Savasci(Karakter):
    def __init__(self,isim,can,aclik,stamina,silah):
        super().__init__(isim,can,aclik,stamina)
        self.silah = silah
    
    def yetenek_kullan(self):
        print(self.isim,self.silah,"ile saldırısını yaptı.")

class Buyucu(Karakter):
    def __init__(self,isim,can,aclik,stamina,mana):
        super().__init__(isim,can,aclik,stamina)
        self.mana = mana
    
    def yetenek_kullan(self):
        self.mana -= 20
        print(self.isim,"alev topu saldırısını yaptı. Kalan mana : ",self.mana)

class Sifaci(Karakter):
    def __init__(self,isim,can,aclik,stamina,iyilestirme_katsayisi):
        super().__init__(isim,can,aclik,stamina)
        self.iyilestirme_katsayisi = iyilestirme_katsayisi
    
    def yetenek_kullan(self,can):
        can = can + (can*self.iyilestirme_katsayisi)
        print(self.isim,"İyileştirme özelliğini kullandı. İyileşme Oranı : ","%" + str(self.iyilestirme_katsayisi*100),"can durumu : ",can)

savasci = Savasci("aragorn",120,100.0,100,"Çift Elli Balta")
savasci.yetenek_kullan()

buyucu = Buyucu("Dumbledore",80,70,200,170.0)
buyucu.yetenek_kullan()

sifaci = Sifaci("harvey",180,50,30.0,0.4)
sifaci.yetenek_kullan(50)

