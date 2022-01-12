def islem_sec():
    i = int(input("islemi seciniz: \npara yatir(1)\n: "))
    if i == 1:
        para_yatir()
    if i == 2:
        pass

def para_yatir():
    ekle = int(input("yatirmak istediginiz miktari giriniz: "))
    bakiye += ekle
    print("Yeni bakiyeniz: ", bakiye)
    exit()

bakiye = 100
print("Bankaya hos geldiniz, bakiyeniz: ", bakiye)


islem_sec()