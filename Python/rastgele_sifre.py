import random

harfler = "abcdefghijklmnopqrstuvwxyz"
büyük = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sembol = "!@#$%^&*()?"
sayi = "01234567890"
sifre = 2
p =  "".join(random.sample(harfler,sifre))
b =  "".join(random.sample(büyük,sifre))
s =  "".join(random.sample(sembol,sifre))
k =  "".join(random.sample(sayi,sifre))
print (p+b+s+k)
