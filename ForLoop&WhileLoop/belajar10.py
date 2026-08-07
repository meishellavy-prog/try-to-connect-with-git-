#day 15 tanggal 7 agustus 2026
"""for loop berguna untuk melakukan perulangan pada suatu data, 
gunanya untuk menghemat waktu dan tenaga. 
"""
print (20*"=","FOR LOOP DENGAN LIST",20*"=")
list_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#ini adalah list angka dari 1 sampai 10 secara manual.
for i in list_angka:#ini akan menampilkan list angka dari 1 sampai 10 yang tadi kita buat
    print (f"angka ke-{i} adalah {i}")

print("\n",20*"=","FOR LOOP DENGAN RANGE",20*"=")

for i in range(1, 11):#ini akan menampilkan list angka dari 1 sampai 10
    print(f"angka ke-{i} adalah {i}")#kenapa hanya sampai 10? karena range(1,11) itu definisinya
    #definisi dari range itu adalah range(start, stop) dimana start itu angka awal dan stop itu angka akhir, tapi stop itu tidak termasuk. jadi kalau mau sampai 10 harus ditulis 11.
    #kenapa tidak termasuk stop? karena range itu digunakan untuk membuat list angka, dan list itu dimulai dari 0. jadi kalau mau sampai 10 harus ditulis 11.
print ("\n",10*"=","AKHIR DARI MATERI FOR LOOP",10*"=","\n")

#while loop
#berguna untuk melakukan perulangan pada suatu data,
#namun while loop ini akan terus melakukan perulangan selama kondisi yang diberikan masih bernilai True. jadi jika kondisi yang diberikan bernilai False maka perulangan akan berhenti.
print (20*"=","WHILE LOOP",20*"=")
angka = 1
while angka <= 10:#ini akan menampilkan list angka dari 1 sampai 10
    print(f"angka ke-{angka} adalah {angka}")
    angka += 1#ini adalah increment, jadi setiap perulangan angka akan bertambah 1

print ("\n",10*"=","AKHIR DARI MATERI WHILE LOOP",10*"=","\n")

