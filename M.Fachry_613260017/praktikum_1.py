kehadiran = int(input("Jumlah kehadiran (1-14):"))
nilai = int(input("Nilai ujian (0-100)"))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai ujian memuaskan")
    else:
        print("REMEDIAL - Nilai ujian kurang")
else:
    print("TIDAK LULUS - Kehadiran kurang dari 12")
