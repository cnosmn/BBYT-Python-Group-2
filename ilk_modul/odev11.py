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

sayi = int(input("yarım yılbaşı için sayi girin"))

for i in range(1,sayi+1): # 1,2,3,4,5
    print("*" * i)



# 2-yine kullanıcı veri girecek ama bu sefer tam noel agacı gözükmesi lazım
# aşagıda kullanıcı 4 degerini girmiş
"""
     *
    ***
   *****
  *******
 *********
***********
"""

# 5 girildi en alttaki yıldız sayısı 
# 1. formul = 2n - 1
# 2. formul = girilen sıra numarasının bir eksiği


tam_agac = int(input("yarım yılbaşı için sayi girin"))


for yildiz_sayisi in range(1,tam_agac + 1): # 1,2,3,4,5
    print(" " * (tam_agac - yildiz_sayisi ) + "*" * (2 * yildiz_sayisi - 1))
