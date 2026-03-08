

# recursive function


def yinelemeli(sayi):
    if sayi <= 0 :
        return 0
    return sayi + yinelemeli(sayi-1)

toplam = yinelemeli(20)
print("yinelemeli toplam : ",toplam)

# girilen sayının faktöriyelini hesaplayan recursive fonksiyon

def faktoriyel(sayi):
    if sayi <= 1 :
        return 1
    return sayi * yinelemeli(sayi-1)

faktoriyel_sonuc = faktoriyel(20)
print("faktoriyel : ",faktoriyel_sonuc)



# fibanocci dizisi

# 1 1 2 3 5 8 13 21 34
# kullanıcının girdiği sıra numarasındaki fibonaci serisindeki sayıyı bulan kod


def fibonacci(sira_numarasi):

    if sira_numarasi <= 0 or sira_numarasi == 1 or sira_numarasi == 2 :
        return 1
    
    sayi1 = 1
    sayi2 = 1
    print(sayi1)
    print(sayi2)

    for i in range(2,sira_numarasi):
        temp = sayi2
        sayi2 = sayi2 + sayi1
        sayi1 = temp
        print(sayi2)
    return sayi2

kullanici_sayisi = int(input("fibonacci sıra numarası girin1"))
fibo_sonuc = fibonacci(kullanici_sayisi)
print(kullanici_sayisi, "sırasında olan sayi : ",fibo_sonuc)


"""
Ödev

1- ters_cevir(1234) -> 4321 olarak dönene recursive fonksiyon yazın
2- basamak_sayisi(4589) -> 4 basamaklı  dönen recursive fonksiyon

"""

# https://codeshare.io/a3zemD

    