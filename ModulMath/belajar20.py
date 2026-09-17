#day 51 tanggal 18 september 2026
#kita buat modul matematika nanti kita import ke dalam file python kita
def tambah(*args): 
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

def pengurangan(*kurang):
    hasil = kurang[0]
    for angka in kurang[1:]:
        hasil -= angka
    return hasil

def perkalian(*kali):
    hasil = 1
    for angka in kali:
        hasil *= angka
    return hasil

def pembagian(*bagi):
    hasil = bagi[0]
    for angka in bagi[1:]:
        hasil /= angka
    return hasil 
