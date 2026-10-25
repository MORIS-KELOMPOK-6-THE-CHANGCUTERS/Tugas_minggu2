def cek_prima(angka):                                            
    # studi kasus: uji bilangan prima
    is_prima = True # Flag penanda

    if angka < 2:
        is_prima = False
    else:
        for i in range(2, int(angka ** 0.5) + 1):
            if angka % i == 0:
                is_prima = False 
                break            


    if is_prima:
                print(f"{angka} adalah BILANGAN PRIMA")
    else:
                print(f"{angka} BUKAN bilangan prima")   
input_user = int(input("masukkan angka: "))
cek_prima(input_user)

