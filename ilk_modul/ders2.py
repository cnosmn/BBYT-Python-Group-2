# print yazım türler 
degisken = 20
# 1. tür
print("Merhaba Dünya")
print(degisken)
# 2. tür
print("değiken degerim: ", degisken , "burası devamı",degisken)
# 3. tür
print(f"degisken degerim: {degisken}") 
# 4. tür
print("degisken degerim: {} {}".format(degisken,degisken))

"""
input() fonksiyonu ile kullanıcıdan veri alma
Tip dönüşümleri (int(), float(), str())
"""

# bir değişkenin türünü öğrenme
print(type(degisken))
print(type("Merhaba"))
print(type(3.14))
print(type(True))


# TİP DÖNÜŞÜMLERİ
# type casting

tam_sayi = 25
ondalik_sayi = 10.5
metin = "Python"
boolean_deger = False

print("float to int : ",int(ondalik_sayi))  # float to int
print("int to float : ",float(tam_sayi))  # int to float
print("int to str : ",str(tam_sayi))      # int to str
print("float to str : ",str(ondalik_sayi))  # float to str
print("str to int : ",int("100"))         # str to int
#print("hatalı dönüşüm : ",int("Python"))   # str to int hata verir

# kullanıcıdan veri alma
kullanici_adi = input("Lütfen kullanıcı adınızı giriniz: ")

print("Kullanıcı Adınız: ", kullanici_adi)

# input aldığı veriyi her zaman string türünde alır

# ilk yöntem tip dönüşümü int(input("sayi giriniz: "))
yas = input("Lütfen yaşınızı giriniz: ")

# ikinci yöntem tip dönüşümü
yas = int(yas)  # "20" -> 20

print("Yaşınız: ", yas)
print("girilen yaşın türü: ", type(yas))

print("dogdugun yıl : ",2025 - yas)

