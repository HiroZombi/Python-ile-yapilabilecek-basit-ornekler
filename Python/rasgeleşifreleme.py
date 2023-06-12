import random
r="0123456789"
kh="abcdefghijklmnopqrstuwvxyz"
bh="ABCDEFGHIJKLMNOPQRSTUWVXYZ"
s="#+-/*&()=?_-!$"
kac_tane=int(input("Kaç Şifre Gerekiyor:"))
for x in range(kac_tane):
    kh1= random.randrange(0,len(kh))
    kh2= random.randrange(0,len(kh))
    bh1= random.randrange(0,len(bh))
    bh2= random.randrange(0,len(bh))
    r1= random.randrange(0,len(r))
    r2= random.randrange(0,len(r))
    s1= random.randrange(0,len(s))
    s2= random.randrange(0,len(s))
    print(kh[kh1]+kh[kh2]+bh[bh1]+bh[bh2]+r[r1]+r[r2]+s[s1]+s[s2])

