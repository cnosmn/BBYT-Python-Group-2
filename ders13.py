


sayi = input("bir sayi giriniz : ")

# 1. yöntem
basamak_sayisi = len(sayi)

#2. yöntem
tam_sayi = int(sayi)
basamak_sayisi2 = 0

while tam_sayi != 0 :
    basamak_sayisi2 += 1
    tam_sayi = tam_sayi // 10


if basamak_sayisi == 1 :
    print("bu sayı palindrom bir sayıdır.")
elif basamak_sayisi == 2 :
    if sayi[0] == sayi[1]:
        print("bu sayı palindrom bir sayıdır.")
elif basamak_sayisi == 3 :
    if sayi[0] == sayi[2] :
        print("bu sayı palindrom bir sayıdır")
elif basamak_sayisi == 4 :
    ters_hali = sayi[-1] + sayi[-2]
    if sayi[:2] == ters_hali : # 4554   -> 45 54
        print("bu sayı palindrom bir sayıdır.")
else :
    print("hizmetçin yok karşında ....")


dizi_hali = list(sayi)
ters_dizi = dizi_hali.copy()
ters_dizi.reverse()

print("dizi hali : ",dizi_hali)
print("ters dizi hali : ",ters_dizi)

if dizi_hali == ters_dizi :
    print("bu sayı palindrom bir sayıdır.")




