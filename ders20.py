


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

kahraman1 = Kahraman(100,100,{"torch":1},20,"ork","oduncu",170,150,"armadillo",{"x":0,"y":0},100,0)

print(kahraman1.get_level())

kahraman1.set_level(-5)

# https://codeshare.io/5gvbWN