oyun = ["Taş","Kağıt","Makas"]
import random
tas = oyun[0]
kagit = oyun[1]
makas = oyun[2]
while True:
    oyuncu2 = random.choice(oyun)
    oyuncu1 = input("Taş, kağıt, makas : ")
    if(oyuncu1 == "Taş"):
        if(oyuncu2 == tas):
            input("Berabere")
        if(oyuncu2 == kagit):
            input("Kaybettin")
        if(oyuncu2 == makas):
            input("Kazandın")
    if(oyuncu1 == "Kağıt"):
        if(oyuncu2 == tas):
            input("Kazandın")
        if(oyuncu2 == kagit):
            input("Berabere")
        if(oyuncu2 == makas):
            input("Kaybettin")
    if(oyuncu1 == "Makas"):
        if(oyuncu2 == tas):
            input("Kaybettin")
        if(oyuncu2 == kagit):
            input("Kazandın")
        if(oyuncu2 == makas):
            input("Berabere")