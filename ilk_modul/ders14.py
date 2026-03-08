
# İç içe Döngüler 

liste = [1,2,3,4,"kelime","merhaba",[9,2,5,6,2,1],{"isim":"osman","soyisim":"can","yil":2000}]


for eleman in liste : 
    print("eleman : ",eleman)
    print("elemanın türü : ",type(eleman))

    if not isinstance(eleman, int) and not isinstance(eleman, dict):
        print(eleman)
        print(eleman[0])

#ALIŞTIRMALAR

## 1. 1’den 10’a Kadar Sayıları Yazdırma

for i in range(1, 11):
    print(i)

## 2. 1’den 20’ye Kadar Çift Sayıları Yazdırma

for i in range(2, 21, 2):
    print(i)

## 3. Bir Sayının Faktöriyelini Hesaplama
# 5! -> 5.4.3.2.1 -> 120
sayi = 5
sonuc = 1
for i in range(1, 6):
    sonuc = sonuc * i

print(sonuc)

## 4. 1’den 50’ye Kadar Olan Sayıların Toplamı

toplam = 0
for i in range(1, 51):
    toplam += i # toplam = toplam + i

print(toplam)

## 5. Listede Kaç Tane Eleman Olduğunu Bulma

liste = [3, 7, 1, 9, 4]
sayac = 0
for eleman in liste:
    sayac += 1

print(sayac)

## 6. Listede Sadece Tek Sayıları Yazdırma

sayilar = [1, 4, 7, 10, 13, 16]
for s in sayilar:
    if s % 2 == 1:
        print(s)

## 7. Girilen Bir Metni Harf Harf Yazdırma

metin = "Python"
for harf in metin:
    print(harf)

## 8. 1’den 10’a Kadar Sayıların Karelerini Yazdırma

for i in range(1, 11):
    print(i, "karesi:", i**2)


## 9. 1–100 Arası 5’e Bölünen Sayıları Yazdırma

for i in range(1, 101):
    if i % 5 == 0:
        print(i)

## 10. İç İçe Döngü ile 3x3 Yıldız Matrisi

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


