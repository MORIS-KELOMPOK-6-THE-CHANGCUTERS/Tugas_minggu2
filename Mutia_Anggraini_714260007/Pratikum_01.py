# ========================================
# Pratikum 1: NESTED IF (EVALUASI KELULUSAN)
# Simpan sebagai: Pratikum_01.py
# ========================================

kehadiran = int(input("jumlah kehadiran (1-14): "))
nilai = int(input("Nilai ujian (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("Lulus - Nilai Memuaskan")
    else:
        print("Remedial - Nilai Ujian kurang")
else:
    print("Tidak Lulus - Kehadiran kurang dari 12")