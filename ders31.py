


# dosya içerisine yazı yazma 
with open("test.txt","w",encoding="utf-8") as dosya:
    dosya.write("Merhaba Bu yazı python ile eklendi!!")
    
with open("test.txt","r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("icerik: ",icerik)
    
with open("test.txt", "a",encoding="utf-8") as f:
    f.write("\nYeni satır eklendi")
    
with open("test.txt", "r",encoding="utf-8") as f:
    for satir in f:
        print(satir.strip())
        
            
import os

if os.path.exists("test.txt"):
    print("test dosyası var")
else:
    print("test dosyası yok")


# dosya türleri (çok fazla ...)
# txt , png ,json ,jpg , xml, pdf , xlsx , py ............

# json dosya formatı ile işlemler

import json 

veriler = [{"id":1,"ad":"can","rol":"doktor"},{"id":2,"ad":"ayşe","rol":"hemşire"}]

with open("hastane.json","w",encoding="utf-8") as dosya:
    json.dump(veriler,dosya,indent=4,ensure_ascii=False)
print("başarılı bir şekilde json veri eklendi")