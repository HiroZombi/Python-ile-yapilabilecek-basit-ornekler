a=float(input("Kargo ağırlığını(gram) giriniz: "))
if(a>=0.1 and a<=999):
    fiyat=15
elif(a>=1000 and a<=1999):
    fiyat=25
elif(a>=2000 and a<=2999):
    fiyat=35
elif(a>=3000):
    fiyat=45
print("Ödemeniz gereken", fiyat," TL'dir.")