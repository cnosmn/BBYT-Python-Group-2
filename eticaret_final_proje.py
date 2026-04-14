"""
==============================================================
  🛒 PyShop — Python OOP ile Küçük E-Ticaret Sistemi
==============================================================
  Kullanılan OOP Kavramları:
  ✅ Class & Object
  ✅ __init__, __str__, __repr__, __len__, __add__  (Magic Methods)
  ✅ Encapsulation  (private attribute + getter/setter)
  ✅ Inheritance    (Urun → Elektronik, Giyim, Gida)
  ✅ Polymorphism   (kargo_ucreti() her sınıfta farklı davranır)
  ✅ Abstraction    (ABC ile soyut temel sınıf)
  ✅ Composition    (Sepet → Urun nesnelerini içerir)
  ✅ Class Method & Static Method
  ✅ Property Decorator
==============================================================
"""

from abc import ABC, abstractmethod
from datetime import datetime


# ─────────────────────────────────────────────
#  SOYUT TEMEL SINIF  (Abstraction)
# ─────────────────────────────────────────────
class Urun(ABC):
    """Tüm ürünlerin türediği soyut temel sınıf."""

    toplam_urun_sayisi = 0  # Class attribute

    def __init__(self, urun_id: int, ad: str, fiyat: float, stok: int):
        self._urun_id = urun_id          # protected
        self._ad = ad                    # protected
        self.__fiyat = fiyat             # private  (Encapsulation)
        self._stok = stok
        self._kategori = "Genel"
        Urun.toplam_urun_sayisi += 1

    # ── Property: fiyat okuma ──
    @property
    def fiyat(self) -> float:
        return self.__fiyat

    # ── Property: fiyat yazma (setter) ──
    @fiyat.setter
    def fiyat(self, yeni_fiyat: float):
        if yeni_fiyat < 0:
            raise ValueError("Fiyat negatif olamaz!")
        self.__fiyat = yeni_fiyat

    @property
    def ad(self) -> str:
        return self._ad

    @property
    def stok(self) -> int:
        return self._stok

    @property
    def kategori(self) -> str:
        return self._kategori

    def stok_azalt(self, miktar: int = 1):
        if miktar > self._stok:
            raise ValueError(f"Yetersiz stok! Mevcut stok: {self._stok}")
        self._stok -= miktar

    # ── Soyut metot: alt sınıflar kendi kargo ücretini tanımlar (Polymorphism) ──
    @abstractmethod
    def kargo_ucreti(self) -> float:
        pass

    # ── Soyut metot: ürün özet bilgisi ──
    @abstractmethod
    def ozet(self) -> str:
        pass

    # ── Magic Methods ──
    def __str__(self) -> str:
        return (f"[{self._kategori}] {self._ad} "
                f"— {self.__fiyat:.2f} TL  (Stok: {self._stok})")

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(id={self._urun_id}, "
                f"ad='{self._ad}', fiyat={self.__fiyat})")

    def __eq__(self, other) -> bool:
        return self._urun_id == other._urun_id

    def __lt__(self, other) -> bool:
        return self.fiyat < other.fiyat

    # ── Static Method ──
    @staticmethod
    def fiyat_formati(fiyat: float) -> str:
        return f"{fiyat:,.2f} TL"

    # ── Class Method ──
    @classmethod
    def toplam_urun(cls) -> str:
        return f"Sistemde toplam {cls.toplam_urun_sayisi} ürün kaydı var."


# ─────────────────────────────────────────────
#  ALT SINIFLAR  (Inheritance + Polymorphism)
# ─────────────────────────────────────────────

class Elektronik(Urun):
    """Elektronik ürünler. Ağırlıklı kargo ücreti hesaplar."""

    def __init__(self, urun_id, ad, fiyat, stok, garanti_yil: int):
        super().__init__(urun_id, ad, fiyat, stok)
        self._kategori = "Elektronik"
        self.garanti_yil = garanti_yil

    def kargo_ucreti(self) -> float:
        # Elektronik ürünler sabit 29.90 TL kargo
        return 29.90

    def ozet(self) -> str:
        return (f"{self._ad} | Fiyat: {Urun.fiyat_formati(self.fiyat)} | "
                f"Garanti: {self.garanti_yil} yıl | Kargo: {self.kargo_ucreti()} TL")


