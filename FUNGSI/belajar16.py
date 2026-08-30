#fungsi 
#day 34 tanggal 27 Agustus 2026 
def fungsi():
    '''ini adalah fungsi, kode ini baru bekerja ketika kita memanggilnya'''
    print ("ini fungsi ya")

fungsi()
#ini aku panggil fungsinya

#fungsi dengan argument 
barang = {
    'Nama' : 'Namabarang',
    'harga': 10000,
    'stok' : 12
}
barang_ = {}
while True:
    barangkey = dict.fromkeys(barang.keys())
    barangkey['Nama']= input("masukkan nama barang: ")
    barangkey['harga']= int(input("Masukkan harga: "))
    barangkey['stok']= int(input("masukkan sisa stok: "))
    barang_.update({barangkey['Nama']: barangkey})
  


    apakah = input("apakah mau lanjutin ngedata?(y/n) :")
    print (apakah)
    if apakah == 'n' :
        break 

def data_warung(namabarang):
    print ("====STOK====")
    for i in namabarang:
        KEY = i
        NAMA = namabarang[KEY]['Nama']
        HARGA = namabarang[KEY]['harga']
        STOK = namabarang[KEY]['stok']
        print (f"""
1. NAMA = {NAMA}
2. HARGA = {HARGA}
3. STOK = {STOK} """)
data_warung(barang_)


#day 35 tanggal 28 agustus 2026 
#fungsi dan return 
#operasi matematika 

def operasi_matematika(angka_1, angka_2):
    return angka_1 + angka_2 

y = operasi_matematika(7,3)
print (y)

def operasi_2 (angka_3, angka_4):
    tambah = angka_3 + angka_4 
    kurang = angka_3 - angka_4 
    bagi = angka_3 /angka_4 
    kali = angka_3 * angka_4 
    return tambah, kurang, bagi, kali 

k,l,m,n = operasi_2(10,2)
z = y + (k+l+m+n)

print (f"""
bilangan y = {y}
bilangan k,l,m,n = {k,l,m,n}
hasil tambah (k) = {k} 
hasil kurang (l) = {l}
hasil bagi (m) = {m}
hasil kali (n)= {n}
hasil y + (k,l,m,n) = {z}
""")

#day 36 tanggal 29 agustus 2026 
#default argumen 
def aku_nama(nama = "kamu"):
    print (f"{nama}, iyaaa kamu cantikk bangettt!!")


aku_nama()
#skip day tanggal 30 agustus 2026 
#day 37 tanggal 31 agustus 2026 
#latihan fungsi 
#mencari keliling dan luas persegi panjang 
import os
def judul_program():
    os.system("clear")
    '''ini adalah judul program'''
    print (f'{"MENGHITUNG LUAS":^40}')
    print (f'{"DAN KELILING PERSEGI PANJANG":^40}')
    print (f'{"-"*40:^40}')

def input_user():
    '''input user'''
    panjang = int(input("Masukkan besar panjang :"))
    lebar = int(input("Masukkan besar lebar :"))
    return panjang,lebar

def hitung_luas(panjangs,lebars):
    '''menghitung luas'''
    return panjangs*lebars
   

def hitung_keliling(panjange,lebare):
    '''hitung keliling'''
    return 2*(panjange+lebare)
    
def display(message,value):
    '''displaynya '''
    print (f"hasil dari {message} adalah : {value}")

while True:
    judul_program()
    PANJANG,LEBAR = input_user()
    LUAS = hitung_luas(PANJANG,LEBAR)
    KELILING = hitung_keliling(PANJANG,LEBAR)
    display("luas",LUAS)
    display("keliling",KELILING)
    lanjutgak = input("masih mau lanjut?(y/n): ")
    if lanjutgak == "n" :
        break 
print("AKHIR PROGRAM, THANK YOU")