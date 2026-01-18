
# email , şifre  alır
# çıkış -> True(giriş başarılı) , False(giriş başarısız)

kullanicilar = [
    {"email": "zeynep@gmail.com", "sifre": "123456"},
    {"email": "sude@gmail.com", "sifre": "123456"}
]

def login(email, sifre,kullanicilar):
    
    for i in kullanicilar :
        if i.get("email","email key i yok") == email and i.get("sifre","sifre key i yok") == sifre:
            return True
    return False

# email = input("email: ")
# sifre = input("şifre: ")
# giris_sonucu = login(email, sifre, kullanicilar)
# if giris_sonucu :
#     print("Giriş başarılı")
# else :
#     print("Giriş başarısız")


# register -> kayıt ol
#  parametre : email, sifre, sifre_tekrar
#  return : True(giriş başarılı) , False(giriş başarısız)

def register(email, sifre, sifre_tekrar):
    if sifre != sifre_tekrar:
        print("Şifreler eşleşmiyor.")
        return False

    if "@" not in email:
        print("Geçersiz email formatı.")
        return False

    for i in kullanicilar :
        if i.get("email","email key i yok") == email:
            print("Bu email zaten kullanılıyor.")
            return False
    
    yeni_kullanici = {"email": email , "sifre": sifre}
    kullanicilar.append(yeni_kullanici)
    return True

email = input("email: ")
sifre = input("şifre: ")
sifre_tekrar = input("şifre tekrar: ")
kayit_sonucu = register(email, sifre, sifre_tekrar)
if kayit_sonucu :
    print("Kayıt başarılı")
else :
    print("Kayıt başarısız")

print("kullanicilar : ", kullanicilar)


# Hatırlatma : 
# sozluk = {
#     "ad": "Zeynep",
#     "soyad": "Yılmaz"
# }

# print(sozluk.get("isim", "isim key i yok"))

# print("burası kod satırı")

# kullanıcı hesabını silme işlemi yapılacak
# parametre : email, sifre
# dönüş : True , False
# hesabını silmesi için giriş yapması lazım
# kullanıcılar listesinde o kullanıcı maili var mı var ise sil

