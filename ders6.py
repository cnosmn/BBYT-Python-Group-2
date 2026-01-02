# Vücut kitle indeksi hesaplama ve değerlendirme


kilo = int(input("kilonuzu kg cinsinden giriniz : "))
boy = float(input("boyunuzu metre cinsinden giriniz : "))

vki = kilo / (boy ** 2)  

# - : 18.5  -> zayıf
# 18.5 - 24.9  -> normal
# 25 - 29.9  -> fazla kilolu
# 30 - 34.9  -> obez
# 35 ve üzeri  -> ileri derece obez

if vki < 18.5 :
    print("zayıfsınız")
elif vki >= 18.5 and vki <= 24.9 :
    print("sıradansınız")
elif vki >= 25 and vki <= 29.9 :
    print("poğaçasınız")
elif vki >= 30 and vki <= 34.9 :
    print("denizde batmazsınız")
else :
    print("sakın karaya vurmayın")

