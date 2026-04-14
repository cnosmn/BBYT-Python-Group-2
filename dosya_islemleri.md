Python’da dosya işlemleri genelde `open()` fonksiyonu ile yapılır. Aşağıya en çok kullanılan senaryoları **net ve pratik örneklerle** bıraktım:

---

## 1. Dosyaya Yazma (Write - `w`)

```python
with open("dosya.txt", "w") as f:
    f.write("Merhaba Dünya\n")
    f.write("Python dosya işlemleri")
```

* `w` → dosya yoksa oluşturur, varsa **sıfırlar (overwrite)**

---

## 2. Dosyaya Ekleme (Append - `a`)

```python
with open("dosya.txt", "a") as f:
    f.write("\nYeni satır eklendi")
```

* `a` → dosyanın sonuna ekler, silmez

---

## 3. Dosya Okuma (Read - `r`)

```python
with open("dosya.txt", "r") as f:
    icerik = f.read()
    print(icerik)
```

---

## 4. Satır Satır Okuma

```python
with open("dosya.txt", "r") as f:
    for satir in f:
        print(satir.strip())
```

---

## 5. `readline()` ve `readlines()`

```python
with open("dosya.txt", "r") as f:
    print(f.readline())   # ilk satır
    print(f.readlines())  # tüm satırlar liste olarak
```

---

## 6. Dosya Var mı Kontrol

```python
import os

if os.path.exists("dosya.txt"):
    print("Dosya var")
else:
    print("Dosya yok")
```

---

## 7. Dosya Silme

```python
import os

os.remove("dosya.txt")
```

---

## 8. JSON Dosyası Yazma / Okuma

```python
import json

veri = {"ad": "Osman", "yas": 25}

# yazma
with open("data.json", "w") as f:
    json.dump(veri, f)

# okuma
with open("data.json", "r") as f:
    data = json.load(f)
    print(data["ad"])
```

---

## 9. CSV Dosyası Yazma / Okuma

```python
import csv

# yazma
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Ad", "Yaş"])
    writer.writerow(["Osman", 25])

# okuma
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## 10. Binary Dosya (örneğin resim kopyalama)

```python
with open("resim.jpg", "rb") as f:
    data = f.read()

with open("kopya.jpg", "wb") as f:
    f.write(data)
```

---

## Kritik Notlar

* `with open(...)` kullan → dosya otomatik kapanır (**best practice**)
* Modlar:

  * `r` → okuma
  * `w` → yazma (silerek)
  * `a` → ekleme
  * `b` → binary
* Encoding problemi için:

```python
open("dosya.txt", "r", encoding="utf-8")
```

---

İstersen sana **mini proje (ör: log sistemi, öğrenci kayıt dosyası, basit CRM dosya yapısı)** da yazabilirim 👍
