# 1-100 arası asal sayıları bulma

# asal sayı olma kuralı
# sadece kendisine ve 1'e bölünebilen sayılar


# girilen sayının asal olup olmadıgını bulan kod 

sayi = int(input("bir sayi girin : "))

asal_mi = True
for i in range(2,sayi): # 2,3,4,5,.....sayi-1
    if sayi % i == 0 :
        print("bu sayi asal değildir")
        asal_mi = False
        break

if asal_mi :
    print("bu sayı asaldır")

print(2)
sayac = 3
while sayac <= 100: # 3,4,5,6,7,8,9 --> 100
    asal_mi2 = True
    for i in range(2,sayac): # 2,3,4
        if sayac % i == 0 :
            asal_mi2 = False
    if asal_mi2 :
        print(sayac)
    sayac = sayac + 1


# çarpım tablosu

# 1 # 2 # 3 # 4 ..... # 10
#1
#2
#3
#4
#5


for i in range(1,11):
    satir = ""
    for j in range(1,11):
        satir = satir + str(i*j) +" "
    print(satir)

# Ödev
#Piramit ve şekil çizme algoritmaları

"""
*
**
***
****
*****
"""
# 1- kullanıcının girdiği değere göre yarım noel agacı yapan döngü kodu
# yukarıda kullanıcı 5 girmiş 
print(25)
print(27)


# 2-yine kullanıcı veri girecek ama bu sefer tam noel agacı gözükmesi lazım
# aşagıda kullanıcı 4 degerini girmiş
"""
     *
    ***
   *****
  *******
"""
dizi = ["elma","muz","armut","ananas","üzüm","karpuz"]



for i in dizi:
    if i[0] == "a":
        print(i)


for i in range (1,100):
    i = str(i)
    if len(i) == 1: 
        print(i)
    elif i[0] == i[1]:
        print(i)

