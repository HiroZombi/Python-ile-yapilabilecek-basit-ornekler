def bolunenler(a,b):
    for i in range(a,b):
        if(i%3==0):
            print(i)

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
bolunenler(sayi1,sayi2)