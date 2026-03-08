kitaplar = {
    "Sefiller": "Victor Hugo'nun yazdıgı, adalet ve merhamet temasını isleyen bir romandır.",
    "Küçük Prens": "Antoine de Saint-Exupéry'nin yazdığı, dostluk ve hayat üzerine bir hikayedir.",
    "Suç ve Ceza": "Dostoyevski'nin yazdıgı, vicdan ve suc kavramlarını ele alan bir romandır."
}

kitap_ismi = input("Lütfen kitap ismini giriniz: ")
if kitap_ismi in kitaplar:
    print("Kitap bulundu!")
    print("Özet:", kitaplar[kitap_ismi])
else:
    print("Kitap bulunamadı.")


liste = [1,2,3,4,5]

icinde_mi = 7 in liste
print("icinde_mi : ",icinde_mi)


sozluk = {
    "ad":"osman",
    "soyad":"can"
}




