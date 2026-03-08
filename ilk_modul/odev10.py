# Collatz sanısı ödevi 
# döngüler kullanarak yazın


# 157 -> 472 -> 236 -> 118 -> 59 -> 178 -> 89 -> 268 -> 134 -> 67 -> 202 -> 101 -> 304 -> 152 -> 76 ->38 -> 19 -> 58 -> 29 -> 88 -> 44 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1


# görev
# kullanıcıdan sayı al
# bu sayıyı 1 e ulaşana kadar işlem yapıcaz
# her adımda işlem sonucunu yazdırıcaz

sayi = int(input("bir sayi giriniz : "))
sonuc = [sayi]
liste = [1,2,3]

while sayi != 1 :
    if sayi % 2 == 0 :
        sayi = sayi/2
    else :
        sayi = (3 * sayi) + 1 
    sonuc.append(sayi)

print("işlem sonucu sayılar : ",sonuc)
