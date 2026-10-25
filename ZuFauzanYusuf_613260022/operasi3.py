def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b
    if b == 0:
       return "Error: Pembagian oleh nol tidak diperbolehkan"
    return a / b
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

def hitung_deret_aritmatika(awal, beda, n):
    suku = awal
    total = 0
    for i in range(n):
        total += suku
        suku += beda
    return total


    



