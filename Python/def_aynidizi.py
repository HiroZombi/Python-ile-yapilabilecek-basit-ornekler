def karsilastir(a,b):
    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==b[j]):
                c.append(a[i])
    return(c)
x = [1,2,3,4,5,6,7,8]
y = [1,2,3,9]
z = karsilastir(x,y)
print(z)