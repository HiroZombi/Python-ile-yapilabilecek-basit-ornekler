kilo = float(input("Kilonuzu giriniz : "))
boy = float(input ("Boyunuzu giriniz : "))

ortalama = kilo / (boy * boy)

print("Ortalama : ", ortalama)
if(ortalama <=20):
    sonuc = "Zayıf"
if (ortalama >= 25 and ortalama < 30):
    sonuc = "Normal"
if (ortalama >= 30 and ortalama < 35):
    sonuc = "Hafif Şişman"
if (ortalama >= 35 and ortalama < 40):
    sonuc = "Şişman"
if (ortalama >= 45 and ortalama < 50):
    sonuc = "Sağlık Açısından Önemli"
if (ortalama >= 50 and ortalama < 55):
    sonuc = "Aşırı Şişman"
if (ortalama >= 55):
    sonuc = "Morbid"
print("Sonuç : ",sonuc)