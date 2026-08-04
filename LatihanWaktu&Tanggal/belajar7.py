#day 12 tanggal 4 Agustus 2026
#jika kita ingin menampilkan tanggal dan waktu saat ini, kita bisa menggunakan modul datetime di Python. Berikut adalah contoh kode untuk menampilkan tanggal dan waktu saat ini:
import datetime
Hari_ini = datetime.date.today()
print("Tanggal hari ini:", Hari_ini)
#jika ingin menggunakan waktu saat ini, kita bisa menggunakan fungsi datetime.datetime.now() untuk mendapatkan tanggal dan waktu saat ini. Berikut adalah contoh kode untuk menampilkan tanggal dan waktu saat ini:
import datetime
Waktu_hari_ini = datetime.datetime.now()
print("Waktu hari ini:", Waktu_hari_ini)
#jika ingin menampilkan hari, bulan, dan tahun saat ini secara terpisah, kita bisa menggunakan atribut year, month, dan day dari objek datetime. Berikut adalah contoh kode untuk menampilkan hari, bulan, dan tahun saat ini:
import datetime
Tanggal_hari_ini = datetime.date.today()
print("Hari:", Tanggal_hari_ini.day)
print("Bulan:", Tanggal_hari_ini.month)
print("Tahun:", Tanggal_hari_ini.year)
#jika ingin menampilkan hari dalam format string, kita bisa menggunakan metode strftime() dari objek datetime. Berikut adalah contoh kode untuk menampilkan hari dalam format string:   
import datetime
hari_ini = datetime.date.today()
hari_string = hari_ini.strftime("%A")
print("Hari dalam format string:", hari_string)
#kita juga bisa menggunakan user input untuk menampilkan tanggal dan waktu saat ini. Berikut adalah contoh kode untuk menampilkan tanggal dan waktu saat ini berdasarkan input pengguna:
import datetime
tanggal_input = input("Masukkan tanggal (YYYY-MM-DD): ")
try:
    tanggal = datetime.datetime.strptime(tanggal_input, "%Y-%m-%d").date()
    print("Tanggal yang dimasukkan:", tanggal)
except ValueError:
    print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD.")    
    