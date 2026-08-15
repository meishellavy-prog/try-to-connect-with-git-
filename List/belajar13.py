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

#day 22 tanggal 14 agustus 2026 
#nested list 
"""
Pelajaran: Nested List (List Bersarang) di Python

Isi:
- Penjelasan singkat tentang nested list
- Cara mengakses elemen
- Contoh penggunaan `for` dan nested `for`
- Contoh list comprehension untuk nested list
- Latihan singkat beserta solusi
"""

def contoh_matrix():
    # Nested list sebagai matriks 2x3
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("Matrix:")
    for row in matrix:
        print(row)
    # Akses elemen (baris 2, kolom 3) -> indeks [1][2]
    print("Elemen baris 2 kolom 3:", matrix[1][2])


def iterasi_nested_for():
    matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    print("Iterasi nested for (per baris, per elemen):")
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            print(f"[{i}][{j}] = {value}")


def cetak_format_rapi(matrix):
    # Cetak matriks rapi
    for row in matrix:
        print("\t".join(str(x) for x in row))


def flatten_with_comprehension(matrix):
    # Mengubah nested list jadi list datar
    flat = [x for row in matrix for x in row]
    return flat


# --- Latihan dan solusi ---
def sum_all_elements(matrix):
    # Solusi: jumlahkan semua elemen
    total = 0
    for row in matrix:
        for x in row:
            total += x
    return total


def transpose(matrix):
    # Transpose matriks (baris jadi kolom)
    # Asumsi semua baris memiliki panjang yang sama
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    trans = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    return trans


def count_occurrences(matrix, target):
    # Hitung berapa kali target muncul
    count = 0
    for row in matrix:
        for x in row:
            if x == target:
                count += 1
    return count
#def ini menandakan untuk tidak di run dulu sebelum kode ini dipanggil 

def _demo_and_tests():
    print("--- Contoh sederhana ---")
    contoh_matrix()
    print()

    print("--- Iterasi contoh ---")
    iterasi_nested_for()
    print()

    m = [[1, 2, 3], [4, 5, 6]]
    print("Cetak rapi:")
    cetak_format_rapi(m)
    print("Flatten:", flatten_with_comprehension(m))
    print()

    # Tes latihan
    test_matrix = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
    print("Sum semua elemen (harus 27):", sum_all_elements(test_matrix))
    print("Transpose:")
    cetak_format_rapi(transpose(test_matrix))
    print("Count occurrences of 1 (harus 2):", count_occurrences(test_matrix, 1))


if __name__ == "__main__":
    _demo_and_tests() 
#nah baru ini di running

#day 23 tanggal 15 agustus 2026
#latihan list 

list_peserta = []

while True:
    print("="*10, "List Peserta", "="*10)
    Nama = input("Masukkan Nama\t:")
    umur = input("Masukkan Umur\t:")
    data_peserta =[Nama,umur]
    list_peserta.append(data_peserta)
    print ("="*10, "Data Peserta", "="*10)
    for index,data in enumerate(list_peserta):
        print (f"{index+1}\t|{data[0]}\t|{data[1]}\t|")

    print ("\n","="*10)
           
    last = input("Apakah dilanjut?(y/n)\t:")

    if last == "n":
        break

print ("done")

