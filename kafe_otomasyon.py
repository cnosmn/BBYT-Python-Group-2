


# print(menu.items())

def menu_goster(menu):
    print("MEZAR Cafe'ye Hoşgeldiniz!")
    for kahve,fiyat in menu.items():
        print(kahve," ---> ",fiyat)

def siparis_al(menu):
    toplam_fiyat = 0
    siparisler = []

    while True :
        print("urun sipari bittiyse tamam yazın")
        siparis = input("ne istersiniz: ")

        if siparis == "tamam":
            break

        if siparis in menu :
            adet = int(input("kaç adet olsun: "))
            fiyat = menu[siparis] * adet
            toplam_fiyat = toplam_fiyat + fiyat
            siparisler.append({"urun" : siparis,"adet" : adet, "tutar" : fiyat})

        else :
            print("Beyfendi/Hanımefendi saçmalamayın lütfen! ")

    return toplam_fiyat,siparisler

def fis_yazdir(siparisler,toplam_fiyat):
    print("MEZAR CAFE Müşteri Sipariş Fişi")
    print("*" * 20)
    for siparis in siparisler:
        print("Ürün :",siparis["urun"],"Adet:",siparis["adet"],"Tutar:",siparis["tutar"],"TL")
    
    print("KDV(%20):", toplam_fiyat * 0.2,"TL")
    print("Toplam Fiyat : ",toplam_fiyat,"TL")
    
def odeme_al(toplam):
    odeme = int(input("Ödenecek tutarı girin: "))
    para_ustu = 0
    
    if toplam > odeme:
        print("Yetersiz Bakiye!")
        return False
    else:
        para_ustu = odeme - toplam
        print("Para Ustunuz : ",para_ustu)
        print("Ödeme Başarılı, Yine Bekleriz :)")
        return True

menu = {
    "filtre_kahve": 40,
    "espresso" : 20,
    "latte" : 50,
    "americano" : 50,
    "capuccino" : 50,
    "turk kahvesi" : 30,
    "cay" : 15,
    "su" : 15
}

menu_goster(menu)
fiyat,siparisler = siparis_al(menu)

if len(siparisler) == 0 :
    print("Sipariş Yok!")
else:
    fis_yazdir(siparisler,fiyat)
    odeme_al(fiyat)



