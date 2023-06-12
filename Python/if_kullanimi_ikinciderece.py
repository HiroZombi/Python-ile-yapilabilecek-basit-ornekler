# ax^2 +bx+c denkleminde kökleri bulunuz.
# a,b,c katsayıları klavyeden girilecektir.
# delta= b^2 -4ac
# delta küçük sıfır ise reel kökü yoktur.
# delta eşit sıfır ise kökler eşittir.
# delta büyük sıfır ise iki kök vardır.
# delta büyük eşit sıfır ise X1 = -b - kök(delta) / 2a
# X2 = -b + kök(delta) / 2a
import math
a = int(input("a giriniz: "))
b = int(input("b giriniz: "))
c = int(input("c giriniz: "))
delta = b**2 - 4*a*c
if(delta<0):
    print("Reel kökü yoktur, çözüm kümesi boş kümedir")
elif(delta==0 or delta>0):
    if(delta==0):
        print("Kökler eşit")
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print("x1= ", x1, "x2= ", x2)