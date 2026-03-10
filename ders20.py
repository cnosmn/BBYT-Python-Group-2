


# Nesneye Yönelimli Programlama

# sınıf -> class
# attribute -> özellik
# method -> fonksiyon
# nesne -> object
# __init__ -> constructor

# sınıf ismi büyük harfle başlar
class Tshirt:

    fiyat = 15
    def goster():
        print("T-shirt gösteriliyor")
        print("T-shirt fiyatı: ", Tshirt.fiyat)

Tshirt.goster()



"""
karakter:
-hp -> int
-durability -> int
-envanter {} -> dict
-hız -> int
-tur (elf,goblin,insan,buyucu,ork) -> string
-meslek -> string
-boy(cm) -> int
-kilo(kg) -> float
-pet -> string
-konum {"x":100,"y":20} -> dict 
-hungary int
-level -> int

metotlar
-bilgileri_goster()
-ileri()
-geri()
-sag()
-sol()
-saldir()
-kosma()
-yemek_ye()
-kullan()

"""

class Kahraman:
    def __init__(self,
        hp,
        durability,
        envanter,
        hiz,
        tur,
        meslek,
        boy,
        kilo,
        pet,
        konum,
        aclik,
        level = 0
        ):
        self.__hp = hp
        self.hiz = hiz
        self.durability = durability
        self.envanter = envanter
        self.tur = tur
        self.meslek = meslek
        self.boy = boy
        self.kilo = kilo
        self.pet = pet
        self.konum = konum
        self.aclik = aclik
        self.__level = level

# encapsulation  -> babaanne tansiyon hapı   (fonksiyon veriyi sarmallıyo)
# private veriyie direk erişim yok fonksiyon ile erişim var daha kontrollü ve güvenli

# get ve set metotları ile

    def get_level(self):
        return self.__level

    def set_level(self,yeni_level):
        if yeni_level < 0 : 
            print("level negatif değer olamaz ")
            return
        self.__level = yeni_level
        return "başarılı"
    
    # python da get ve set metotları yerine property dekoratörleri kullanılır
    # pytonic way -> python tarzı
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self,yeni_level):
        if yeni_level < 0 : 
            print("level negatif değer olamaz ")
            return
        self.__level = yeni_level
        return "başarılı"
    

    def bilgileri_goster(self):
        print("hp: ", self.__hp)
        print("durability: ", self.durability)
        print("envanter: ", self.envanter)
        print("hız: ", self.hiz)
        print("tur: ", self.tur)
        print("meslek: ", self.meslek)
        print("level: ", self.level)

    def ileri(self):
        print("ileri gidiliyor")
        if self.durability < 100:
            self.durability += 10
            if self.durability > 100:
                self.durability = 100

        self.konum["y"] += self.hiz

    def geri(self):
        print("geri gidiliyor")
        if self.durability < 100:
            self.durability += 10
            if self.durability > 100:
                self.durability = 100
        self.konum["y"] -= self.hiz

    def sag(self):
        print("sağa gidiliyor")
        if self.durability < 100:
            self.durability += 10
            if self.durability > 100:
                self.durability = 100
        self.konum["x"] += self.hiz
    
    def sol(self):
        print("sola gidiliyor")
        if self.durability < 100:
            self.durability += 10
            if self.durability > 100:
                self.durability = 100
        self.konum["x"] -= self.hiz

    def saldir(self):
        print("saldırılıyor")
        if self.durability <= 0:
            print("Bu karakter saldıramaz, karakter çok incinmiş.")
            return
        if self.durability < 100:
            self.durability -= 10
            if self.durability < 0:
                self.durability = 0

    def kosma(self):
        print("koşuluyor")
        if self.durability <= 0:
            print("Bu karakter koşamaz, karakter çok incinmiş.")
            return
        self.konum["y"] += self.hiz * 2
        if self.durability <= 100:
            self.durability -= 50 # self.ileri metodu durability arttırdıgından dolayı
            if self.durability < 0:
                self.durability = 0
    
    def yemek_ye(self):
        if self.aclik < 0:
            print("aclik negatif degerde hata")
            return
        if self.aclik < 100:
            self.durability += 20
            self.aclik += 20
            if self.aclik > 100:
                self.aclik = 100
            print("yemek yenildi, açlık ve durability arttı")
            print("aclik: ", self.aclik)
            print("durability: ", self.durability)

    def kullan(self,kullanilacak_esya):
        print(f"{kullanilacak_esya} kullanılıyor")
        esya_var_mi = self.envanter.get(kullanilacak_esya,"esya yok")
        if esya_var_mi == "esya yok":
            print("aradıgın esya envanterde yok")
            return
        if esya_var_mi > 0 :
            self.envanter[kullanilacak_esya] -= 1
            print(f"{kullanilacak_esya} kullanıldı")
        else:
            print("kullanılacak esya envanterde bitmiş")
            return
        
    def envantere_ekle(self,esya_adi,esya_adedi):
        esya_var_mi = self.envanter.get(esya_adi,"esya yok")
        if esya_adedi < 1 :
            print("esya adedi 1'den küçük olamaz")
            return
        if esya_var_mi == "esya yok":
            self.envanter[esya_adi] = esya_adedi
            print("envantere",esya_adi,"eklendi",esya_adedi,"tane eklendi")
        else :
            self.envanter[esya_adi] += esya_adedi
            print("envantere",esya_adi,"içerisine",esya_adedi,"tane eklendi")

kahraman1 = Kahraman(100,100,{"torch":1,"bread":0,"water":5,"key":5,"potion":16},20,"ork","oduncu",170,150,"armadillo",{"x":0,"y":0},100,0)
kahraman2 = Kahraman(100,100,{"torch":1,"bread":10,"water":10,"key":11,"potion":5},20,"elf","okçu",170,150,"tilki",{"x":0,"y":0},100,0)
kahraman3 = Kahraman(100,100,{"torch":1,"bread":1,"water":3,"key":17,"potion":1},20,"insan","savaşçı",170,150,"tavşan",{"x":0,"y":0},100,0)

kahraman1.bilgileri_goster()
kahraman1.ileri()
kahraman1.sag()
kahraman1.kosma()
print("kahraman1.durability:", kahraman1.durability)
print("kahraman1.envanter:", kahraman1.envanter)
print("kahraman1.konum:", kahraman1.konum)
print("kahraman1.aclik:", kahraman1.aclik)
kahraman1.aclik = 70
print("kahraman1.aclik:", kahraman1.aclik)
kahraman1.yemek_ye()
kahraman1.kullan("bread")
print("kahraman1.envanter : ",kahraman1.envanter)
kahraman1.envantere_ekle("bread",4)
print("kahraman1.envanter : ",kahraman1.envanter)
