import random

rastgele = random.randrange(1, 51)
while True:
    sayi = int(input("Bir sayı giriniz: "))
    if(sayi > rastgele):
        input("Küçük")
        continue
    if(sayi < rastgele):
        input("Büyük")
        continue
    else:
        input("Doğru bildiniz!")
    print(x)

