
# Koşul yapısı 

# yazım kuralı 
# if (koşul) :
#   (koşul sağlandıgında yapılacak işlemler) 

sayi = 20 

if sayi > 15 :
    print("sayı degişkeni 15 den büyüktür.")

if True :
    print("burası her zaman çalışır")

if 0 :
    print("hiçbir zaman çalışmıcaktı")
#print("her zaman çalışır")


# else  -> değilse
# if olmadan else yazılamaz
# else olmadan if olabilir

"""

if (kosul) :
    koşul saglanırsa çalışan kod
else :
    kosul sağlanmaz ise çalışan kod

""" 


if sayi > 0 :
    print("bu sayı pozitiftir")
else : 
    print("bu sayı negatiftir")

# sayının pozitif negatif olma durumunu kontrol et

"""

degisken = input("bir sayı gir")
degisken = int(degisken)

if degisken > 0 :
    print("bu sayı pozitiftir")
elif degisken == 0 : 
    print("bu sayı nötr")
else :
    print("bu sayı negatiftir")

"""

# if 1 :
#     print("burası çalışır")

# girilen sayının çift mi yoksa tek mi olduğunu bulan program

tam_sayi = int(input("bir tane sayi giriniz : "))

if tam_sayi % 2 == 0 :
    print("evet sayı çifttir")
else :
    print("bu sayı tektir")


a = 10
b = 12
c = 15
# and or not

ucgen_olurmu = True

if a > b+c and a < b-c :
    ucgen_olurmu = False
if b > a+c and b < a-c :
    ucgen_olurmu = False
if c > b+a and c < b-a :
    ucgen_olurmu = False


if ucgen_olurmu == True :
    print("bu kenar uzunlukları ile üçgen oluşturulabilir")
else :
    print("bu kenar uzunlukları ile üçgen oluşturulamaz")