class Giyim(Urun):
    """Giyim ürünleri. Ücretsiz kargo kampanyası vardır."""

    def __init__(self, urun_id, ad, fiyat, stok, beden: str):
        super().__init__(urun_id, ad, fiyat, stok)
        self._kategori = "Giyim"
        self.beden = beden

    def kargo_ucreti(self) -> float:
        # 500 TL üzeri ürünlerde ücretsiz kargo (Polymorphism farkı)
        return 0.0 if self.fiyat >= 500 else 19.90

    def ozet(self) -> str:
        kargo = "ÜCRETSİZ" if self.kargo_ucreti() == 0 else f"{self.kargo_ucreti()} TL"
        return (f"{self._ad} | Fiyat: {Urun.fiyat_formati(self.fiyat)} | "
                f"Beden: {self.beden} | Kargo: {kargo}")


class Gida(Urun):
    """Gıda ürünleri. Son kullanma tarihi takip edilir."""

    def __init__(self, urun_id, ad, fiyat, stok, son_kullanma: str):
        super().__init__(urun_id, ad, fiyat, stok)
        self._kategori = "Gıda"
        self.son_kullanma = son_kullanma  # "GG/AA/YYYY" formatı

    def kargo_ucreti(self) -> float:
        # Gıdalar soğutmalı kargo: 39.90 TL
        return 39.90

    def gunler_kaldi(self) -> int:
        tarih = datetime.strptime(self.son_kullanma, "%d/%m/%Y")
        fark = tarih - datetime.now()
        return fark.days

    def ozet(self) -> str:
        gun = self.gunler_kaldi()
        durum = f"{gun} gün kaldı" if gun > 0 else "⚠️ SÜRESİ GEÇMİŞ"
        return (f"{self._ad} | Fiyat: {Urun.fiyat_formati(self.fiyat)} | "
                f"SKT: {self.son_kullanma} ({durum}) | Kargo: {self.kargo_ucreti()} TL")


# ─────────────────────────────────────────────
#  MÜŞTERİ SINIFI  (Encapsulation)
# ─────────────────────────────────────────────

class Musteri:
    _id_sayaci = 1000

    def __init__(self, ad: str, email: str):
        self._musteri_id = Musteri._id_sayaci
        Musteri._id_sayaci += 1
        self._ad = ad
        self.__email = email          # private
        self._siparis_gecmisi = []

    @property
    def musteri_id(self):
        return self._musteri_id

    @property
    def ad(self):
        return self._ad

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, yeni_email: str):
        if "@" not in yeni_email:
            raise ValueError("Geçersiz e-posta adresi!")
        self.__email = yeni_email

    def siparis_ekle(self, siparis):
        self._siparis_gecmisi.append(siparis)

    def siparis_gecmisi(self):
        if not self._siparis_gecmisi:
            print(f"{self._ad} için henüz sipariş yok.")
            return
        print(f"\n{'─'*50}")
        print(f"  {self._ad} — Sipariş Geçmişi")
        print(f"{'─'*50}")
        for s in self._siparis_gecmisi:
            print(s)

    def __str__(self):
        return f"Müşteri #{self._musteri_id}: {self._ad} ({self.__email})"

    def __repr__(self):
        return f"Musteri(id={self._musteri_id}, ad='{self._ad}')"


# ─────────────────────────────────────────────
#  SEPET SINIFI  (Composition + Magic Methods)
# ─────────────────────────────────────────────

