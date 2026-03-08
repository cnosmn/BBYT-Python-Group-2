"""
Armstrong Sayısı Nedir?
Bir sayının basamaklarındaki rakamların, 
basamak sayısı kadar kuvvetleri toplamı, 
sayının kendisine eşitse bu sayıya Armstrong sayısı denir.
"""

# 123 -> 1**3  + 2**3 + 3**3
# 18  -> 1**2  + 8**2 
sayi = int(input("bir sayi giriniz : "))
tutucu = sayi
asil_sayi = sayi
basamak_sayisi = 0

while sayi != 0 :
    basamak_sayisi = basamak_sayisi + 1
    sayi = sayi // 10

print("basamak sayısı : ",basamak_sayisi)

print("sayi degeri : ",sayi)
toplam = 0
for i in range(1,basamak_sayisi+1): # 1,2,3,4,5  # tutucu = 123
    basamak = tutucu % 10 
    tutucu = tutucu // 10
    toplam = toplam + basamak**basamak_sayisi  # 2**3  -> 8

print("basamaklarının kuvvetlerinin toplamı : ",toplam)

if toplam == asil_sayi :
    print("girdiğiniz sayi armstrong sayısıdır.")
else :
    print("malesef girilen sayi armstrong sayısı degildir.")

# "dfgfdgdf"
sayi2 = int(input("bir sayi daha girin : "))

basamak_uzunlugu = len(str(sayi2))  #  "1456" -> len("1456")  -> 4 

print("basamak sayısı (kolay yöntem) : ",basamak_uzunlugu)
