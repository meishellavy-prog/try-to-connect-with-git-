# day 8 tanggal 29 Juli 2026 
# pengenalan penggunaan string dan operator string
# 1. operator penjumlahan (+) untuk menggabungkan string
a = "belajar"
b = "python"
c = a + " " + b
print ("======OPERATOR 'PENJUMLAHAN'========")
print ('nilai a =', a)
print ('nilai b =', b)
print ('-----------------------------+')
print ('nilai c =', c)

# 2. operator perkalian (*) untuk mengulang string
d = "belajar"
e = d * 3
print ("======OPERATOR 'PERKALIAN'========")
print ('nilai d =', d)
print ('-----------------------------*')
print ('nilai e =', e)

# 3. operator keanggotaan (in) untuk mengecek apakah string terdapat dalam string lain
f = "belajar"
g = "belajar python"
h = f in g
print ("======OPERATOR 'KEANGGOTAAN'========")
print ('nilai f =', f)
print ('nilai g =', g)
print ('-----------------------------in')
print ('nilai h =', h)

# 4. operator identitas (is) untuk mengecek apakah dua string adalah objek yang sama
i = "belajar"
j = "belajar"
k = i is j
print ("======OPERATOR 'IDENTITAS'========")
print ('nilai i =', i)
print ('nilai j =', j)
print ('-----------------------------is')
print ('nilai k =', k)

#5. cara membuat string ada 2 cara yaitu dengan menggunakan tanda kutip tunggal (') atau tanda kutip ganda (")
l = 'belajar'
m = "belajar"
n = l is m
print ("======CARA MEMBUAT STRING========")
print ('nilai l =', l)
print ('nilai m =', m)
print ('-----------------------------is')
print ('nilai n =', n) 

#6. menggunkan tanda \
#\ untuk mengetik tanda kutip tunggal (') dan tanda kutip ganda (") di dalam string
#contoh :
print ('misalnya saya ingin mengetik hari jumat, maka saya harus mengetik hari jum\'at')
#atau menggunakan tanda kutip berbeda 
print ("misalnya saya ingin mengetik hari jumat, maka saya harus mengetik hari jum'at")#jadi luarnya menggunakan tanda kutip " sedangkan yang didalamnya menggunakan ' atau sebaliknya 
#\t untuk melakukan tab antara satu kata ke kata yang lain 
print ("misalnya saya ketik mishel \t noer, mishel dan noer akan berjauhan")
#jika ada tanda \ di dalam string apabila mau di print kan maka kita double kan tandanya seperti ini \\
print ("contoh\\penggunaannya\\yaaa")
#\n untuk enter ke line baru 
print ("kalau mau enter ketik ini, \n gituuu")

#7. menggunakan raw atau string literal
#gunanya itu untuk nge print semua yang ada di dalam string meskipun berupa simbol seperti \,",',\t,\n, ini berguna kalau simbol yang digunakan banyak jadi mempercepat waktu
print (r"Apabila sudah ditambahkan huruf r lalu tanda petik, maka simbol apapun di dalam string ini akan akan tetap di print baik itu \n\t\\\:;'gitu yaaa ")

#8. multiline literal string 
#bisa digunakan seperti enter \n tapi menggunakan 3 kali double quote """
print ("""ini contoh ya,
Nama saya : Meishella
Umur saya : 19 tahun 
""")
#9. multiline literal string dan raw 
print (r"""
Bisa print multiline dan juga simbol simbol seperti ini: \\n\t\j
meishella/noer/alysia/19thn""")

