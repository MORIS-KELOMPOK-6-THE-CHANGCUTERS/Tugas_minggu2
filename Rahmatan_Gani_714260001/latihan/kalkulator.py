import operasi3

while True:
    print("\n" + "=" * 45)
    print("           APLIKAIS KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi aritmatika dasar (+, -, *, /)")
    print("2. Cek sifat bilangan (ganjill/genap)")
    print("3. hitung deret aritmatika (for & akumulator)")
    print("4. cetak tabel perkalian matriks (nested loop)")
    print("5. Keluar")
    print("=" * 45)

    pilihan = input("pilih menu (1-5): ")


    if pilihan == "5":
        print("\nTerima kasih telah menggunakan kalkulator konsol. program selesai!")
        break


    elif pilihan == "1":
        op = input("pilih operasi (+, -, *, /)").upper()

        if op in ["+", "-", "*", "/"]:
            inp1 = input("masukkan angka pertama: ")
            inp2 = input("masukkan angka kedua: ")

            if inp1.isdigit() and inp2.isdigit():
                a = int(inp1)
                b = int(inp2)

                if op == "+":
                    hasil = operasi3.tambah(a, b)
                    print(f"Hasil {a} + {b} = {hasil}")

                elif op == "-":
                    hasil = operasi3.kurang(a, b)
                    print(f"Hasil {a} - {b} = {hasil}")

                elif op == "*":
                    hasil = operasi3.kali(a, b)
                    print(f"Hasil {a} * {b} = {hasil}")

                elif op == "/":
                    hasil = operasi3.bagi(a, b)
                    print(f"Hasil {a} / {b} = {hasil}")
            else:
                print("peringatan: masukkan wajib berupa bilangan bulat") 
        else:
            print("peringatan: pilihan operasi tidak valid:") 


#menu 2

    elif pilihan == "2":
        print("\n--- Cek ganjil / genap (modulus %) ---")
        inp_angka = input("masukkan angka bulat positif: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi3.cek_ganjil_genap(angka)
            print(f"Hasil: angka {angka} tergolong bilangan {status}")
        else:
            print("peringatan: masukan harus berupa angka murni!")

#menu 3
    elif pilihan == "3":
        print("\n--- hitung deret aritmatika ----")
        inp_a = input("suku pertama (a) :") 
        inp_b = input("beda deret (b) :") 
        inp_n = input("banyak suku (n) :") 

        if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            while n <= 0:
                print("peringatan: banyak suku (n) harus lebih dari 0")
                n = int(input("Masukkan ulang banyak suku (n): "))

            total_deret = operasi3.hitung_deret_aritmatika(a, b, n)
            print(f"total jumlah seluruh deret = {total_deret}")
        else:
            print("peringatan: seluruh masukan wajib berupa angka bulat!")


#menu 4

    elif pilihan == "4":
        print("\n--- Matrix Tabel perkalian 1-3 (nested loop)---")
        for baris in range(1, 4):
            for kolom in range(1, 4):
                print(f"{baris * kolom}\t", end="")
            print()

    else:
        print("pilihan tidak valid! silahkan masukkan opsi 1 sampai 5.")