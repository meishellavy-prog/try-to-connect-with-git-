#Day 65 tanggal 5 Oktober 2026 
#persiapan 

import os
from unittest import case

while True:
    if __name__ == "__main__":
        sistem_operasi = os.name
        match sistem_operasi:
            case "posix" : print("\033[H\033[2J\033[3J", end="")
            case "nt" : os.system ("cls")

        print ("SELAMAT DATANG")
        print ("DATA PERPUSTAKAAN")
        print ("="*30)
        print ('''
        1. Read 
        2. Add Data
        3. Update Data
        4. Delete Data
        ''')
        pilihan = input("Masukkan Pilihan Anda : ")
        print("\n","="*30, "\n")
        match pilihan:
            case "1" : print("Read")
            case "2" : print("Add Data")
            case "3" : print("Update Data")
            case "4" : print("Delete Data")
        
        print("\n","="*30, "\n")
        lanjut_gak = input("Apakah masih mau lanjut?(y/n) :")
        if lanjut_gak == "n" or lanjut_gak == "N":
            break

print ("TERIMA KASIH SUDAH PERCAYA PADA PROGRAM KAMI")

        