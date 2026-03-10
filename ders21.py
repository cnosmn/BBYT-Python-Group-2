
# 1- encapsulation -> tamamlandı
# 2- inheritence -> kalıtım

"""
bir class yapısı oluşturucaz 
en az iki tane olucak 
ve biri diğerinden kalıtım alıcak
yani kalıtım alan sınıf üst sınıfın özelliklerini 
ve metotlarını barındırıcam


"""

class Insan:

    # constructor -> yapıcı fonksiyon
    def __init__(self,name,surname,okul):
        self.__name = name
        self.__surname = surname
        self.__okul = okul
    
    def bilgileri_goster(self):
        print("isim : ",self.__name,"soyisim : ",self.__surname)
    

class Ogrenci(Insan):
    def __init__(self,name,surname,ogrenciNo,okul,sinif):
        super().__init__(name,surname,okul)
        self.__ogrenciNo = ogrenciNo
        self.__sinif = sinif


class OkulPersoneli(Insan):
    def __init__(self,name,surname,okul,mesai,gorev):
        super().__init__(name,surname,okul)
        self.__mesai = mesai
        self.__gorev = gorev


ogrenci1 = Ogrenci("osman","can","1234","acikatolye","5A")

ogrenci1.bilgileri_goster()