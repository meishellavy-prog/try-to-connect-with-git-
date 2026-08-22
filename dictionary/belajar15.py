#day 26 tanggal 18 agustus 2026 

#berbeda dengan data list, yang dimana jika kita ingin mengambil datanya maka kita membutuhkan index,
#data dictionary menggunakan simbol atau singkatan untuk mengambil datanya 
data_dict = {
    'nm':'mishel',
    'age':19 
}
print (data_dict)
print (data_dict['nm'])


#DAY 27 TANGGAL 19 AGUSTUS 2026 
#OPERASI DICTIONARY

# Dictionary menyimpan data dalam bentuk key dan value.
# key = nama kunci, value = isi data.
data_siswa = {
    'nama': 'Budi',
    'umur': 17,
    'kelas': 'XI IPA'
}

# 1. Menampilkan seluruh isi dictionary
print('\nIsi awal:', data_siswa)

# 2. Mengambil value berdasarkan key
print('Nama siswa:', data_siswa['nama'])
print('Umur siswa:', data_siswa['umur'])

# 3. Mengubah value
data_siswa['umur'] = 18
print('Umur setelah diubah:', data_siswa['umur'])

# 4. Menambah data baru
data_siswa['kota'] = 'Jakarta'
print('Setelah menambah kota:', data_siswa)

# 5. Menghapus data berdasarkan key
del data_siswa['kota']
print('Setelah menghapus kota:', data_siswa)

# 6. Mengambil value dengan get()
# get() lebih aman jika key belum tentu ada.
print('Hobi:', data_siswa.get('hobi'))

# 7. Melihat semua key
print('Semua key:', data_siswa.keys())

# 8. Melihat semua value
print('Semua value:', data_siswa.values())

# 9. Melihat key dan value sekaligus
print('Key dan value:')
for key, value in data_siswa.items():
    print(key, ':', value)

# 10. Mengecek apakah sebuah key ada
if 'nama' in data_siswa:
    print('Key nama ada di dictionary\n\n')
    
#day 28 tanggal 20 agustus 2026 
#for loop data dictionary 
data_guru = {
    'math' : 'Rina',
    'olga' : 'Agi'
    }

for guru in data_guru:
    print (guru)

keys = data_guru.keys()
print (keys)

for key in data_guru.keys():
    print (data_guru.get(key))

values = data_guru.values()
print (values)

for value in data_guru.values():
    print(value)

items = data_guru.items()
print(items)

for item in data_guru.items():
    print(item)


for key,value in data_guru.items():
    print (f"guru {key} adalah : {value}")

#nested dictionary day 29 21 agustus 2026
import datetime
mahasiswa_ui1 = {
    'nama' : 'Meishella',
    'nim' : '12000101',
    'tanggal lahir' : datetime.datetime(2007,5,19)
}


mahasiswa_ui2 = {
    'nama' : 'Lala',
    'nim' : '12000102',
    'tanggal lahir' : datetime.datetime(2006,5,10)
}

data_mahasiswa = {
    'MU1001' : mahasiswa_ui1,
    'MU1002' : mahasiswa_ui2
}

print (f"\n{'Nama':<10} {'NIM': <8} {'Tanggal Lahir'} ")
print ("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa 

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    LAHIR = data_mahasiswa[KEY]['tanggal lahir'].strftime("%x")

    print (f"{NAMA:<10} {NIM:<10} {LAHIR} ")

#day 30 tanggal 22 Agustus 2026 
#skip day karena sinyal ga mendukung untuk materi baru
