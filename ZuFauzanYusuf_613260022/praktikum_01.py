kehadiran = int(input("masukan kehadiran(0-14):"))
nilai = int(input("nilai ujian(0-100):"))

if kehadiran>=12:
    if nilai>=75:
        print("LULUS-Nilai memuaskan")
    else:
        print("REMEDIAL-Nilai ujian kurang")
else:
    print("TIDAK LULUS-kehadiran kurang dari 12")




