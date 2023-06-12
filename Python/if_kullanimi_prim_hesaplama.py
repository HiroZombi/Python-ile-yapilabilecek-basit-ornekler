# pazarlamacı olarak çalışanlara yaptıkları satışa göre
# prim verilmektedir. Pazarlamacı, ne kadar çok satış
# yaparsa o kadar prim kazanacaktır. Satışlara göre prim
# yüzdeleri şöyledir;
# 2.000 TL'den küçük satışlar için prim yok.
# 2.000 TL ile 5.000 TL arası
#  (2.000 dahil, 5.000 dahil değil) satışın %5'si prim,
# 5.000 TL ile 7.000 TL arası
#  (5.000 dahil, 7.000 dahil değil) satışın %10'u prim,
# 7.000 TL ve üstü %15 prim kazanmaktadır.
# Girilen satışa göre pazarlamacının ne kadar prim
# kazanacağını hesaplayan programı yazınız.

satis = float(input("satış fiyatını giriniz: "))
if(satis < 2000):
    prim = 0
    print("Prim yok.")
elif(satis >= 2000 and satis < 5000):
    prim = satis * 5 / 100 # veya 0.05 ile çarpabiliriz.
elif(satis >= 5000 and satis < 7000):
    prim = satis * 10 / 100
elif(satis >= 7000):
    prim = satis * 15 / 100

if(prim>0): print(prim, " kadar prim kazandınız!")