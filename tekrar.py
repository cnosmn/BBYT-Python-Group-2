

# veri türleri
#  int, float, str, bool
# değişkenler
# operatörler
# +, -, *, /, %, //, **  
# mantıksal operatörler: and, or, not
# if-else
# if kosul :
#     # koşul doğruysa çalışacak kod
# elif diger_kosul:
#     # diğer koşul doğruysa çalışacak kod
# else:
#     # hiçbir koşul doğru değilse çalışacak kod

# döngüler
# for , while 


while True:
    sayi = int(input("Bir sayı girin:  "))
    if sayi < 0 :
        print("Negatif sayı girdiniz, lütfen pozitif bir sayı girin.")
    elif sayi == 0:
        print("Sıfır girdiniz, lütfen pozitif bir sayı girin.")
    else:
        print("Girdiğiniz sayı: ",sayi)
        break


# ileri veri yapıları


# listeler(list), demetler(tuple), sözlükler(dict), kümeler(set)

liste = [1, 2, 3, 4, 5]
print(liste)




# fonksiyonlar

def fonksiyon_ismi(param1,param2):

    toplam = param1 + param2
    print("Toplam: ", toplam)
    return toplam

sonuc = fonksiyon_ismi(10, 20)
print("Fonksiyon sonucu: ", sonuc)

"""
Ödev projeleri

1-emir
kitap özeti uygulaması
kullanıcı kitap adını yazıcak sistem kullanıcıya 
o kitap sistemde varsa özetini verecek yoksa kitap bulunamadı diyecek

2-Zeynep
kullanıcı elindeki minecraft evreninin malzemeleri sisteme yazıcak daha sonra 
sistem kullanıcıya neler yapabileceğini söyleyecek örneğin kullanıcı elinde 
10 odun, 5 taş, 2 demir var yazacak sistem kullanıcıya 2 kılıç, 
1 zırh yapabileceğini söyleyecek

3-Mavi
bir giriş sistemi olucak kullanıcının login,register,logout, 
şifre değiştirme gibi işlemleri yapabileceği bir sistem olacak

4-Derin
oyun karakteri seçimi yardımcısı
minecraft canavarları olsun creeper, zombie, skeleton, enderman 
kullanıcı canavarın adını yazıcak sistem kullanıcıya o canavar hakkında bilgi verecek

"""



