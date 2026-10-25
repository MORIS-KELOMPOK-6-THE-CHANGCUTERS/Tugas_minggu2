def cek_prima():
    angka = int(input("Masukkan angka: "))
    is_prima = True

    if angka <2:
        is_prima = False
    else:
        for pembagi in range(2, int(angka ** 0.5) + 1):
            if angka % pembagi == 0:
                is_prima = False
                break

    if is_prima:
        print(f"{angka} adalah BILANGAN PRIMA")
    else:
        print(f"{angka} BUKAN bilangan prima")

cek_prima()