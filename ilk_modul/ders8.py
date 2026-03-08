meyveler = ["elma", "armut", "muz"]

print(meyveler[0][0]) # elma -> e
print(meyveler[1][0]) # armut -> r
print(meyveler[2][0]) # muz   -> u

# Döngüler
# for döngüsü özellikleri
# 1- Belirli sayıda tekrarlama yapar
# 2- Liste, demet, sözlük gibi veri yapılarında kullanılır 
# 3- for döngüsü ile birlikte range() fonksiyonu sıkça kullanılır
# 4- Döngü sayacı otomatik olarak artar
# 5- Döngü sayacı manuel olarak da değiştirilebilir
#
# for döngüsü
"""
for döngüsü yazılışı

for i in range(başlangıç, bitiş, adım): 
    # yapılacak işlemler
print("merhaba")
veya 

for eleman in veri_yapısı:
    # yapılacak işlemler
    print("merhaba")

"""
for i in range(10):  # 0,1,2,3,4,5,6,7,8,9
    print("Sayac : ", i)

print("***********************")
for i in range(5,12): # 5,6,7,8,9,10,11
    print("Sayac  : ", i)

print("***********************")

for i in range(2,21,2): # 2,4,6,8,10,12,14,16,18,20
    print("Sayac : ", i)

print("***********************")

for i in range(20,1,-3): # 20,17,14,11,8,5,2
    print("Geri Sayım : ", i)

print("***********************")

for meyve in meyveler:
    print("Meyve Adı : ", meyve[0])

print("***********************")

# while döngüsü özellikleri 
# 1- Belirli bir koşul sağlanana kadar döngü devam eder
# 2- Döngü sayacı manuel olarak artırılmalıdır
# 3- Döngü sayacı artırılmazsa sonsuz döngü oluşabilir
# 4- Koşul sağlanmazsa döngü hiç çalışmayabilir
# 5- while döngüsü ile birlikte break ve continue ifadeleri sıkça kullanılır
# while döngüsü
"""
koşul sağlanana kadar döngü çalışır

while (koşul):
    # yapılacak işlemler

"""

sayi = 0

print("sayi < 5 : ",sayi < 5 )
while sayi < 5 :
    print("Sayı Değeri : ", sayi)
    sayi += 1  # sayi = sayi + 1


# while True:
#     print("Bu döngü sonsuza kadar çalışır")

# while 1 :
#     print("Bu döngüde sonsuza kadar çalışır")


# 1'den n'e kadar sayıların toplamı

kullanici_verisi = int(input("Bir sayı giriniz: "))
toplam = 0
for i in range(kullanici_verisi): # 0,1,2,3,4
    toplam = toplam + i

print("Girdiğiniz sayıya kadar olan sayıların Toplamı : ", toplam)