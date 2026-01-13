# Python Fonksiyonlar - Örnek Uygulamalar

## 1. Temel Seviye - Selamlama Fonksiyonu

```python
def selamla(isim):
    """Verilen ismi selamlayan fonksiyon"""
    print(f"Merhaba {isim}!")

# Kullanımı
selamla("Ahmet")
selamla("Zeynep")
```

## 2. Geriye Değer Döndüren Fonksiyon - Alan Hesaplama

```python
def dikdortgen_alan(uzunluk, genislik):
    """Dikdörtgen alanını hesaplar"""
    alan = uzunluk * genislik
    return alan

# Kullanımı
sonuc = dikdortgen_alan(5, 3)
print(f"Dikdörtgenin alanı: {sonuc}")
```

## 3. Çift mi Tek mi?

```python
def cift_mi(sayi):
    """Sayının çift olup olmadığını kontrol eder"""
    if sayi % 2 == 0:
        return True
    else:
        return False

# Kullanımı
print(cift_mi(10))  # True
print(cift_mi(7))   # False
```

## 4. Hesap Makinesi

```python
def hesap_makinesi(sayi1, sayi2, islem):
    """Basit hesap makinesi fonksiyonu"""
    if islem == "topla":
        return sayi1 + sayi2
    elif islem == "cikar":
        return sayi1 - sayi2
    elif islem == "carp":
        return sayi1 * sayi2
    elif islem == "bol":
        if sayi2 != 0:
            return sayi1 / sayi2
        else:
            return "Sıfıra bölme hatası!"
    else:
        return "Geçersiz işlem!"

# Kullanımı
print(hesap_makinesi(10, 5, "topla"))   # 15
print(hesap_makinesi(10, 5, "carp"))    # 50
```

## 5. Not Ortalaması Hesaplama

```python
def not_ortalamasi(notlar):
    """Verilen notların ortalamasını hesaplar"""
    toplam = sum(notlar)
    ortalama = toplam / len(notlar)
    return ortalama

def harf_notu(ortalama):
    """Ortalamaya göre harf notu verir"""
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 80:
        return "BA"
    elif ortalama >= 70:
        return "BB"
    elif ortalama >= 60:
        return "CB"
    elif ortalama >= 50:
        return "CC"
    else:
        return "FF"

# Kullanımı
notlarim = [85, 90, 78, 92]
ort = not_ortalamasi(notlarim)
print(f"Ortalamanız: {ort:.2f}")
print(f"Harf notunuz: {harf_notu(ort)}")
```

## 6. Asal Sayı Kontrolü

```python
def asal_mi(sayi):
    """Sayının asal olup olmadığını kontrol eder"""
    if sayi < 2:
        return False
    
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    
    return True

# Kullanımı
print(f"7 asal mı? {asal_mi(7)}")
print(f"10 asal mı? {asal_mi(10)}")
```

## 7. Şifre Güvenlik Kontrolü

```python
def sifre_guclu_mu(sifre):
    """Şifrenin güçlü olup olmadığını kontrol eder"""
    if len(sifre) < 8:
        return False, "Şifre en az 8 karakter olmalı!"
    
    buyuk_harf = any(c.isupper() for c in sifre)
    kucuk_harf = any(c.islower() for c in sifre)
    rakam = any(c.isdigit() for c in sifre)
    
    if buyuk_harf and kucuk_harf and rakam:
        return True, "Şifre güçlü!"
    else:
        return False, "Şifre büyük harf, küçük harf ve rakam içermeli!"

# Kullanımı
sonuc, mesaj = sifre_guclu_mu("Abc123xyz")
print(mesaj)
```

## 8. Kelime Sayacı

```python
def kelime_say(metin):
    """Metindeki kelime sayısını bulur"""
    kelimeler = metin.split()
    return len(kelimeler)

def en_uzun_kelime(metin):
    """Metindeki en uzun kelimeyi bulur"""
    kelimeler = metin.split()
    en_uzun = max(kelimeler, key=len)
    return en_uzun

# Kullanımı
cumle = "Python programlama öğrenmek çok eğlenceli"
print(f"Kelime sayısı: {kelime_say(cumle)}")
print(f"En uzun kelime: {en_uzun_kelime(cumle)}")
```
