#nah fungsi yang kita buat di belajar20.py akan kita import

from belajar20 import tambah, pengurangan, perkalian, pembagian
input_pembuka = input("===Selamat datang di program kalkulator sederhana===\n\n")
input_operasi = input("masukkan operasi matematika yang ingin dilakukan (tambah, kurang, kali, bagi): ")
if input_operasi == "tambah":
    input_angka = input("masukkan angka yang ingin ditambahkan (pisahkan dengan spasi): ")
    angka_list = list(map(int, input_angka.split()))
    hasil = tambah(*angka_list)
    print(f"Hasil penjumlahan: {hasil}")
elif input_operasi == "kurang":
    input_angka = input("masukkan angka yang ingin dikurangkan (pisahkan dengan spasi): ")
    angka_list = list(map(int, input_angka.split()))
    hasil = pengurangan(*angka_list)
    print(f"Hasil pengurangan: {hasil}")
elif input_operasi == "kali":
    input_angka = input("masukkan angka yang ingin dikalikan (pisahkan dengan spasi): ")
    angka_list = list(map(int, input_angka.split()))
    hasil = perkalian(*angka_list)
    print(f"Hasil perkalian: {hasil}")
elif input_operasi == "bagi":
    input_angka = input("masukkan angka yang ingin dibagi (pisahkan dengan spasi): ")
    angka_list = list(map(int, input_angka.split()))
    hasil = pembagian(*angka_list)
    print(f"Hasil pembagian: {hasil}")
else:
    print("Operasi tidak valid. Silakan pilih dari: tambah, kurang, kali, bagi.")

