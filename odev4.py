# 3 basamaklı bir sayı al   376
# onlar birler ve yuzler olarak
# rakamlarını ayrı ayrı ekrana yazdır

# mod alma ve tam bölme operatörlerini kullanarak
# 123 -> 1*100 + 2*10 + 3*1

#birler basamağı
# 123 % 10  -> 3

# yüzler basamağı
# 123 // 100 -> 1

# 165 
# 165 // 10  -> 16  % 10 -> 6

sayi = int(input("uc basamaklı bir sayı giriniz : "))
print("girilen sayı : ",sayi)

birler = sayi % 10
yuzler = sayi // 100
onlar = (sayi // 10) % 10

print("birler basamagı : ",birler)
print("onlar basamagı : ",onlar)
print("yuzler basamagı : ",yuzler)