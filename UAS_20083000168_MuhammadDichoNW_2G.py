import os
clear = lambda : os.system('cls')

import datetime
from time import process_time_ns
x = datetime.datetime.now()

ulang = "y"
while ulang=="y" or ulang=="Y":
    kodeGolongan = [1,2,3]
    gajiPokok = [2500000, 4500000, 6500000]
    tunjanganIstri = [0.01, 0.03, 0.05]
    kodeJK =[1,2]
    JK = ['Laki - Laki','Perempuan']
    kodeStsKwn =[1,2]
    StsKwn = ['Kawin','Belum Kawin']
    kodeStsAnk =[1,2]
    StsAnk = ['Punya','Belum Punya']
    iuranPensiun = 15500
    iuranOrganisasi = 3500

    clear
    print ("==============================================")
    print("{:^44}".format("SELAMAT DATANG"))
    print("{:^44}".format("PERHITUNGAN GAJI KARYAWAN CV.LOGOS"))
    print("{:^44}".format("TANGGAL = " + x.strftime("%x")))
    print ("==============================================")
    namaKaryawan = input("Masukan Nama = ")

    inp = 1
    while inp < 4:
        clear()
        print("==============================================")
        print("{:^44}".format("PILIHAN GOLONGAN"))
        print("==============================================")
        nmr = 1
        a = 0
        for kodeGol in kodeGolongan :
            print(str(nmr) + ". Golongan " + str(kodeGol))
            a = a + 1
            nmr = nmr + 1
        print("==============================================")
        golongan = int(input("Masukan Kode Golongan = "))
        clear()
        inp = golongan

        if inp <= len(kodeGolongan) :
            i = 0
            while i<len(kodeGolongan):
                if kodeGolongan[i] == inp:
                    ambilGaji = gajiPokok[i]
                i+=1
        else :
            break

        clear()
        print("==============================================")
        print("{:^44}".format("PILIHAN JENIS KELAMIN"))
        print("==============================================")
        a = 0
        for jenisKel in JK :
            kodeKel = kodeJK[a]
            print(str(kodeKel) + ". " + str(jenisKel))
            a = a + 1
        print("==============================================")
        jenisKelamin = int(input("Masukan Kode Jenis Kelamin = "))
        clear()
        inpJK = jenisKelamin

        if inpJK <= len(kodeJK) :
            i = 0
            while i<len(kodeJK):
                if kodeJK[i] == inpJK:
                    ambilJK = JK[i]
                i+=1
        else :
            break

        clear()
        print("==============================================")
        print("{:^44}".format("PILIHAN STATUS KAWIN"))
        print("==============================================")
        a = 0
        for jenisSK in StsKwn :
            kodeSK = kodeStsKwn[a]
            print(str(kodeSK) + ". " + str(jenisSK))
            a = a + 1
        print("==============================================")
        StatusKawin = int(input("Masukan Kode Status Kawin = "))
        clear()
        inpSK = StatusKawin

        if inpSK <= len(kodeStsKwn) :
            i = 0
            while i<len(kodeStsKwn):
                if kodeStsKwn[i] == inpSK:
                    ambilSK = StsKwn[i]
                i+=1
        else :
            break

        if ambilSK == 'Kawin' :
            clear()
            print("==============================================")
            print("{:^44}".format("PILIHAN STATUS ANAK"))
            print("==============================================")
            a = 0
            for jenisSA in StsAnk :
                kodeSA = kodeStsAnk[a]
                print(str(kodeSA) + ". " + str(jenisSA))
                a = a + 1
            print("==============================================")
            StatusAnak = int(input("Masukan Kode Status Anak = "))
            clear()
            inpSA = StatusAnak

            if inpSA <= len(kodeStsAnk) :
                i = 0
                while i<len(kodeStsAnk):
                    if kodeStsAnk[i] == inpSA:
                        ambilSA = StsAnk[i]
                    i+=1
            else :
                break

        #hitung tunjangan istri
        if ambilJK == 'Laki - Laki' and ambilSK == 'Kawin' :
            i = 0
            while i<len(kodeGolongan):
                if kodeGolongan[i] == inp:
                    ambilTunjanganIstri = tunjanganIstri[i]
                    totalTunjanganIstri = ambilGaji * ambilTunjanganIstri
                i+=1
        else :
            totalTunjanganIstri = 0

        #hitung tunjangan anak
        if ambilSK == 'Kawin' and ambilSA == 'Punya' :
            totalTunjanganAnak = ambilGaji * 0.02
        else :
            totalTunjanganAnak = 0
        
        #hitung gaji bruto
        gajiBruto = ambilGaji + totalTunjanganAnak + totalTunjanganIstri

        #hitung biaya jabatan
        biayaJabatan = gajiBruto * 0.0005

        #hitung gaji netto
        gajiNetto = gajiBruto - biayaJabatan - iuranPensiun - iuranOrganisasi

        clear()
        print("==============================================")
        print("{:^44}".format("SLIP GAJI"))
        print("{:^44}".format("KARYAWAN CV.LOGOS"))
        print("{:^44}".format("TANGGAL = " + x.strftime("%x")))
        print("==============================================")
        print("Nama                     " + namaKaryawan)
        print("Golongan                 " + str(golongan))
        print("jenis kelamin            " + ambilJK)
        print("Staus Kawin              " + ambilSK)
        print("Gaji Pokok               Rp " + format(ambilGaji,',.2f'))
        print("Tunjangan istri          Rp " + format(totalTunjanganIstri,',.2f'))
        print("Tunjangan Anak           Rp " + format(totalTunjanganAnak,',.2f'))
        print(">> Gaji bruto            Rp " + format(gajiBruto,',.2f'))
        print("==============================================")
        print("Biaya Jabatan            Rp " + format(biayaJabatan,',.2f'))
        print("Iuran Pensiun            Rp " + format(iuranPensiun,',.2f'))
        print("Iuran Organisasi         Rp " + format(iuranOrganisasi,',.2f'))
        print(">> Gaji Netto            Rp " + format(gajiNetto,',.2f'))

        print("")
        
        #cetak struk (ekstensi : .txt)
        f=open("SLIPGAJI"+ namaKaryawan.upper() +".txt","w+")
        f.write("==============================================\r")
        f.write("{:^44}".format("SLIP GAJI") + "\r")
        f.write("{:^44}".format("KARYAWAN CV.LOGOS") + "\r")
        f.write("{:^44}".format("TANGGAL = " + x.strftime("%x")) + "\r")
        f.write("==============================================\r")
        f.write("Nama                     " + namaKaryawan + "\r")
        f.write("Golongan                 " + str(golongan) + "\r")
        f.write("jenis kelamin            " + ambilJK + "\r")
        f.write("Staus Kawin              " + ambilSK + "\r")
        f.write("Gaji Pokok               Rp " + format(ambilGaji,',.2f') + "\r")
        f.write("Tunjangan istri          Rp " + format(totalTunjanganIstri,',.2f') + "\r")
        f.write("Tunjangan Anak           Rp " + format(totalTunjanganAnak,',.2f') + "\r")
        f.write(">> Gaji bruto            Rp " + format(gajiBruto,',.2f') + "\r")
        f.write("==============================================\r")
        f.write("Biaya Jabatan            Rp " + format(biayaJabatan,',.2f') + "\r")
        f.write("Iuran Pensiun            Rp " + format(iuranPensiun,',.2f') + "\r")
        f.write("Iuran Organisasi         Rp " + format(iuranOrganisasi,',.2f') + "\r")
        f.write(">> Gaji Netto            Rp " + format(gajiNetto,',.2f') + "\r")
        f.write("\r")
        f.write("{:^44}".format("- TETAP SEMANGAT & SEHAT SELALU -") + "\r")
        f.write("{:^44}".format("- TERIMA KASIH -") + "\r")

        ulang = input('Ulangi Cek Gaji? (y/t) : ')
        clear()
        break

    


    
    
            
        