
"""

def kalori_hesapla(egzersiz_turu,sure,agirlik) -> yakilan_kalori

def su_ihtiyaci(egzersiz_suresi) -> su_miktari(ml cinsinden)

def hedef_kontrol(yakilan_kalori,hedef) -> string("tebrikler veya şu kadar kaldı")

def haftalik_rapor(gunluk_veri) -> None

"""

def kalori_hesapla(egzersiz_turu,sure,agirlik):
    # Egzersiz türüne göre dakikada yakılan kalori (70 kg için)
    egzersizler = {
        "koşu": 11.4,
        "yürüyüş": 4.5,
        "bisiklet": 8.0,
        "yüzme": 9.0,
        "halat atlama": 12.0,
        "mekik": 8.0,
        "şınav": 7.0,
        "basketbol": 8.0,
        "futbol": 9.0
    }
    yakilan_kalori = (egzersizler[egzersiz_turu] * agirlik) / 70
    toplam_yakilan = yakilan_kalori * sure
    toplam_yakilan = round(toplam_yakilan, 2)
    return toplam_yakilan

# sonuc = kalori_hesapla("yüzme",40,120)
# print("toplam_yakılan_kalori : ",sonuc)

def su_ihtiyaci(egzersiz_suresi):
    # Her 15 dakika için 200 ml
    su_miktari = (egzersiz_suresi / 15) * 200
    su_miktari = round(su_miktari,2)
    return su_miktari

def hedef_kontrol(yakilan_kalori,hedef):
    # 1 kg yağ -> 7700 kalori 
    fark = hedef - yakilan_kalori
    if fark <= 0 :
        print("Tebrikler, hedefinize ulaştınız")
    else:
        print("Biraz daha yol alman lazım, şu kalori yakman lazım :",fark)

def haftalik_rapor(gunluk_veri):
    # gunluk_veri = {"Pzt":600,"Sal":300....}
    gunler = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]

    for i in range(7): # 0,1,2,3,4,5,6
        print(gunler[i],"günü",gunluk_veri[gunler[i]],"kalori yakıldı.")



isim = input("İsminiz nedir : ")
kilo = int(input("kilonuzu giriniz(kg) : "))
hedef_kalori = int(input("yakılması gereken hedef kalori"))

print("Hoşgeldin",isim)

toplam_kalori = 0

egzersizler = [
        "koşu",
        "yürüyüş",
        "bisiklet",
        "yüzme",
        "halat atlama",
        "mekik",
        "şınav",
        "basketbol",
        "futbol"
        ]

while True:
    print("1-egzersiz ekle")
    print("2-özet gör")
    print("3-sistemi durdur")

    komut = int(input("komut girin"))

    if komut == 1:
        print("Seçebileceğiniz egzersizler : ")
        for egzersiz in egzersizler:
            print(egzersiz)
        
        egzersiz_turu = input("egzersiz girin : ")
        sure = int(input("egzersiz suresini girin(dk) : "))
        yakilan = kalori_hesapla(egzersiz_turu,sure,kilo)
        hedef_kontrol(yakilan,hedef_kalori)

    elif komut == 2:
        hedef_kontrol(yakilan,hedef_kalori)

        if toplam_kalori > 0 :
            toplam_sure = int(input("toplam kaç dakika : "))
            su_miktari = su_ihtiyaci(toplam_sure)
            print("İçmeniz gereken su miktari : ",su_miktari) 

    elif komut == 3:
        print("Program Durduruldu!")
        break

    else:
        print("Program Durduruldu!")
        break
# gunler = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]

gunluk_veri = {
    "Pzt":600,
    "Sal":300,
    "Çar":100,
    "Per":0,
    "Cum":800,
    "Cmt":0,
    "Paz":0
    }
print("\n\n--- HAFTALİK RAPOR ÖRNEĞİ ---")
haftalik_rapor(gunluk_veri)


#Ödev 
#kullanıcının boy verisini de alsın.
#kullanıcının kilosunu aldıktan sonra sistem yakması gereken kaloriyi kendi hesaplasın
# kullanıcının ideal kilosunu hesapla kendi kilosundan çıkar ve bunu 7700 ile çarp bu sayede yakması gereken kaloriyi bulmuş olursun
