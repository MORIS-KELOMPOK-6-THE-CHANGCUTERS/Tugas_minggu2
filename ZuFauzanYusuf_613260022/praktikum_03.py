print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("masukan suku pertama (a):"))
beda = int(input("masukan beda (b):"))

banyak = int(input("masukan banyak suku (n):"))
while banyak <= 0:
    print("Peringatan: banyak suku harus lebih dari 0")
    banyak = int(input("silahkan masukan ulang banyak suku (n):"))

suku = awal 
total = 0

print("\nbarisan deret:", end="")
for i in range(banyak):
        print(suku, end="")
        total += suku
        suku += beda

print(f"\ntotal jumlah seluruh deret={total}")
