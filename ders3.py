
# string ile işlemler

metin1 = "Merhaba "
metin2 = "Dünya"

# birleştirme (concatenation)
sonuc = metin1 + " " + metin2  # "Merhaba Dünya"  3 + 3 -> 6
# "3" + "3" -> "33"
print(sonuc)  # Merhaba Dünya

# tekrar etme
tekrar = metin1 * 3   #"MERHABAMERHABAMERHABA"
print(tekrar)  # MerhabaMerhabaMerhaba

# string indeksleme ve dilimleme (slicing)
metin = "Python Programlama Dili"
print("0. index : ",metin[0])    # P
print("7. index : ",metin[7])    # P
print("18. index : ",metin[18])   # " "
print("Son index : ",metin[-1])   # i
print("Sondan 2. index : ",metin[-2]) # l

# dilimleme (slicing)
print("İlk 6 karakter : ",metin[0:6])  # Python
print("ilk 5 karakter : ",metin[:5])   # Python
print("7. karakterden sonuna kadar : ",metin[7:])  # Programlama Dili

# f string kullanımı
ad = "Ahmet"

print(f"Merhaba {ad}, nasılsın?")  # Merhaba Ahmet, nasılsın?

# 3.14151941239538345943
pi = 3.14151941239538345943
print(f"Pi sayısı: {pi:.5f}")  # Pi sayısı: 3.14


"""
isim- soyisim - yaş - şehir bilgilerini kullanıcıdan alıp
isim[:7]  => ilk 7 karakter
soyisim[5:] => soyismin son 3 karakteri

"""


# operatörler 
# Aritmetik operatörler: +, -, *, /, //, %, **
a = 10
b = 3

print("tam bölme operatörü : ", a // b)  # 3

print("üs alma işlemi : ", a ** b)  # 1000

# mod alma operötürü
print("mod alma operatörü : ", a % b)  # 1

# karşılaştırma operatörleri: ==, !=, >, <, >=, <=

print( a == b)  # False
print( a != b)  # True
print( a > b)   # True
print( a < b)   # False
print( a >= b)  # True
print( a <= b)  # False

# Mantıksal operatörler: and, or, not
                        #    0 n 1 n 1  -> 0
                        # False  and  True  and True
print("and cevabı : ", (a == b) and (a != b) and ( a > b))  # False
print("or cevabı : ", (a == b) or (a != b) or (a > b))   # True
print("not cevabı : ", not (a == b))  # True
print("not and cevabı : ", not (a == b and a != b and  a > b)) # True
