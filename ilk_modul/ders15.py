
# f(x) = x^3 - 6x^2 + 11x - 6
# f() = 5



# Fonksiyonlar 
# Tanımı :  
# Türleri :
# 1- Parametresiz - Dönüşsüz

def fonksiyon_ismi():
    print("Merhaba Dünya!")

def toplama():
    a = 5
    b = 10
    print("Toplam:", a + b)

fonksiyon_ismi()
fonksiyon_ismi()
fonksiyon_ismi()

toplama()

# 2- Parametreli - Dönüşsüz

def yazdir(metin):
    print(metin)

yazdir("Python Programlama")
yazdir([1, 2, 3, 4, 5])

def parametreli_toplama(a, b):
    print("Toplam:", a + b)

parametreli_toplama(a=7, b=12)
parametreli_toplama(3, 4)


# 3- Parametresiz - Dönüşlü

def sayi_dondur():
    dondur = "Merhaba"
    return dondur

# 1.yöntem
sonuc = sayi_dondur()
print(sonuc)
#2.yöntem
print(sayi_dondur())

def mutlak_deger():
    a = 10 
    b = -15
    if a-b < 0:
        return -1 * (a-b)
    else:
        return a-b

mutlak_sonuc = mutlak_deger()
print("Parametresiz Mutlak Değer Sonucu :", mutlak_sonuc)

# 4- Parametreli - Dönüşlü

def mutlak_parametreli(sayi):
    if sayi < 0:
        return -1 * sayi
    else:
        return sayi

kullanici_sayisi = int(input("Bir sayı giriniz: "))
parametreli_sonuc = mutlak_parametreli(kullanici_sayisi)

print("Girilen Sayının Mutlak Değeri :", parametreli_sonuc)

# faktoriyel hesaplama
# 5! -> 5*4*3*2*1 -> 120

def faktoriyel_hesapla(n):
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i # sonuc = sonuc * i

    return sonuc
    
kullanici_faktoriyel = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı giriniz: "))

faktoriyel_sonuc = faktoriyel_hesapla(kullanici_faktoriyel)
print("Girdiğiniz sayının faktoriyeli :", faktoriyel_sonuc)



# ucgenin alanını hesaplayan fonksiyon

def ucgen_alan(taban, yukseklik):
    alan = (taban * yukseklik) / 2
    return alan

taban = int(input("Taban uzunluğunu giriniz: "))
yukseklik = int(input("Yüksekliği giriniz: "))

ucgen_alan_sonuc = ucgen_alan(taban, yukseklik)

print("Girilen üçgenin alanı:", ucgen_alan_sonuc)



















