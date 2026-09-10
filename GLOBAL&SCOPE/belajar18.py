#day 46 tanggal 10 september 2026
#global scope adalah area di mana variabel global dapat diakses. Variabel global didefinisikan di luar fungsi dan dapat diakses dari mana saja dalam program. Namun, jika kita ingin mengubah nilai variabel global di dalam fungsi, kita perlu menggunakan kata kunci global.
#contoh penggunaan global scope:
x = 10  # variabel global
# fungsi untuk mengubah nilai variabel global
def change_global_variable():
    global x  # menggunakan kata kunci global untuk mengubah nilai variabel global
    x = 20  # mengubah nilai variabel global
print("Nilai x sebelum fungsi dipanggil:", x)  # Output: 10
change_global_variable()  # memanggil fungsi untuk mengubah nilai variabel global
print("Nilai x setelah fungsi dipanggil:", x)  # Output: 20 