class Sepet:
    """Composition: Sepet, Urun nesnelerini içerir."""

    def __init__(self, musteri: Musteri):
        self._musteri = musteri
        self._urunler: list[tuple[Urun, int]] = []   # (urun, adet)

    def ekle(self, urun: Urun, adet: int = 1):
        if adet > urun.stok:
            raise ValueError(f"Stok yetersiz! '{urun.ad}' için max {urun.stok} adet eklenebilir.")
        # Aynı ürün zaten varsa adedi artır
        for i, (u, a) in enumerate(self._urunler):
            if u == urun:
                self._urunler[i] = (u, a + adet)
                print(f"✅ '{urun.ad}' adedi güncellendi: {a + adet}")
                return
        self._urunler.append((urun, adet))
        print(f"✅ '{urun.ad}' sepete eklendi (adet: {adet})")

    def cikar(self, urun: Urun):
        self._urunler = [(u, a) for u, a in self._urunler if u != urun]
        print(f"🗑️  '{urun.ad}' sepetten çıkarıldı.")

    def ara_toplam(self) -> float:
        return sum(u.fiyat * a for u, a in self._urunler)

    def kargo_toplam(self) -> float:
        # Her üründen bir kez kargo alınır (aynı üründen kaç adet olursa olsun)
        return sum(u.kargo_ucreti() for u, _ in self._urunler)

    def genel_toplam(self) -> float:
        return self.ara_toplam() + self.kargo_toplam()

    def sepeti_goster(self):
        if not self._urunler:
            print("Sepet boş.")
            return
        print(f"\n{'═'*55}")
        print(f"  🛒  {self._musteri.ad} — Sepet")
        print(f"{'═'*55}")
        for urun, adet in self._urunler:
            satirlik = urun.fiyat * adet
            print(f"  {urun.ad:<25} {adet} adet  x  "
                  f"{urun.fiyat:>8.2f} TL  =  {satirlik:>9.2f} TL")
        print(f"{'─'*55}")
        print(f"  {'Ara Toplam:':<40} {self.ara_toplam():>9.2f} TL")
        print(f"  {'Kargo:':<40} {self.kargo_toplam():>9.2f} TL")
        print(f"{'─'*55}")
        print(f"  {'GENEL TOPLAM:':<40} {self.genel_toplam():>9.2f} TL")
        print(f"{'═'*55}")

    # __add__ ile iki sepeti birleştirme (Magic Method)
    def __add__(self, diger):
        yeni = Sepet(self._musteri)
        yeni._urunler = self._urunler + diger._urunler
        return yeni

    def __len__(self) -> int:
        return sum(a for _, a in self._urunler)

    def __str__(self) -> str:
        return (f"Sepet ({self._musteri.ad}) — "
                f"{len(self)} ürün, Toplam: {self.genel_toplam():.2f} TL")

    def __bool__(self) -> bool:
        return len(self._urunler) > 0


# ─────────────────────────────────────────────
#  SİPARİŞ SINIFI
# ─────────────────────────────────────────────

class Siparis:
    _siparis_sayaci = 10000

    DURUMLAR = ["Hazırlanıyor", "Kargoya Verildi", "Teslim Edildi", "İptal Edildi"]

    def __init__(self, musteri: Musteri, sepet: Sepet):
        self._siparis_no = Siparis._siparis_sayaci
        Siparis._siparis_sayaci += 1
        self._musteri = musteri
        self._tarih = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._toplam = sepet.genel_toplam()
        self._urunler = list(sepet._urunler)
        self.__durum = "Hazırlanıyor"   # private

        # Stoktan düş
        for urun, adet in self._urunler:
            urun.stok_azalt(adet)

        musteri.siparis_ekle(self)
        print(f"\n🎉 Sipariş oluşturuldu! Sipariş No: #{self._siparis_no}")

    @property
    def durum(self):
        return self.__durum

    @durum.setter
    def durum(self, yeni_durum: str):
        if yeni_durum not in Siparis.DURUMLAR:
            raise ValueError(f"Geçersiz durum! Geçerli durumlar: {Siparis.DURUMLAR}")
        self.__durum = yeni_durum
        print(f"📦 Sipariş #{self._siparis_no} durumu: {yeni_durum}")

    def __str__(self):
        satirlar = [f"\n  Sipariş #{self._siparis_no} | {self._tarih} | {self.__durum}"]
        for urun, adet in self._urunler:
            satirlar.append(f"    • {urun.ad} x{adet}  —  {urun.fiyat * adet:.2f} TL")
        satirlar.append(f"    Toplam: {self._toplam:.2f} TL")
        return "\n".join(satirlar)


# ─────────────────────────────────────────────
#  DEMO — Sistemin çalışması
# ─────────────────────────────────────────────

