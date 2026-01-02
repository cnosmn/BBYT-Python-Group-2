
# 0 dan 50 e kadar olan çift sayıların toplamı

toplam = 0
toplam2 = 0
for i in range(50):  # 0,1,2,3,4,5,...,49
    if i % 2 == 0:
        toplam = toplam + i
        

print("0 dan 50 e kadar olan çift sayıların toplamı : ", toplam)
    
for sayi in range(0,50,2):  # 2,4,6,8,...,50
    toplam2 = toplam2 + sayi

print("0 dan 50 e kadar olan çift sayıların toplamı (ikinci yöntem) : ", toplam2)


 
liste = [1,2,3]
print("döngü öncesi liste verisi : ",liste)
while len(liste) <= 6 :
    liste.append(99)
print("döngü sonrası liste verisi :",liste)

liste2 = [1,2,3]
sayac = 4
print("döngü öncesi liste2 verisi : ",liste2)

while len(liste2) <= 6:
    liste2.append(sayac)
    sayac = sayac + 1
print("döngü sonrası liste2 verisi : ",liste2)

