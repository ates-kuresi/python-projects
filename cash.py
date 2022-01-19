def islem_sec():
    print(f"{hesap['bakiye']}")
    i = int(input("islemi seciniz: \npara yatir(1)\n: "))
    if i == '1':
        para_yatir()
    if i == '2':
        pass
    if i == '3':
        para_cek()


def para_yatir(hesap):
    ekle = int(input("yatirmak istediginiz miktari giriniz: "))
    bakiye = int(ekle) + int(bakiye)
    print("Yeni bakiyeniz: ", bakiye)


def para_cek(hesap, cek):
    cek = int(input("cekmek istediginiz miktari giriniz: "))
    bakiye = int(bakiye) - int(ekle)
    print("Yeni bakiyeniz: ", bakiye)

hesap = {
    'ad' : 'Burak',
    'bakiye' : 100
}

print(f"Merhaba {hesap['ad']} Guncel bakiyeniz:  {hesap['bakiye']}")

islem_sec()
