# armstrong sayisini bulan kodu fonksiyona çevirin.
# paramtereli ve dönüşlü olsun
# ders12.py içerisinde armstrong sayısını bulan kod var.
# bu kod fonksiyona çevrilicek

# armstrong_sayisi() -> evet(true) veya hayır(false) string dönsün

# giriş verisi : sayi   -> True veya False

def armstrong_sayisi(sayi):
    tutucu = sayi

    # "dfgfdgdf"
    basamak_sayisi = len(str(sayi))  #  "1456" -> len("1456")  -> 4 
    print("basamak sayısı : ",basamak_sayisi)

    toplam = 0
    for i in range(1,basamak_sayisi+1): # 1,2,3  # 102 10 1
        basamak = tutucu % 10 # 2 0 1
        tutucu = tutucu // 10 # 10 1 0
        toplam = toplam + basamak**basamak_sayisi  # 2**3 + 0**3 + 1**3 = 9

    print("basamaklarının kuvvetlerinin toplamı : ",toplam)

    # if toplam == sayi :
    #     return True
    # return False
    return True if toplam == sayi else False

sayi = int(input("bir sayi giriniz : "))

sonuc = armstrong_sayisi(sayi)

if sonuc :
    print("girdiğiniz sayi armstrong sayısıdır.")
else :
    print("malesef girilen sayi armstrong sayısı degildir.")