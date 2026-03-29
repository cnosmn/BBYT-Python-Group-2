
# nesneye yönelimli programlama (OOP)
# encapsulation
# inheritance
# polimorfizm
# abstraction


class KrediKarti: # sınıf ismi büyük harf ile başlar
    # constructor -> yapıcı fonksiyon
    def __init__(self,numara,isim,soyisim,cvc):
        self.__numara = numara # private
        self.isim = isim # public
        self.__soyisim = soyisim
        self.__cvc = cvc

    # pytonic yazım aslında pythona özel yazım şeklidir.
    # kodun karmaşıklığını azaltmak için yapılmıştır.
    # yazımı kolaylaştırır.

    def get_numara(self):
        return self.__numara

    @property
    def numara(self):
        return self.__numara
    
    @numara.setter
    def numara(self,yeni_numara):
        if len(yeni_numara) == 16:
            self.__numara = yeni_numara
            print("numara değiştirme başarılı")
        else:
            print("lütfen geçerli kart numarası gir (16 haneli)")
    
    @property
    def soyisim(self):
        return self.__soyisim
    
    @soyisim.setter
    def soyisim(self,yeni_soyisim):
        if len(yeni_soyisim) != 0 :
            print("soyisim değiştirme başarılı")
            self.__soyisim = yeni_soyisim
        else:
            print("lütfen soyismini boş bırakma")

    @property
    def cvc(self):
        return self.__cvc
    
    @cvc.setter
    def cvc(self,yeni_cvc):
        if len(yeni_cvc) == 3 :
            print("cvc değiştirme başarılı")
            self.__cvc = yeni_cvc
        else:
            print("lütfen geçerli bir cvc gir(3 karakter)")

    def kart_bilgileri_yaz(self):
        print("============== KART BİLGİLERİ ==============")
        print("Kartın üzerindeki isim soyisim : ",self.isim," ",self.__soyisim)
        print("Kart Numarası :",self.__numara)
        print("Kart CVC bilgisi : ",self.__cvc)
        print("==========================================")
    

kart1 = KrediKarti("1234123412341234","acik","atolye","198")

print("kart1.isim : ",kart1.isim)
kart1.isim = "-"
print("kart1.isim : ",kart1.isim)
print("kart1.numara : ",kart1.numara)
kart1.numara = "1234552342"
print(kart1.get_numara())

kart1.kart_bilgileri_yaz()

kart1.cvc = "123"
print("kart1.cvc : ",kart1.cvc)