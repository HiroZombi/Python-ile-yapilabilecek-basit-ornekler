import random
ogr_liste = ["Semih","Doğukan","Yiğit","Alper","Atahan","Erdil","Oğuz","Burak","Emirhan"]
okl_liste = ["BAU","IMKB","ATATURK","BORUSAN","AVCILAR","GALATASARAY","ISTANBUL","TRAKYA"]
random.shuffle(ogr_liste)
random.shuffle(okl_liste)

ogretmensay = len(ogr_liste)
okulsay = len(okl_liste)
print(ogr_liste)
for i in range(8):
    print(okl_liste[i], " ", ogr_liste[i])
fark = ogretmensay - okulsay
for x in range(okulsay+1,ogretmensay+1):
    print("Atanamayan öğrenciler listesi: ", ogr_liste[x-1])