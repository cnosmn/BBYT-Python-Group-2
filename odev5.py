# Bir yılın artık yıl olup olmadığını kontrol etme

# input ile yıl verisini al tam sayı olarak
# artık yıl olma algoritmasını yaz 
# artık yıl mı degıl mı ekrana yaz

yil = int(input("bir yıl giriniz : "))

if yil % 4 == 0 :
    print("bu yıl artık yıldır")
else :
    print("bu yıl artık yıl değildir")