#sesi 2 day 8 tanggal 29 Juli 2026 
#manipulasi string 
#1. menggabungkan string 
#contoh :
nama_awal = "Meishella"
nama_tengah = "Noer" 
nama_akhir = "Alysia"
Nama_saya = nama_awal + " " + nama_tengah + " " + nama_akhir
print ("Nama saya adalah :", Nama_saya)
#jika tidak menambahkan tanda petik kosong, nanti nama nya akan kegabung. 
#2. mengetahui panjang sebuah string 
#kita menggunakan len yaitu panjang, contohnya :
panjang_string_nama = len(Nama_saya)
print ("panjang string :", Nama_saya, "adalah :", str(panjang_string_nama))
#ini seperti yang dipelajari tadi 
#3. operator 'not in' kalau sebelumnya belajar beberapa operator string termasuk 'in', sekarang operator 
#not in, operator not in berguna untuk mengecek apakah suatu string atau suatu simbol dan bagian ada di dalam string yang kita maksud. 
elemen = "saya" 
tidak_ada = elemen not in Nama_saya 
print ("tidak ada elemen:", elemen, ",di dalam string:", Nama_saya, "apakah benar?:", str(tidak_ada))

#mengambil beberapa bagian dari string menggunakan index 
#notes : jika length di baca dari paling kiri dihitung mulai dari 1, maka index dihitung mulai dari 0
#mudah, hanya menggunakan kurung kotak [] 
print ("index ke-1:" + Nama_saya [1])
#jika kita tulis nya -1 maka akan dihitunng mundur dari huruf paling belakang
print ("index ke-(-1):" + Nama_saya [-1])
#jika ingin mengambil dari index ke x menuju index ke y maka :
print ("index ke-(0:8):"+ Nama_saya [0:9])#jadi kalo misalnya tulis indexnya x menuju y, y nya ditambah 1 
#jika kita mau ngambil beberapa index dengan jarak yang berpola, misalnya jaraknya 2, maka :
print ("index ke-(0,2,4,6,8,10):" + Nama_saya [0:10:2])
#jadi titik awal : titik akhir (gausah ditambah lagi) : jarak antar nilai yang mau di ambil 
#untuk mencari item yang paling kecil maupun paling besar bisa menggunakan 
print ("nilai yang paling kecil adalah ;", min(Nama_saya))
print ("nilai yang paling besar adalah ;", max(Nama_saya))
#nilainya bisa dihitung sesuai urutan alfabet 
#jika kita ingin mengetahui di posisi mana elemen itu berada, kita bisa menggunakan ASCII code. 
#dimana ascii akan menunjukkan elemen itu ada di nomor berapa, biasanya dalam suatu string,
#Nilai minimum yang tadi kita coba print adalah nilai ascii yang paling kecil
#sedangkan nilai maxikmum yang tadi kita coba print kan juga adalah elemen yang memiliki nilai ascii terbesar
#kita bisa menanyakan nomor ascii  suatu elemen maupun kita bisa mengecek nomor ascii ada untuk elemen apa
#misalnya jika kita ingin mencari tahu nomor ascii dari spasi " "
cari_ascii_spasi = ord(" ")
print ("ASCII dari spasi adalah :"+ str(cari_ascii_spasi))
#atau mencari tahu ascii nilai y 
cari_ascii_y = ord("y")
print ("ASCII dari nilai 'y' adalah :"+ str(cari_ascii_y))
#atau kita mencari tahu elemen atau character dari nomor ascii nya 
nomorascii = 122
print ("char dari nilai ASCII 90 adalah:" + chr(nomorascii))


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

#day 10 tanggal 31 Juli Contoh metode lain :

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

#isalpha() (untuk mengecek apakah semuanya huruf)
#isalnum() (untuk mengecek apakah ada huruf dan angka)
#isdecimal() (untuk mengecek apakah semuanya angka)
#isspace() (untuk mengecek adanya spasi, tab, maupun newline \n)
#istitle() (untuk mengecek masing masing kata diawali dengan huruf kapital)

#kita juga bisa cek apakah bagian dari suatu data dibagian depan dan akhirnya
data_me = "computer science".endswith("science")
print(data_me)
data_you = "computer science".startswith("science")
print(data_you)

#penggabungan list data join split 
data_pisah = ['computer','sciece']
data_gabungan = ' '.join(data_pisah)
print (data_gabungan)
#jadi kata ' ' itu adalah objek yang jadi penggabung dari list nya itu
#misalnya kita menggabungkan list itu menggunakan tanda koma ','
#maka hasilnya akan computer,science

