
# ileri veri türleri 

# listeler
# demetler (tuple)
# kümeler (set)
# sözlükler (dictionary)

# listeler -> birden fazla veriyi tek bir değişkende tutmamızı sağlar
# sıralı ve değiştirilebilir veri türüdür
# köşeli parantez [] ile oluşturulur
# veri eklenip çıkarılabilir
# indeks ile erişilebilir
# index 0'dan başlar
# aynı veriden birden fazla olabilir

isimler = ["ali", "veli", "ayşe", "fatma",[1,2,3]]

print(isimler)
print(isimler[0])
print(isimler[1])
print(isimler[4][2])
# print(isimler[5]) # index hatası verir

print("liste verisinin type : ", type(isimler))


# 2-Tuple (demet)
# sıralı ancak değiştirilemez veri türüdür
# parantez () ile oluşturulur
# index numarası 0'dan başlar
# veri eklenip çıkarılamaz
# aynı veriden birden fazla olabilir

demet = (2000,2015,2020,2023)
print(demet)
print(demet[2])

demet2 = demet + (2024, 2025)  # demetler değiştirilemez ama yeni demet oluşturulabilir
print("demet verisinin type : ", type(demet))


# 3- Set (küme)
# sırasız ve degistirilebilir veri türüdür
# süslü parantez {} ile oluşturulur
# index numarası yoktur
# aynı veriden birden fazla olamaz

kume = {10.5, 20.5, 30.5, 10.5}

print("kume : ", kume)
print("kume verisinin type : ", type(kume))


# 4- Dictionary (sözlük)
# sırasız ve değiştirilebilir veri türüdür
# süslü parantez {} ile oluşturulur
# anahtar-değer (key-value) çiftlerinden oluşur
# anahtarlar benzersizdir her zaman string
sozluk = {
    "ad": "Ahmet",
    "soyad": "Ahmet",
    "yas": 30,
    "sehir": True
    }
print("sozluk : ", sozluk)
print("sozluk verisinin type : ", type(sozluk))
print("ad : ", sozluk["ad"])
print("keys : ",sozluk.keys())
print("values : ",sozluk.values())


# listeye özel fonksiyonlar
meyveler = ["elma", "armut", "muz"]
meyveler.append("çilek")  # sona ekler
print("append sonrası meyveler : ", meyveler)

meyveler.insert(1,"kavun")  # belirtilen indexe ekler
print("insert sonrası meyveler : ", meyveler)

meyveler.remove("elma")
print("remove sonrası meyveler : ", meyveler)

meyveler.pop()  # sondaki veriyi çıkarır
print("pop sonrası meyveler : ", meyveler)

meyveler.pop(1) # belirtilen indexteki veriyi çıkarır
print("index ile pop sonrası meyveler : ", meyveler)

meyveler.append("ayva")
meyveler.append("armut")
meyveler.append("çilek")
print("append sonrası meyveler : ", meyveler)

meyveler.sort()  # alfabetik sıralar
print("sort sonrası meyveler : ", meyveler)

sayi_listesi = [50, 10, 30, 20, 40]
sayi_listesi.sort()  # küçükten büyüğe sıralar
print("sayı listesi sort sonrası : ", sayi_listesi)

meyveler.reverse()  # listeyi ters çevirir
print("reverse sonrası meyveler : ", meyveler)

print("armut eleman sayısı : ", meyveler.count("armut"))  # armut kaç tane var
print("eleman sayısı : ", len(meyveler))  # listedeki eleman sayısı

meyveler.clear()  # listeyi boşaltır
print("clear sonrası meyveler : ", meyveler)

list1 = [1,2,3]
list2 = [4,5,6]

list3 = list1
print("list1 : ", list1)
print("list3 : ", list3)

list3.append("a")
print("list3 append sonrası : ", list3)
print("list1 append sonrası : ", list1)

list4 = list1.copy()

list4.append("b")
print("list4 append sonrası : ", list4)
print("list1 append sonrası : ", list1)

print("a verisinin dizideki index numarası : ", list4.index('a'))  # a'nın index numarasını verir

list5 = list1 + list2
print("list5 : ", list5)


