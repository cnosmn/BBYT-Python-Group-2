# kullanıcının 3 tane string veri alıcaksınız
# bu verilerin :
# birinicisinin ilk 3 karakteri 
# ikincisinin son 2 karakteri
# üçüncüsünün ortadaki karakteri ekrana yazdırılacak
# daha sonra bu kesilen karakterlerin birleşimini ekrana yazıcak ->üçünün birleşmiş halini

# kullanıcıdan en az 25 karakter uzunluğunda 1 tane string veri alınız
# bu verinin ilk 5 karakterini ve son 5 karakterini ekrana yazdırınız

# kullanıcıdan 3 tane sayı al 2 tanesi tam sayı 1 tanesi ondalıklı sayı olsun
#bu sayıların birbiri arasında büyüklük küçüklük karşılaştırmasını yazınız


# BİRİNCİ KISIM
veri1 = input("Lütfen birinci string veriyi giriniz: ")
veri2 = input("Lütfen ikinci string veriyi giriniz: ")
veri3 = input("Lütfen üçüncü string veriyi giriniz (6 harfli veri girin): ")

print("Birinci verinin ilk 3 karakteri:", veri1[:3]) # merhaba 
print("İkinci verinin son 2 karakteri:", veri2[-2:]) # merhaba
print("Üçüncü verinin ortadaki karakteri:",veri3[2:4]) # merhab 2 : 4

birlesim = veri1[:3] + veri2[-2:] + veri3[2:4]
print("Kesilen karakterlerin birleşimi:", birlesim)

# uzunluk = len(veri1)
# print("uzunluk veri tipi : ",type(uzunluk))
# print("veri1 harf uzunluğu:", uzunluk)

#   10 tane harf var        4:6  4. ve 5.  index

#İKİNCİ KISIM

sayi1 = int(input("Lütfen birinci tam sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci tam sayıyı giriniz: "))
sayi3 = float(input("Lütfen ondalıklı sayıyı giriniz: "))

temp = sayi1 > sayi2
print("1. vs 2. :", temp )
temp = sayi1 > sayi3
print("1. vs 3. :", temp )
temp = sayi2 > sayi3
print("2. vs 3. :", temp )

temp = sayi1 < sayi2
print("1. vs 2. :", temp )
temp = sayi1 < sayi3
print("1. vs 3. :", temp )
temp = sayi2 < sayi3
print("2. vs 3. :", temp )

