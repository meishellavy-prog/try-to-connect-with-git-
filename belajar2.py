## tanggal 22 Juli 2026 (day 4)
#jika ingin mengubah tipe data, kita set dulu nilai datanya 
# ke dalam variabel, 
# lalu kita ubah tipe datanya menggunakan fungsi bawaan python
print ("TYPE CASTING (PERUBAHAN TIPE DATA DARI SATU TIPE KE TIPE LAIN)")
print (".")
print ("contoh mengubah tipe data integer ke tipe data lain")
data_int = 9
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print ("data integer : ", data_int, "bertipe :", type(data_int))
print ("data float : ", data_float, "bertipe :", type(data_float))
print ("data string : ", data_str, "bertipe :", type(data_str))
print ("data boolean : ", data_bool, "bertipe :", type(data_bool))
#jika diubah ke data float maka nilai 9 akan menjadi 9.0
#jika diubah ke data string maka nilai 9 akan menjadi "9"
#jika diubah ke data boolean maka nilai 9 akan menjadi True
print (".")
print ("contoh mengubah tipe data float ke tipe data lain")
data_float = 9.5
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print ("data float : ", data_float, "bertipe :", type(data_float))
print ("data integer : ", data_int, "bertipe :", type(data_int))
print ("data string : ", data_str, "bertipe :", type(data_str))
print ("data boolean : ", data_bool, "bertipe :", type(data_bool))
#jika diubah ke data integer maka nilai 9.5 akan menjadi 9
#tidak dibulatkan ke atas, melainkan dibulatkan ke bawah
#jika diubah ke data string maka nilai 9.5 akan menjadi "9.5"
#jika diubah ke data boolean maka nilai 9.5 akan menjadi True
#perubahan-perubahan tipe data ini disebut sebagai type casting
#boolean akan bernilai False jika nilai datanya adalah 0, 0.0, "", [], {}, (), None

