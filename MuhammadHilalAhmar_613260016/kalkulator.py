import operasi3 # Memanggil modul fungsi terpisah

while True:
    print("\n" + "=" * 45)
    print("        APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2.  Cek Sifat Bilangan (Ganjil / Genap)")
    print("3. Hitung Deret Arutmatika (For & Akumulator)")
    print("4. Cetak Tabel Perkalian Matriks (Nested Loop)")
    print("5. Keluarr")
    print("=" * 45)

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("\nTerima kasih telah menggunakan Kalkulator Konsol. Program selesai!")
        break

    elif pilihan == "1":
        print("\n--- Sub-Menu Operasi Dasar ---")
        print("A. Penjulahan  (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian   (*)")
        print("D. Pembagian   (/)")

        op = input("Pilih operasi (A/B/C/D): ").upper()

        if op in{"A", "B", "C", "D",}:
               inp1 = input("Masukan angka pertama :")
               inp2 = input("Masukan Angka kedua :")

               if inp1.isdigit() and inp2.isdigit():
                   a = int(inp1)
                   b = int(inp2)

               if op == "A":
                  hasil = operasi3.tambah(a, b)
                  print(f"Hasil {a} + {b} = {hasil} ")
               elif op == "B":
                  hasil = operasi3.kurang(a, b)
                  print(f"Hasil {a} - {b} = {hasil}")
               elif op == "C":
                  hasil = operasi3.kali(a, b)
                  print(f"Hasil {a} * {b} = {hasil}")
               elif op == "D":
                  hasil = operasi3.bagi(a, b)
                  print(f"Hasil {a} / {b} = {hasil}")
               else:
                  print("Peringatan: Masukan jawaban wajib berupa bilangan bulat!")
        else:
               print("Peringatan: Pilihan operasi tidak valid!")

    elif pilihan == "2":
           print("\n--- Cek Ganjil / Genap (Modulus %) ---")
           inp_angka = input( "Masukan angka bulat positif: ")

           if inp_angka.isdigit():
               angka = int(inp_angka)
               status = operasi3.cek_ganjil_genap(angka)
               print(f"Hasil: Angka {angka} tergolong bilangan {status}")
           else:
            print("Peringatan: Masukan harus berupa angka murni!")

    elif pilihan == "3":
       print("\n--- Hitung deret aritmatika ---")
       inp_a= input("Suku pertama (a):")
       inp_b= input("Suku deret   (b):")
       inp_n= input("Banyak suku  (n):")

       if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():

        while n <= 0:
          print("Peringatan Banyak suku (n) harus lebih dari 0!")
          n = int(input("Masukan ulang banyak suku (n):"))

          total_deret = operasi3.hitung_deret_artimatika(a, b, n,)
          print(f"Total jumlah seluruh deret = {total_deret}")
       else:
          print("Peringatan: seluruh masukan wajib berupa angka bulat!")

    elif pilihan == "4":
       print("\n--- Matriks tabel perkalian 1-3 (Nested Loop) ---")

       for baris in range(1, 4):
          
           for kolom in range(1, 4):
              print(f"{baris * kolom}\t", end="")
           print()

       else:
           print("Pilihan tidak valid! silahkan masukan opsi 1 sampai 5.")
           


 

          
          
              
              
           
               
               
       
        
    

        







        


    





