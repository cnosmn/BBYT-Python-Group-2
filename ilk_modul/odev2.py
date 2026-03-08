print("Oyun Karakteri Oluşturucusuna Hoşgeldiniz!")

ad = input("Lütfen karakterinizin adını giriniz: ")
yas = int(input("Lütfen karakterinizin yaşını giriniz: "))
seviye = int(input("Lütfen karakterinizin seviyesini giriniz: "))
altin_miktari = float(input("Lütfen karakterinizin sahip olduğu altın miktarını giriniz: "))
saglik_puani = int(input("Lütfen karakterinizin sağlık puanını giriniz: "))
sihirli_guc = bool(input("Karakterinizin sihirli güce sahip olup olmadığını giriniz (True/False): "))

toplam_guc = (seviye * 10)  + (saglik_puani / 2)
deneyim = seviye * 100


print("=======================================")
print("KARAKTER KARTI\n")
print("=======================================")
print("Ad : ", ad)
print("Yaş : ", yas)
print("Seviye : ", seviye)
print("=======================================")
print("Altın Miktarı : ", altin_miktari, " gold")
print("Sağlık Puanı : ", saglik_puani, " HP")  # 70 HP 
print("Toplam Güç : ", toplam_guc)
print("Sonraki Seviye : ", deneyim, " XP")
print("Sihirli Güç : ", sihirli_guc)
print("=======================================")

