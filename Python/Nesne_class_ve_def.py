class araba():
    def __init__(self ,yakıt_tipi='benzin',vites=4,renk='Beyaz'):
        self.yakit_tipi=yakıt_tipi
        self.vites=vites
        self.renk=renk

    def setVites(self,vites):
        self.vites=vites

    def getVites(self):
        return self.vites

    def setRenk(self,renk):
        self.renk=renk

    def getRenk(self):
        return  self.renk

    def getYakitTipi(self):
        return  self.yakit_tipi

    def setYakitTipi(self,yakit_tipi):
        self.yakit_tipi=yakit_tipi


araba1=araba('dizel',5,'kırmızı')
print("1-arabanın rengi:",araba1.getRenk())
print("1-arabanın vites sayısı:",araba1.getVites())
print("1-arabanın yakıt tipi",araba1.getYakitTipi())

araba2=araba()
print("2-arabanın rengi:",araba2.getRenk())
print("2-arabanın vites sayısı:",araba2.getVites())
print("2-arabanın yakıt tipi",araba2.getYakitTipi())