x = open("1.txt","r", encoding="utf-8")
aliste = x.readlines()
y = open("2.txt","r", encoding="utf-8")
bliste = y.readlines()

sonuc = []
for s1 in aliste:
    for s2 in bliste:
        if(s1==s2):
            sonuc.append(s1)
file = open("3.txt", "w", encoding="utf-8")
file.writelines(sonuc)