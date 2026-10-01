#day 31 tanggal 01 oktober 2026 
import os
print("Lokasi Terminal Kamu saat ini:", os.getcwd())
print("Lokasi File belajar25.py berada :", os.path.dirname(__file__))
folder_aktif = os.path.dirname(__file__)
jalur_file = os.path.join(folder_aktif, "eksternalfile.txt")
#cara membaca eksternal file menggunakan open dan with 
print ("="*5, "Membaca File Eksternal Menggunakan Open", "="*5)
file = open(jalur_file, mode="r")#mode r ini memiliki makna read atau membaca file eksternal 
print(file.read())#fungsi read ini berguna untuk membaca seluruh isi file eksternal
#print(file.readline())#berfungsi untuk membaca file eksternal per baris
print(f"Apakah file eksternal ini readable? {file.readable()}")
print(f"Apakah file eksternal ini writable? {file.writable()}")
#file diatas tidak writable karena kita menggunakan mode r atau read
#jika kita mau nge save, kita harus close file eksternalnya terlebih dahulu, jika tidak maka akan eror
print(f"Apakah file eksternal ini sudah di close? {file.closed}")
file.close()
print(f"Apakah file eksternal ini sudah di close? {file.closed}")

print ("/n","="*5, "Membaca File Eksternal Menggunakan With", "="*5)


with open(jalur_file, mode="r") as file:
    print(f"Apakah file eksternal ini readable? {file.readable()}")
    print(f"Apakah file eksternal ini writable? {file.writable()}")
    print(f"Apakah file eksternal ini sudah di close? {file.closed}")
    print(file.read())

    
print (f"Apakah file eksternal ini sudah di close? {file.closed}")
