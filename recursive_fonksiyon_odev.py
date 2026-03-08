def ters_cevir(metin):
    if len(metin) == 0:
        return metin
    return metin[-1] + ters_cevir(metin[:-1])


sonuc = ters_cevir("Python")
print("ters cevrilmis hali : ",sonuc)


def tersten(saayi):
    if saayi > 0 :
        if saayi < 10 :
            return str(saayi)
        else :
            return str(saayi % 10) + tersten(saayi // 10)
    
saayi = input("sayı giriniz : ")
print("ters hali :" ,tersten(saayi))


def tersten2(sayi,tersten_sayi=0):
    tersten_sayi = tersten_sayi * 10

    if sayi > 0 :
        if sayi < 10 :
            return tersten_sayi + sayi
        
        tersten_sayi = tersten_sayi + sayi % 10
        return tersten2(sayi // 10,tersten_sayi)
    else :
        return 0

def basamak_sayisi(sayi):
    sayi = abs(sayi)  #chatgbt ye sordum negatif için ne yapmalıyım diye bunu önerdi 

    if sayi < 0 :
        sayi = sayi * -1

    if sayi < 10:
        return 1
    else:
        return 1 + basamak_sayisi( sayi // 10)
    
sayi = int(input("bir sayı giriniz : "))
print("basamak_sayisi: ",basamak_sayisi(sayi))

