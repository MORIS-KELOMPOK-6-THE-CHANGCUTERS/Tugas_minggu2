print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan suku pertama (a): "))
beda = int(input("Masukkan beda deret (b): "))

banyak = int(input("Masukkan banyak suku (n): "))
while banyak <= 0:
    print("peringatan banyak suku harus lebih dari 0!")
    banyak = int(input("silahkan masukkan ulang banyak suku (n): "))

suku = awal
total = 0

print("Barisan_Deret: ", end="")
for i in range(banyak):
    print(suku, end="")
    total += suku
    suku += beda

print(f" total jumlah seluruh derett = {total}")
