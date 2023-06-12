# r okuma modu
# w yazma modu
# a sonuna ekleme
# r + hem okuma hem yazma
# f.seek(0) dosya başına konumlanmayı sağlar
# print(f.read()) tüm satırı okur
# print(f.readlines()) bir liste şeklinde sonuç döndürür

file = open("isimler.txt","r", encoding="utf-8")
for satir in file:
    print(satir)