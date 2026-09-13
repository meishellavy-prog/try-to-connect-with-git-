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
#dy 47 tanggal 11 september 2026 
#full materi , tidak ada codingan
#day 48 tanggal 12 september 2026
#local scope adalah area di mana variabel lokal dapat diakses. Variabel lokal didefinisikan di dalam fungsi dan hanya dapat diakses dari dalam fungsi tersebut. Variabel lokal tidak dapat diakses dari luar fungsi.
#contoh penggunaan local scope:
def my_function():
    y = 5  # variabel lokal
    print("Nilai y di dalam fungsi:", y)  # Output: 5
my_function()  # memanggil fungsi untuk menampilkan nilai variabel lokal        
#jika kita mencoba mengakses variabel lokal dari luar fungsi, akan terjadi error karena variabel tersebut tidak dapat diakses dari luar fungsi.

#namun,jika ingin mengubah local variable menjadi global variable, kita bisa menggunakan kata kunci global di dalam fungsi. Berikut contohnya:
def change_local_to_global():
    global z  # menggunakan kata kunci global untuk mengubah variabel lokal menjadi variabel global
    z = 15  # mengubah nilai variabel lokal menjadi variabel global
change_local_to_global()  # memanggil fungsi untuk mengubah variabel lokal menjadi variabel global
print("Nilai z setelah fungsi dipanggil:", z)  # Output: 15
