print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukan Suku Pertama (a):"))
beda = int(input("Masukan Beda Deret (b): "))

banyak = int(input("Masukan Banyak Suku (n):"))
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

print(f"\ntotal jumlah seluruh derett={total}")