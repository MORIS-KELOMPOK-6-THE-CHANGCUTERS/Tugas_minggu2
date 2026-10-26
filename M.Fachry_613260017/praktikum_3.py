print("==PROGRAM HITUNG DERERT ARITKMATIKA==")

awal = int(input("Masukan Suku pertama (a): "))
beda = int(input("Masukan Beda Deret (b): "))

banyak = int(input("Masukan Banyak Suku (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dari 0!")
    banyak = int(input("Silahkan masukan banyak suku (n): "))

suku = awal
total = 0

print("Barisan Deret:", end=" ")
for i in range(banyak):
    print(suku, end=" ")
    total += suku
    suku += beda

print(f"Total dari {banyak} suku pertama adalah: {total}")