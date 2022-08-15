#Saldo menginput sendiri karena masih belajar dasar
ulang = "ya"
while( ulang == "ya"):
    print("==============================================")
    print("SELAMAT DATANG DI PROGRAM PEMBELIAN E-PULSA")
    print("==============================================")
    pin = input("Silahkan masukkan pin anda : ")
    saldo = input("Berapa sisa saldo e-Money anda : ")
    print("==============================================")
    if 25000 <= int(saldo) < 50000 and pin == "1111":
        print("=========SELAMAT DATANG MEMBER GOLD !=========")
        print("=Anda memiliki potongan pembelian sebesar 15%=")
        print("==============================================")
        number = str(input("Masukkan nomor tujuan pengisian : "))
        print ("1. 25000 \n2. 50000")
        print("==============================================")
        pulsa = int(input("Nominal pulsa yang ingin anda beli : "))
        if int(pulsa) == 25000:
            a = 25000 - 3750
            saldo_akhir1 = int(saldo) - a
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 15%")
            print("Total yang harus anda bayar adalah : ", a)
            print("Sisa saldo anda adalah : ", saldo, "-", a,"=", saldo_akhir1)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        elif int(pulsa) == 50000 :
            print("Saldo anda = ", saldo)
            print("Mohon maaf saldo anda tidak cukup")
            print("Silahkan memilih menu yang lain")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")       
        else:
            print("Mohon maaf, tolong masukkan nominal yang sesuai (25000/50000)")
            print("==============================================")
            
    elif int(saldo) >= 50000 and pin == "1111" :
        print("=========SELAMAT DATANG MEMBER GOLD !=========")
        print("=Anda memiliki potongan pembelian sebesar 15%=")
        print("==============================================")
        number = str(input("Masukkan nomor tujuan pengisian : "))
        print ("1. 25000 \n2. 50000")
        print("==============================================")
        pulsa = int(input("Nominal pulsa yang ingin anda beli : "))
        if int(pulsa) == 25000:
            a = 25000 - 3750
            saldo_akhir1 = int(saldo) - a
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 15%")
            print("Total yang harus anda bayar adalah : ", a)
            print("Sisa saldo anda adalah : ", saldo, "-", a,"=", saldo_akhir1)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        elif int(pulsa) == 50000 :
            b = 50000 - 7500
            saldo_akhir2 = int(saldo) - b
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 15%")
            print("Total yang harus anda bayar adalah : ", b)
            print("Sisa saldo anda adalah : ", saldo, "-", b,"=", saldo_akhir2)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        else:
            print("Mohon maaf, tolong masukkan nominal yang sesuai (25000/50000)")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
    elif 25000 <= int(saldo) < 50000 and pin == "2222":
        print("========SELAMAT DATANG MEMBER SILVER !========")
        print("=Anda memiliki potongan pembelian sebesar 10%=")
        print("==============================================")
        number = str(input("Masukkan nomor tujuan pengisian : "))
        print ("1. 25000 \n2. 50000")
        print("==============================================")
        pulsa = int(input("Nominal pulsa yang ingin anda beli : "))
        if int(pulsa) == 25000:
            a = 25000 - 3750
            saldo_akhir1 = int(saldo) - a
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 10%")
            print("Total yang harus anda bayar adalah : ", a)
            print("Sisa saldo anda adalah : ", saldo, "-", a,"=", saldo_akhir1)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        elif int(pulsa) == 50000 :
            print("Saldo anda = ", saldo)
            print("Mohon maaf saldo anda tidak cukup")
            print("Silahkan memilih menu yang lain")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")       
        else:
            print("Mohon maaf, tolong masukkan nominal yang sesuai (25000/50000)")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
    elif int(saldo) >= 50000 and pin == "2222" :
        print("========SELAMAT DATANG MEMBER SILVER !========")
        print("=Anda memiliki potongan pembelian sebesar 10%=")
        print("==============================================")
        number = str(input("Masukkan nomor tujuan pengisian : "))
        print ("1. 25000 \n2. 50000")
        print("==============================================")
        pulsa = int(input("Nominal pulsa yang ingin anda beli : "))
        if int(pulsa) == 25000:
            a = 25000 - 2500
            saldo_akhir1 = int(saldo) - a
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 10%")
            print("Total yang harus anda bayar adalah : ", a)
            print("Sisa saldo anda adalah : ", saldo, "-", a,"=", saldo_akhir1)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        elif int(pulsa) == 50000 :
            b = 50000 - 5000
            saldo_akhir2 = int(saldo) - b
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 10%")
            print("Total yang harus anda bayar adalah : ", b)
            print("Sisa saldo anda adalah : ", saldo, "-", b,"=", saldo_akhir2)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        else:
            print("Mohon maaf, tolong masukkan nominal yang sesuai (25000/50000)")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
    elif 25000 <= int(saldo) < 50000 and pin == "3333":
        print("========SELAMAT DATANG MEMBER PREMIUM!========")
        print("=Anda memiliki potongan pembelian sebesar 5% =")
        print("==============================================")
        number = str(input("Masukkan nomor tujuan pengisian : "))
        print ("1. 25000 \n2. 50000")
        print("==============================================")
        pulsa = int(input("Nominal pulsa yang ingin anda beli : "))
        if int(pulsa) == 25000:
            a = 25000 - 1250
            saldo_akhir1 = int(saldo) - a
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 5%")
            print("Total yang harus anda bayar adalah : ", a)
            print("Sisa saldo anda adalah : ", saldo, "-", a,"=", saldo_akhir1)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        elif int(pulsa) == 50000 :
            print("Saldo anda = ", saldo)
            print("Mohon maaf saldo anda tidak cukup")
            print("Silahkan memilih menu yang lain")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")       
        else:
            print("Mohon maaf, tolong masukkan nominal yang sesuai (25000/50000)")
            print("==============================================")
    elif int(saldo) >= 50000 and pin == "3333" :
        print("========SELAMAT DATANG MEMBER PREMIUM!========")
        print("=Anda memiliki potongan pembelian sebesar 5% =")
        print("==============================================")
        number = str(input("Masukkan nomor tujuan pengisian : "))
        print ("1. 25000 \n2. 50000")
        print("==============================================")
        pulsa = int(input("Nominal pulsa yang ingin anda beli : "))
        if int(pulsa) == 25000:
            a = 25000 - 1250
            saldo_akhir1 = int(saldo) - a
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 5%")
            print("Total yang harus anda bayar adalah : ", a)
            print("Sisa saldo anda adalah : ", saldo, "-", a,"=", saldo_akhir1)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        elif int(pulsa) == 50000 :
            b = 50000 - 2500
            saldo_akhir2 = int(saldo) - b
            print("Pengisian ke nomor", number, "Sukses")
            print("Anda mendapat potongan sebesar 5%")
            print("Total yang harus anda bayar adalah : ", b)
            print("Sisa saldo anda adalah : ", saldo, "-", b,"=", saldo_akhir2)
            print("==============================================")
            print("=========TERIMA KASIH TELAH BERBELANJA========")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
        else:
            print("Mohon maaf, tolong masukkan nominal yang sesuai (25000/50000)")
            print("==============================================")
            ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")
            
    else:
        print("Mohon maaf pin anda salah atau saldo anda tidak mencukupi")
        print("==============================================")
        ulang = input("Apakah anda ingin mengulang? (ya/tidak) : ")