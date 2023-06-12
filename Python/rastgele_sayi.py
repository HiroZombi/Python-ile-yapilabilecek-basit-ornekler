import random
# 0.0 ile 1 arasında üretir
print(random.random())
# 1 ve 9 arasında sayı üretir
print(random.randrange(1, 10))
# sonuç 0,1,2,3,4
for x in range(6):
    print(x)
# red apple red banana .... gidiyor sırayla
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
# iki sayı arasında
for x in range(1,4):
    print(x)
# üç parametreli döngü | 2den başlar 11e kadar gider ama 11 yazmaz
for x in range(2,11,3):
    print (x)