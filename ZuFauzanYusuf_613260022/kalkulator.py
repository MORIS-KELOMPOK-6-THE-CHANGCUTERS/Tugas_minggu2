import operasi3


while True:
    print("\n" +"="* 45)
    print(" APLIKASI KALKULATOR KONSOL")
    print("="* 45)
    print("1 Operasi aritmatika dasar (+,-,*,/)")
    print("2 Cek bilangan ganjil/genap")
    print("3 Hitung deret aritmatika (For & Akumulator)")
    print("4 Cetak tabel perkalian matriks (Nested Loop)")
    print("5 Keluar")
    print("="* 45)

    pilihan = input("Pilih menu (1-5):")

    if pilihan == "5":
        print("\nTerima kasih telah menggunakan kalkulator konsol. Program selesai.")
        break

    elif pilihan == "1":
        print("\n---Sub-Menu operasi dasar---")
        print("A. Penjumalahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pembagian (/)")

        op =input("pilih operasi (A/B/C/D):")

        if op in["A","B","C","D",]:
            inp1=input("masukan angka pertama:")
            inp2=input("masukan angka kedua:")

            if inp1.isdigit()and inp2.isdigit():
                a=int(inp1)
                b=int(inp2)

                if op=="A":
                    hasil=operasi3.tambah(a,b)
                    print(f"hasil penjumlahan {a}+{b}={hasil}")
                elif op=="B":
                    hasil=operasi3.kurang(a,b)
                    print(f"hasil pengurangan {a}_{b}={hasil}")
                elif op=="C":
                    hasil=operasi3.kali(a,b)
                    print(f"hasil perkalian {a}*{b}={hasil}")
                elif op=="D":
                    hasil=operasi3.bag(a,b)
                    print(f"hasil pembagian {a}/{b}={hasil}")
                else:
                    print("Peringatan: Masukan wajib berupa bilangan bulat!")
            else:
                print("Peringatan: Pilihan operasi tidak valid!")

        elif pilihan == "2":
            print("\n---  Cek Ganjil/Genap (Modulus%) ---")
            inp_angka=input("Masukan angka bulat positif:")

            if inp_angka.isdigit():
                angka=int(inp_angka)
                status=operasi3.cek_ganjil_genap(angka)
                print(f"angka{angka}Tergolong bilangan{status}")
            else:
                print("Peringatan: Masukan harus berupa angka murni!")

        elif pilihan == "3":
            print("\n---Hitung Deret Aritmatika---")
            inp_a=input("Suku pertama (a):")
            inp_b=input("Beda deret (b):")
            inp_n=input("Banyak suku (n):")

            if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():
                a=int(inp_a)
                b=int(inp_b)
                n=int(inp_n)

                while n <= 0:
                    print("Peringatan: Banyak suku (n) harus lebih dari 0!")
                    n=int(input("Masukan ulang banyak suku (n):"))

                    total_deret=operasi3.hitung_deret_aritmatika(a, b, n)
                    print(f"Toatal jumlah seluruh deret = {total_deret}")
                else:
                    print("Peringatan: Seluruh masukan wajib berupa angka bulat!")

            elif pilihan == "4":
                print("\n--- Matriks tabel perkalian 1-3 (Nested Loop) ---")

                for baris in range(1, 4):

                    for kolom in range(1, 4):
                        print(f"{baris*kolom}\t", end=" ")
                        print()


                    else:
                        print("Pilihan tidak valid! Silahkan masukan opsi 1 sampai 5.")



            
                        





