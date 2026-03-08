
# Alıştırma 1
# Boş bir alışveriş listesi oluşturun
# append() ile 5 ürün ekleyin
# Listenin uzunluğunu yazdırın
# Son eklenen ürünü pop() ile çıkarın
# Güncel listeyi yazdırın
alisveris_listesi = []
print("tip : ",type(alisveris_listesi))
alisveris_listesi.append("elma")
alisveris_listesi.append("ekmek")
alisveris_listesi.append("süt")
alisveris_listesi.append("peynir")
alisveris_listesi.append("yumurta")
print("Alisveris Listesi : ",alisveris_listesi)
print("Liste uzunluğu : ",len(alisveris_listesi))
alisveris_listesi.pop()
print("Güncel Alisveris Listesi : ",alisveris_listesi)
print("************************************************")
# Alıştırma 2
# Bir sınıftaki öğrenci isimlerini liste olarak oluşturun (en az 6 isim)
# count() ile "Ahmet" isminin kaç kere geçtiğini bulun
# index() ile "Ayşe" isminin kaçıncı sırada olduğunu bulun
# len() ile toplam öğrenci sayısını yazdırın
ogrenciler = ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ahmet", "Can"]
print("Öğrenci Listesi : ", ogrenciler)
print("Ahmet ismi sayısı : ", ogrenciler.count("Ahmet"))
print("Ayşe ismi indexi : ", ogrenciler.index("Ayşe"))
print("Toplam öğrenci sayısı : ", len(ogrenciler))
print("************************************************")

# Alıştırma 3
# 8 şarkı adı içeren bir liste oluşturun
# 3. ve 5. index numaralı şarkıları silin (pop veya remove ile)
# 2 yeni şarkı ekleyin (append)
# Listenin ilk 3 şarkısını yazdırın (dilimleme: [:3])
# Toplam şarkı sayısını yazdırın
sarkilar = ["ankara rüzgarı", "radioactive", "jingle bells", "hav hav hav", "softcore", "sonbahar", "dönsen bile", "ela"]
print("Şarkı Listesi : ", sarkilar)
sarkilar.pop(3)
sarkilar.pop(5)
print("Güncel Şarkı Listesi : ", sarkilar)
sarkilar.append("y")
sarkilar.append("after dark")
sarkilar.append("friends")

print("İlk 3 Şarkı : ", sarkilar[:3])
print("Toplam Şarkı Sayısı : ", len(sarkilar))
