#day 19 tanggal 11 agustus 2026
#cara membuat list 
print("="*5+"data angka"+"="*5)
data_list = [1,2,3,4,5,6,7]
print (data_list)
print("="*5+"data string"+"="*5)
data_string = ("aku","suka","belajar")
print (data_string)
print("="*5+"data boolean"+"="*5)
data_boolean = [True,False,False,True]#huruf awalnya kapital
print (data_boolean)
print("="*5+"data campuran"+"="*5)
data_campuran = [1,True, 10, False,"bisa","dong"]
print(data_campuran)
print("="*5+"data range"+"="*5)
#list menggunakan range 
data_range = range(1,11)
print (data_range)
data_listrange = list(data_range)
print (data_listrange)
print("="*5+"data menggunakan for"+"="*5)
#list menggunakan for dan if 
data_pake_for = [i for i in range(1,11)]
print (data_pake_for)
data_pake_for = [i**2 for i in range(1,11)]
print (data_pake_for)
data_pake_for = [i**3 for i in range(1,11)]
print (data_pake_for)
data_pake_for_if = [i for i in range(1,11) if i%2 ==0]
print (data_pake_for_if)
data_pake_for_if = [i for i in range(1,11) if i%2]
print (data_pake_for_if)

#day 20 tanggal 12 agustus 
#manipulasi list
#index suatu list dihitung dari 0 
data_list = ["satu", "dua", "tiga"]
print("="*5 + " manipulasi list " + "="*5)
print("Awal:", data_list)

# menambahkan item
data_list.append("empat")
print("append:", data_list)

# menyisipkan item di indeks tertentu
data_list.insert(1, "setengah")
print("insert:", data_list)

# menggabungkan list lain
data_list.extend(["lima", "enam"])
print("extend:", data_list)

# menghapus item berdasarkan nilai
data_list.remove("setengah")
print("remove:", data_list)

# menghapus item berdasarkan indeks
dihapus = data_list.pop(2)
print("pop:", dihapus, data_list)

# mengganti nilai
data_list[0] = "satu ulang"
print("ganti:", data_list)

# mengambil indeks suatu nilai
idx = data_list.index("lima")
print("index 'lima':", idx)

# menghitung kemunculan nilai
jumlah = data_list.count("lima")
print("count 'lima':", jumlah)

# membalik urutan list
data_list.reverse()
print("reverse:", data_list)

# mengurutkan list jika datanya sama tipe
angka = [3, 1, 4, 2, 5]
angka.sort()
print("sort:", angka)

# membuat salinan list
salinan = data_list.copy()
print("copy:", salinan)

# slicing list
potong = data_list[1:4]
print("slice [1:4]:", potong)

# clear list
data_baru = ["a", "b", "c"]
data_baru.clear()
print("clear:", data_baru)

#day 21 tanggal 13 agustus 2026 
#copy list
list_a = ["aku", "saya", "gue"]
list_b = list_a
print (f"list a adalah: \n {list_a}")
print (f"list b adalah: \n {list_b}")
list_a[2] = "GW"
print (f"list a setelah dirubah: \n {list_a}")
print (f"list b setelah list a dirubah: \n {list_b}")
print (f"""jadi jika hanya menggunakan operasi list_a = list_b,
maka alamat dari data a dan data b sama, hanya berbeda nama saja
apabila kita ingin merubah salah satu bagian dari data, maka kedua data
akan ikut berubah
""")
#namun jika menggunakan operasi list_c = list_a.copy() maka akan menghasilkan 
#dua data yang sama dengan alamat yang berbeda sehingga bisa dirubah 
list_c = list_a.copy()
print (f"list a adalah : \n {list_a} \n list b adalah: \n {list_b} \n list_c adalah: \n {list_c}")
list_c[0] = "akuh"

print (f"list a adalah : \n {list_a} \n list b adalah: \n {list_b} \n list_c adalah: \n {list_c}")