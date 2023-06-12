ucret = 0
cocuksay = int (input("Çocuk sayısını giriniz: "))
if(cocuksay==1):
    yas = int(input("Yaşını giriniz: "))
    if(yas<6):
        ucret = 60
    elif(yas>=6):
        ucret = 40
elif(cocuksay>=2):
    yas1 = int(input("1. Çocuğun yaşı: "))
    if(yas1<6):
        ucret = 60
    elif(yas1>=6):
        ucret = 40
    yas2 = int(input("2. Çocuğun yaşı: "))
    if(yas1<6):
        ucret += 60
    elif(yas1>=6):
        ucret += 40
print("Alacağınız toplam ücret= ",ucret)