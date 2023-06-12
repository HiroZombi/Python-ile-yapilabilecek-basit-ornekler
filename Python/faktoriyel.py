sayi = int(input("Faktöriyeli alınacak sayı: "))
if(sayi==0):
    print("Faktöriyeli işlemi sonucu: 1")
elif(sayi>0):
    i = 1
    fakt = 1
    while(i<=sayi):
        fakt *= i
        i += 1
    print("Faktöriyel sonucu: ", fakt)