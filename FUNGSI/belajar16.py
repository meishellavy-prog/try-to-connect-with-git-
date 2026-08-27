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
