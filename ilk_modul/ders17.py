# parametre : sayi1(float) , sayi2(float) , islem_turu(string)
# dönüş : float

def hesap_makinesi(sayi1, sayi2, islem_turu):
    if islem_turu == "+":
        toplam = sayi1 + sayi2
        return toplam
    
    if islem_turu == "-":
        cikarma = sayi1 - sayi2
        return cikarma
    
    if islem_turu == "*":
        carpma = sayi1 * sayi2
        return carpma
    
    if islem_turu == "/":
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayi sıfır olamaz."
        else :
            bolme = sayi1 / sayi2
            return bolme
        
sonuc = hesap_makinesi(10.0,20.5,"+")
print("islemin sonucu:", sonuc)

sonuc = hesap_makinesi(10.0,20.5,"-")
print("islemin sonucu:", sonuc)

sonuc = hesap_makinesi(10.0,20.5,"*")
print("islemin sonucu:", sonuc)

sonuc = hesap_makinesi(10.0,20.5,"/")
print("islemin sonucu:", sonuc)

sonuc = hesap_makinesi(10.0,0,"/")
print("islemin sonucu:", sonuc)


"""
| Değer                       | Normal Aralık         | Düşükse (Az)                                   | Yüksekse (Çok)               |
| --------------------------- | --------------------- | ---------------------------------------------- | ---------------------------- |
| **Hemoglobin (Hb)**         | 12 – 17 g/dL          | Kansızlık (anemi), yorgunluk, baş dönmesi      | Kan koyulaşması, pıhtı riski |
| **WBC (Beyaz Kan Hücresi)** | 4.000 – 11.000 /µL    | Bağışıklık zayıflığı, enfeksiyonlara yatkınlık | Enfeksiyon, iltihap          |
| **Trombosit (PLT)**         | 150.000 – 450.000 /µL | Kanama riski, kolay morarma                    | Pıhtı riski, inme            |
| **Glukoz (Açlık)**          | 70 – 100 mg/dL        | Hipoglisemi, bayılma                           | Diyabet riski                |

"""

# dönüş olarak bize string listesi dönmesini istiyorum.
def kan_testi(hemoglobin, wbc, trombosit, glukoz):
    #sonuc_listesi = []
    # Hemoglobin testi
    if hemoglobin < 12 :
        print("Hemoglobin düzeyi düşük. Kansızlık olabilir.")
    elif hemoglobin > 17:
        print("Hemoglobin düzeyi yüksek. Kan koyulaşması, pıhtı riski olabilir.")
    else :
        print("Hemoglobin düzeyi normal.")
    
    # wbc testi
    if wbc < 4000 :
        print("WBC düzeyi düşük. Bağışıklık zayıflığı olabilir.")
    elif wbc > 11000:
        print("WBC düzeyi yüksek. Enfeksiyon, iltihap olabilir.")
    else :
        print("WBC düzeyi normal.")
    
    # trombosit testi
    if trombosit < 150000 :
        print("Trombosit düzeyi düşük. Kanama riski olabilir.")
    elif trombosit > 450000:
        print("Trombosit düzeyi yüksek. Pıhtı riski olabilir.")
    else :
        print("Trombosit düzeyi normal.")

    # glukoz testi
    if glukoz < 70 :
        print("Glukoz düzeyi düşük. Hipoglisemi olabilir.")
    elif glukoz > 100:
        print("Glukoz düzeyi yüksek. Diyabet riski olabilir.")
    else :
        print("Glukoz düzeyi normal.")

    #return sonuc_listesi


"""
## Test Senaryosu 1 – Tüm Değerler Normal

**Beklenen sonuç:** “Genel durum normal”

* Hemoglobin (Hb): **14.2**
* WBC: **7.500**
* Trombosit (PLT): **250.000**
* Glukoz (Açlık): **90**

---

## Test Senaryosu 2 – Kansızlık Şüphesi

**Beklenen sonuç:** “Hemoglobin düşük uyarısı”

* Hemoglobin (Hb): **9.8** 🔻
* WBC: **6.200**
* Trombosit (PLT): **280.000**
* Glukoz (Açlık): **85**

---

## Test Senaryosu 3 – Enfeksiyon Şüphesi

**Beklenen sonuç:** “WBC yüksek uyarısı”

* Hemoglobin (Hb): **13.5**
* WBC: **15.300** 🔺
* Trombosit (PLT): **300.000**
* Glukoz (Açlık): **92**
## Test Senaryosu 4 – Pıhtılaşma Riski

**Beklenen sonuç:** “Trombosit yüksek uyarısı”

* Hemoglobin (Hb): **16.8**
* WBC: **8.100**
* Trombosit (PLT): **520.000** 🔺
* Glukoz (Açlık): **95**
---

## Test Senaryosu 5 – Hipoglisemi Riski

**Beklenen sonuç:** “Kan şekeri düşük uyarısı”

* Hemoglobin (Hb): **14.0**
* WBC: **6.800**
* Trombosit (PLT): **230.000**
* Glukoz (Açlık): **58** 🔻
"""

kan_testi(14.2, 7500, 250000, 90)
print("===========================")
kan_testi(9.8, 6200, 280000, 85)
print("===========================")
kan_testi(13.5, 15300, 300000, 92)
print("===========================")
kan_testi(16.8, 8100, 520000, 95)
print("===========================")
kan_testi(14.0, 6800, 230000, 58)
