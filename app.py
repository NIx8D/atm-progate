import random
import datetime
import module as m
from customer import Customer

id = random.randint(0, 1000000)
atm = Customer(id)
Atm = True
while Atm:
    m.alert("Selamat Datang di ATM-Progate Apps\nID: "+str(id))
    pin = int(input("Masukkan Pin Anda: "))
    
    trial = 0

    Verify = True
    while Verify:
        if (pin != atm.checkPin()) and trial < 2:
            
            m.alert('Error Pin. kesempatan: '+str((1-trial))+'x')
            pin = int(input("Pin anda salah. Silahkan Masukkan Lagi: "))
            
            trial += 1
            
            if trial > 1:
                m.alert("Kesempatan Berakhir. Coba lagi.")
                exit() 
            
            if ((pin != atm.checkPin()) and (trial < 2)):
                # Verify = False
                continue
        Menu = True
        while Menu:
            m.cls()
            m.alert("Selamat Datang di ATM-Progate Apps\nID: "+str(id))
            print("ATM - Progate Bootcamp")
            print("---")
            print("1. Cek Saldo") #information saldo
            print("2. Debet") #Deposito
            print("3. Simpan ") #Withdrawal
            print("4. Ganti Pin") #change pin
            print("5. Keluar") #exit
            print("-----------------------")

            inpMenu = input("Masukkan Pilihan Anda : ")

            if inpMenu == '1':
                m.alert("Saldo Anda: Rp."+str(atm.checkBalance()))
                input("Press Enter to back main menu.")
                continue

            elif inpMenu == '2':

                m.alert("Wellcome to Deposito\n---\nSaldo Anda: Rp."+str(atm.checkBalance()))
                nominal = int(input("Masukkan Saldo Yang Akan Ditarik: "))
                verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n " + str(nominal) + " ")
                
                if verify_withdraw == "y":
                    m.alert("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
                    input("Press Enter.")

                if nominal <= atm.checkBalance():
                    atm.witdrawalBalance(nominal)
                    m.alert("Transaksi debet berhasil!\n---\nSaldo sisa sekarang: Rp. " + str(atm.checkBalance()) + "")
                    input("Press Enter to back main menu")
                    continue
                else:
                    m.alert("Saldo tidak cukup. Silahkan tambah nominal saldo !")
                    input("Press Enter to back main menu")
                    continue

            elif inpMenu == '3':

                m.alert("Wellcome to Widrawal\n---\nSaldo Anda: Rp."+str(atm.checkBalance()))
                nominal = float(input("Masukkan nominal saldo: "))
                verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " ")
                if verify_deposit == "y":
                    atm.depositBalance(nominal)
                    m.alert("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n" )
                    input("Press Enter to back main menu.")
                else:
                    m.alert("Saldo gagal di simpan.")
                    input("Press Enter to back main menu.")

            elif inpMenu == '4':
                changePin = True
                while changePin:

                    m.alert("Change Your Pin")
                    verify_pin = int(input("masukkan pin lama anda: "))

                    if verify_pin != int(atm.checkPin()):
                        m.alert("Change Your Pin\nError : Pin Salah. Silahkan Masukkan Ulang.")
                        input("Press Enter.")
                        continue
                    else:
                        updated_pin = int(input("Silakan masukkan pin baru: "))
                        verify_newpin = int(input("Masukkan Ulang pin baru: "))
                        
                        if verify_newpin == updated_pin:
                            atm.setNewPin(verify_newpin)
                            m.alert("pin baru anda sukses!")
                            input("Press Enter. back to Login.")
                            changePin = False
                            Menu = False
                            Verify = False
                            continue
                        else:
                            m.alert("Error: Verifikasi password baru gagal.")
                            input("Press Enter to back main menu.")
                            continue
                        
            elif inpMenu == '5':
                m.alert("Resi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini sebagai bukti transaksi anda.\n=============================================\nNo. Rekord  : "+ str(random.randint(100000, 1000000))+"\nTanggal     : "+ str(datetime.datetime.now())+"\nSaldo akhir : "+ str(atm.checkBalance())+"\n=============================================\nTerima kasih telah menggunakan ATM Progate!")
                exit()

            else:
                m.alert("Error. Maaf, menu tidak tersedia")
                input("Press Enter to back main menu")