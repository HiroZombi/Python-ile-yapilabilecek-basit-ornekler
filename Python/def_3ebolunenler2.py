def ucebolunen(a,b):
    list=[]
    for x in range(a,b):
        if(x%3==0):
            list.append(x)
    return(list)

basla=int(input("Aralık başlangıç: "))
bitis=int(input("Aralık bitiş: "))
sonucliste=[]
sonucliste=ucebolunen(basla,bitis)
print(sonucliste)