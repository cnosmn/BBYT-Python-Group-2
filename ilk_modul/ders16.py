# f(x) = ax + b
# y = mx + n

# collatz sanısı 

# fonksiyon türleri
# 1- parametresiz dönüşsüz
def fonksiyon_ismi():
    print("fonksiyon çalıştı")

fonksiyon_ismi()

def parametresiz_toplama():
    a = 5
    b = 35
    print("a + b toplamı : ", a + b)

parametresiz_toplama()

def a():
    print("zeynep sude oluşturabilyorkigibi")

a()



# 2- parametreli dönüşsüz
# f(x) = ax + b
# f(x1,x2) = ax1 + bx2 + c

def parametreli_fonksiyon(sayi1,sayi2):
    print("sayi1 + sayi2 toplamı : ", sayi1 + sayi2)

def derin(kelime1,kelime2):
    print("kelimelerin birleşmi : ",kelime1+kelime2)

derin("merhaba","Zeynep")

# 3- parametresiz dönüşlü

def parametresiz_donuslu():
    a = 5
    b = 27
    return a + b

print(parametresiz_donuslu())

paramtresiz_sonuc = parametresiz_donuslu()
print("parametresiz donuslu fonksiyon çıktısı : ",paramtresiz_sonuc)

def b():
    x = 10
    y = 5
    return x * y

fonksiyon_sonucu = b()
print("fonksiyon sonucu : ",fonksiyon_sonucu)

# 4- parametreli dönüşlü

def parametreli_donuslu(p1,p2):
    if p1 > p2 :
        return p1
    return p2

enBuyuk = parametreli_donuslu(10, 20)
print("enBuyuk deger : ",enBuyuk)

pi = 3.14
def dairenin_alani(r):
    alan = pi * (r**2)
    return alan

# pi * r * r

yaricap = int(input("yaricap giriniz : "))
sonuc = dairenin_alani(yaricap)
print("dairenin alanı : ", sonuc)





