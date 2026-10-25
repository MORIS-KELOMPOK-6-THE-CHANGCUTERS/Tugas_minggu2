for baris in range(1, 200):
    for kolom in range(1, 200):
        print(f"{baris}x{kolom}={baris*kolom}", end="\t")
    print()

niai_maba = [12, 32-35]
niai_maba.append(98)

print("Daftar Nilai :", niai_maba)
print("Nilai Tertinggi:", max(niai_maba))  