class kus():
    def __init__(self,kanat_uzunlugu=50,kanat_varmı="yok",memelimi="evet"):
        self.kanat_uzunlugu=kanat_uzunlugu
        self.kanat_varmı=kanat_varmı
        self.memelimi=memelimi

    def setKanatuzunlugu(self,kanat_uzunlugu):
        self.kanat_uzunlugu=kanat_uzunlugu
    def getKanatuzunlugu(self):
        return self.kanat_uzunlugu

    def setKanatvarmı(self,kanat_varmı):
        self.kanat_varmı=kanat_varmı
    def getKanatvarmı(self):
        return self.kanat_varmı

    def setMemelimi(self,memelimi):
        self.memelimi=memelimi
    def getMemelimi(self):
        return self.memelimi

kus1=kus(60,"yok","hayır")
print("kanat uzunluğu:",kus1.getKanatuzunlugu())
print("kanat varmı:",kus1.getKanatvarmı())
print("memelimi?:",kus1.getMemelimi())