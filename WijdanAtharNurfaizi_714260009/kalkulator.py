import operasi3

while True:
    print("\n" + "=" * 45)
    print(" APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. cek sifat bilangan (ganjil / genap)")
    print("3. hitung deret aritmatika (for & akumulator)")
    print("4. cek tabel perkalian matriks (nested loop)")
    print("5. keluar")
    print("=" * 45)

    pilihan = input("pilih menu (1-5): ")

    if pilihan == "5":
        print("\nterima kasih telah menggunakan kalkulator konsol. program selesai!")
        break

    elif pilihan == "1":
        print("\n--- Sub-Menu operasi dasar ---")
        print("A. Penjumlahan (+)")
        print("B. Penguranagn (-)")
        print("A. Perkalian (*)")
        print("A. Pembagian (/)")

        op = input("Pilih operasi (A/B/C/D): ").upper()

        if op in ["A", "B", "C", "D"]:
            inp1 = input("Masukkan angka pertama : ")
            inp2 = input("Masukkan angka kedua   : ")

            if inp1.isdigit() and inp2.isdigit():
                a = int(inp1)
                b = int(inp2)

                if op == "A":
                    hasil = operasi3.tambah(a, b)
                    print(f"hasil {a} + {b} = {hasil}")
                elif op == "B":
                    hasil = operasi3.kurang(a, b)
                    print(f"hasil {a} - {b} = {hasil}")
                elif op == "C":
                    hasil = operasi3.kali(a, b)
                    print(f"hasil {a} * {b} = {hasil}")
                elif op == "D":
                    hasil = operasi3.bagi(a, b)
                    print(f"hasil {a} / {b} = {hasil}")

            else:
                print("Peringatan: masukkan wajib berupa bilangan bulat!")
        else:
            print("Peringatan: pilihan operasi tidak valid!")

    elif pilihan == "2":
        print("\n--- cek ganjil / genap (modulus %) ---")
        inp_angka = input("masukkan angka bulat positif: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi3.cek_ganjil_genap(angka)
            print(f"hasil: angka {angka} tergolong bilangan {status}")
        else:
            print("peringatan: masukkan harus berupa angka murni!")

    elif pilihan == "3":
        print("\n--- hitung deret aritmatika ---")
        inp_a = input("suku pertama (a)  : ")
        inp_b = input("suku pertama (b)  : ")
        inp_n = input("suku pertama (n)  : ")  

        if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            while n <= 0:
                print("peringatan: banyak suku (n) harus lebih dari 0!")
                n = int(input("masukkan ulang banyak suku (n): "))

            total_deret = operasi3.hitung_deret_aritmatika(a, b, n)
            print(f"total jumlah seluruh deret = {total_deret}")

        else:
            print("peringatan: seluruh masukan wajib berupa angka bulat!")

    elif pilihan == "4":
        print("\n--- matriks tabel perkalian 1-3 (nested loop) ---")

        for baris in range(1, 4):

            for kolom in range(1, 4):
                print(f"{baris * kolom}\t", end="")
            print()

    else:
        print("piliha tidak valid! silahkan masukkan opsi 1 sampai 5.")                                                        