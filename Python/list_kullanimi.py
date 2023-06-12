# listede elemanlar 0dan başlar
thislist = ["van","muş","elazığ","konya","izmir","istanbul"]
# sadece elazığ yazar
print(thislist[2])
# en sondakini alır
print(thislist[-1])
# elazığ ve konya yazdırır (list) 4ü almaz 2den başlar..
print(thislist[2:4])
# sondan gelir
print(thislist[-4:-2])
# hepsini getirir ve 5inciyi değiştirir
thislist[4] = "ordu"
print(thislist[0:6])
# tüm listeyi alalım
print(thislist[0:6]) # tamamını yazdırır
print(thislist[:]) # tamamını yazdırır
print(len(thislist)) # uzunluğunu verir
# list yapısının sonuna eleman ekler
thislist.append("istanbul")
print(thislist[:])
#list yapımıza insert ile araya ekler
thislist.inser(3,"mardin")
print(thislist[:])
# listeden 4. indisli elemanı kaldıralım
thislist.pop(4)
print(thislist[:])
# list yapımızı tersine çevirelim
thislist.reverse()
print(thislist[:])
# list yapımızı sıralayalım
thislist.sort()
print(thislist[:])
# list yapısından ismini vererek eleman kaldırmak için
thislist.remove("istanbul")
print(thislist[:])
# arama gibi belli şeyi bulur
indeks = thislist.index(("izmir"))
print(indeks)