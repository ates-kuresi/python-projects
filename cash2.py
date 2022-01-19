BurakHesap = {
    'ad' : 'Burak',
    'bakiye' : 100,
    'ekHesap' : 200
}


def karsilama():
    print(f"Merhaba {BurakHesap['ad']}, Bakiyeniz: {BurakHesap['bakiye']}")
    q = input('yapmak istediginiz islem girin; \nhesap sorgu = 1 \npara cek = 2\npara yatir = 3\n :')
    if q == '1':
        print(f"{BurakHesap['ad']} adli kisinin bakiyesi {BurakHesap['bakiye']} ek hesabinin bakiyesi {BurakHesap['ekHesap']}")
    elif q == '2':
        para_cek()
    elif q =='3':
        para_yatir()


def para_cek():
    print('para cek')
    pass


def para_yatir():
    print('para cek')
    pass


karsilama()
