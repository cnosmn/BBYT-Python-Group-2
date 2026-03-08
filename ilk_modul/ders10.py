
email = input("lütfen mail adresinizi giriniz : ")
sifre = input("lütfen şifrenizi giriniz : ")

kullanici_email = "osman@acikatolye.com.tr"
kullanici_sifre = "123456"


# break , continue , pass
while True :
    if email == kullanici_email and sifre == kullanici_sifre:
        print("giriş başarılı, teşekkürler")
        break # döngü durdurur

    email = input("lütfen mail adresinizi giriniz : ")
    sifre = input("lütfen şifrenizi giriniz : ")

    if len(email) < 5 :
        continue

print("Sisteme başarılı şekilde giriş yaptınız")


if sayi < 10 :
    pass

for i in range(5):
    pass

"""
for sayi in range(0,50,2):  # 2,4,6,8,...,50
    toplam2 = toplam2 + sayi

"""

iterator = 0
toplam3 = 0
while iterator < 50 :
    toplam3 = toplam3 + iterator
    iterator = iterator + 2
print("while döngüsü ile yazdığımız toplam değeri : ",toplam3)

# faktöriyel (sayı)!    5!  -> 5.4.3.2.1  30! -> 30.29.28.27.....1

# kullanıcıdan alınan değerin faktöriyelini hesaplayan program

sonuc = 1
veri = int(input("faktöriyeli hesapalanacak sayıyı giriniz : "))

# for i in range(veri,0,-1)
for i in range(1,veri+1):
    sonuc = sonuc * i 

print("girdiğiniz sayının faktöriyel değeri : ",sonuc)


# Collatz sanısı ödevi 
# döngüler kullanarak yazın


# 157 -> 472 -> 236 -> 118 -> 59 -> 178 -> 89 -> 268 -> 134 -> 67 -> 202 -> 101 -> 304 -> 152 -> 76 ->38 -> 19 -> 58 -> 29 -> 88 -> 44 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1