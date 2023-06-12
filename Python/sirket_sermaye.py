sermaye = int(input("Sermaye giriniz: "))
i = 0
while i<20:
    i += 1
    sermaye = sermaye + (sermaye * 10 / 100)
    print(i,"Senede",int(sermaye))