# day 9 tanggal 30  Juli 2026 
print ("========OPERATOR DALAM BENTUK METHOD========")
#1. MENGHITUNG BANYAKNYA SUATU CHARACTER YANG MAU KITA HITUNG DARI SUATU DATA 
data1 = "Meishella Noer Alysia"
banyak_a = data1.count("a")
print ("banyaknya huruf a yang ada di data :" + data1 + "\nadalah:" + " " + str(banyak_a))
#jadi 'count' method akan menghitung banyaknya huruf 'a' di dalam data1 

#2. merubah case dari string 
#dengan method ini, huruf yang ada di suatu data string akan berubah sesuai method nya
#lower : merubah semua huruf jadi huruf kecil
#upper : merubah semua huruf jadi huruf besar 
#contoh :
data2 = "huruf kecil"
versi_huruf_besar = data2.upper()
print ("jadi ini huruf besar/kecil? :"+ versi_huruf_besar)

data3 = "HURUF BESAR"
versi_huruf_kecil = data3.lower()
print ("apakah ini huruf kapital? :"+ versi_huruf_kecil)

#Kita juga bisa mengecek suatu data apakah dia terdiri dari huruf kecil atau kapital 
apakah_kecil = data2.islower()
print ("hasilnya data2 :"+ data2 + "\napakah merupakan huruf kecil?" + str(apakah_kecil))
apakah_besar = data3.isupper()
print ("hasilnya data3 :"+ data3 + "\napakah merupakan huruf besar?" + str(apakah_besar))
#jika isinya tidak valid maka hasilnya akan false 

#Contoh metode lain :

#1) capitalize() <-- Membuat karakter pertama di string menjadi uppercase
tes_capitalize = "ayam goreng enak"
cek_hasil = tes_capitalize.capitalize()
print(cek_hasil)

tes_capitalize = "AYAM GORENG ENAK"
cek_hasil = tes_capitalize.capitalize()
print(cek_hasil)

#------> Hasil keduanya : Ayam goreng enak

#2) casefold() <-- sama dengan lower()
#bedanya, casefold() mengkonversi karakter tidak umum menjadi lowercase karakter umum
#Contoh  : 'ß' (german) = menjadi 'ss'

tes_casefold = "außen IS AN GERMAN WORD"
cek_hasil = tes_casefold.casefold()
print(cek_hasil)

#------> Hasil : aussen is an german word

#3) swapcase() <-- Uppercase jadi lowercase dan kebalikannya
tes_swapcase = "Ayam Goreng Suharti"
cek_hasil = tes_swapcase.swapcase()
print(cek_hasil)

#------> Hasil : aYAM gORENG sUHARTI

#4) expandtabs () <-- Mengatur lebar tab (\t)
tes_expandtabs = "Ayam\tGoreng\tSuharti"
cek_hasil = tes_expandtabs.expandtabs(10)
print(cek_hasil)

#------> Hasil : Ayam      Goreng    Suharti

