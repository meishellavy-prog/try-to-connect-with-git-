print ("hellow")
# ini adalah kata pertama aku belajar python 
#comment ini aku buat di commit kedua
#commit kedua aku akan membuat matematika menggunakan variabel
d = 19 
m = 5
y = 2007
print ("tanggal lahir saya adalah", d, m, y)
#next belajar tipe data (data type)
data_integer = 8 #data integer adalah data bilangan bulat"
print ("data integer adalah : ", data_integer)
print ("bertipe :", type(data_integer))

#data float adalah data bilangan desimal

data_float = 8.5 #data float adalah data bilangan desimal"
print ("data float adalah : ", data_float)
print ("bertipe :", type(data_float))

#data_string = "i learn python" 

data_string = "i learn python" #data string adalah data teks"
print ("data string adalah : ", data_string)
print ("bertipe :", type(data_string))

#data_boolean = True #data boolean adalah data yang bernilai benar atau salah"
data_boolean = True #data boolean adalah data yang bernilai true atau false"
print ("data boolean adalah : ", data_boolean)
print ("bertipe :", type(data_boolean))

#data_list = ["apel", "jeruk", "mangga"] #data list adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung siku"
data_list = ["apel", "jeruk", "mangga"] #data list adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung siku"
print ("data list adalah : ", data_list)
print ("bertipe :", type(data_list))    

#data_tuple = ("apel", "jeruk", "mangga") #data tuple adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung biasa"
data_tuple = ("apel", "jeruk", "mangga") #data tuple adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung biasa"
print ("data tuple adalah : ", data_tuple)
print ("bertipe :", type(data_tuple))        

#data_set = {"apel", "jeruk", "mangga"} #data set adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung kurawal"
data_set = {"apel", "jeruk", "mangga"} #data set adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung kurawal"
print ("data set adalah : ", data_set)
print ("bertipe :", type(data_set))     

#data_dictionary = {"nama": "andi", "umur": 20, "alamat": "jakarta"} #data dictionary adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung kurawal dan setiap nilai memiliki pasangan key dan value"
data_dictionary = {"nama": "andi", "umur": 20, "alamat": "jakarta"} #data dictionary adalah data yang berisi beberapa nilai yang dipisahkan dengan koma dan dibungkus dengan tanda kurung kurawal dan setiap nilai memiliki pasangan key dan value"
print ("data dictionary adalah : ", data_dictionary)
print ("bertipe :", type(data_dictionary))  

##sekarang tanggal 22 Juli 2026 kita belajar mengubah tipe data
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

print ("belajar input data dari user")
#input data dari user menggunakan fungsi input()
nama = input("masukkan nama anda : ")
umur = input("masukkan umur anda : ")
print (".")
data = input("masukkan data : ")
angka = int(input("masukkan angka : "))
angka_desimal = float(input("masukkan angka desimal : "))
string = str(input("masukkan data string : "))
angka_bool = bool(int(input("masukkan data boolean : ")))
print ("nama anda adalah : ", nama)
print ("umur anda adalah : ", umur)
print ("angka yang anda masukkan adalah : ", angka)
print ("angka desimal yang anda masukkan adalah : ", angka_desimal) 
print ("data string yang anda masukkan adalah : ", string)
print ("data boolean yang anda masukkan adalah : ", angka_bool, "bertipe :", type(angka_bool))
#data boolean akan bernilai True jika nilai datanya adalah 1, 2, 3, 4, 5, 6, 7, 8, 9, dan seterusnya    
#jadi jika ingin memasukkan data boolean, kodenya harus diubah menjadi int terlebih dahulu, lalu diubah menjadi boolean 


                                                                