def demo():
    print("\n" + "="*55)
    print("       🛒  PyShop E-Ticaret Sistemi  🛒")
    print("="*55)

    # ── Ürün oluşturma (Inheritance) ──
    print("\n📦 Ürünler oluşturuluyor...")
    laptop   = Elektronik(1, "Laptop Pro X500",      18_999.99, 15, garanti_yil=2)
    kulaklik = Elektronik(2, "Kablosuz Kulaklık",     1_249.00, 50, garanti_yil=1)
    tisort   = Giyim(3,      "Pamuk Tişört",            299.90, 100, beden="M")
    mont     = Giyim(4,      "Kışlık Mont",             799.00, 30,  beden="L")
    peynir   = Gida(5,       "Organik Beyaz Peynir",    149.90, 200, son_kullanma="31/12/2025")
    kahve    = Gida(6,       "Filtre Kahve 500g",        89.90, 150, son_kullanma="01/06/2026")

    # ── Ürün listesi (Polymorphism ile kargo ücreti) ──
    urunler = [laptop, kulaklik, tisort, mont, peynir, kahve]
    print("\n🏪 Ürün Kataloğu:")
    print("─" * 55)
    for u in urunler:
        print(f"  {u.ozet()}")     # Her sınıf kendi ozet() ve kargo_ucreti() metodunu çağırır

    # ── Magic method: sıralama ──
    print("\n💰 Fiyata Göre Sıralı Ürünler (ucuzdan pahalıya):")
    for u in sorted(urunler):
        print(f"  {u.ad:<30} {Urun.fiyat_formati(u.fiyat)}")

    # ── Class method ──
    print(f"\n📊 {Urun.toplam_urun()}")

    # ── Müşteri oluşturma ──
    print("\n👤 Müşteriler oluşturuluyor...")
    ali   = Musteri("Ali Yıldız",   "ali@pyshop.com")
    ayse  = Musteri("Ayşe Kaya",    "ayse@pyshop.com")
    print(f"  {ali}")
    print(f"  {ayse}")

    # ── Encapsulation testi ──
    print("\n🔒 Encapsulation testi:")
    try:
        laptop.fiyat = -100   # Hata fırlatmalı
    except ValueError as e:
        print(f"  Hata yakalandı: {e}")
    try:
        ali.email = "gecersiz-mail"
    except ValueError as e:
        print(f"  Hata yakalandı: {e}")

    # ── Sepet (Composition) ──
    print("\n🛒 Ali'nin sepeti hazırlanıyor...")
    sepet_ali = Sepet(ali)
    sepet_ali.ekle(laptop, 1)
    sepet_ali.ekle(kulaklik, 2)
    sepet_ali.ekle(tisort, 3)
    sepet_ali.sepeti_goster()

    # ── __len__ ve __bool__ ──
    print(f"\n  Sepetteki toplam ürün adedi: {len(sepet_ali)}")
    print(f"  Sepet dolu mu? {bool(sepet_ali)}")

    # ── Sipariş oluşturma ──
    print("\n📝 Sipariş oluşturuluyor...")
    siparis1 = Siparis(ali, sepet_ali)

    # ── Sipariş durumu güncelleme ──
    siparis1.durum = "Kargoya Verildi"
    siparis1.durum = "Teslim Edildi"

    # ── İkinci müşteri ──
    print("\n🛒 Ayşe'nin sepeti...")
    sepet_ayse = Sepet(ayse)
    sepet_ayse.ekle(mont, 1)
    sepet_ayse.ekle(kahve, 2)
    sepet_ayse.ekle(peynir, 1)
    sepet_ayse.sepeti_goster()
    siparis2 = Siparis(ayse, sepet_ayse)

    # ── __add__: iki sepeti birleştir ──
    print("\n➕ İki sepeti birleştirme (__add__):")
    yeni_sepet = Sepet(ali)
    yeni_sepet.ekle(kahve, 1)
    birlesik = sepet_ali + yeni_sepet
    print(f"  Birleşik sepet: {birlesik}")

    # ── Sipariş geçmişi ──
    ali.siparis_gecmisi()

    # ── Stok kontrolü ──
    print(f"\n📦 Kalan stoklar:")
    for u in urunler:
        print(f"  {u.ad:<30} stok: {u.stok}")

    print("\n" + "="*55)
    print("  Demo tamamlandı! 🎉")
    print("="*55 + "\n")


if __name__ == "__main__":
    demo()