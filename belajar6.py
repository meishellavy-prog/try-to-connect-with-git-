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
