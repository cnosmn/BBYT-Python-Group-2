#Bir listedeki en büyük ve en küçük elemanı bulma (hazır fonksiyon kullanmadan)


liste = [34, 12, 5, 67, 23, 89, 1, 45]

uzunluk = 0
enkucuk = liste[0]
enbuyuk = liste[0]
while uzunluk < len(liste):
    if enkucuk > liste[uzunluk]:
        enkucuk = liste[uzunluk]

    if enbuyuk < liste[uzunluk]:
        enbuyuk = liste[uzunluk]
        
    uzunluk += 1 # uzunluk = uzunluk + 1

print("Dizinin en küçük değeri : ",enkucuk)
print("Dizinin en büyük değeri : ",enbuyuk)

