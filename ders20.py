


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
        self.ileri()
        self.ileri()
        if self.durability < 100:
            self.durability -= 50 # self.ileri metodu durability arttırdıgından dolayı
            if self.durability < 0:
                self.durability = 0
"""
-yemek_ye()
açıklama : karakter yemek yediğinde açlık seviyesi artar ve hp si artar
-kullan()
açıklama : karakter bir eşya kullandığında envanterinden o eşya azalır ve karakterin hp si artar

metotları ödev olarak veriyorum
"""



kahraman1 = Kahraman(100,100,{"torch":1},20,"ork","oduncu",170,150,"armadillo",{"x":0,"y":0},100,0)

print(kahraman1.get_level())
kahraman1.set_level(-5)

kahraman1.level = -5
print(kahraman1.level)

# https://codeshare.io/5gvbWN