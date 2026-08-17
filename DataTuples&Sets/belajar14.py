#day 25 tanggal 17 agustus 2026 
"""
- data List [10, 5, 2] Punya indeks, 
datanya bisa diambil lewat indeks, dan bisa
diubah harganya (di-edit).
- data Tuple (10, 5, 2) Punya indeks, 
datanya bisa diambil lewat indeks, 
tetapi tidak bisa diubah harganya (dikunci/permanen).
- data Set {10, 5, 2} Benar-benar tidak punya indeks. 
Kamu tidak akan bisa melakukan data_set[0] atau 
data_set.index(5) pada Set karena 
akan menghasilkan error (TypeError).
"""
data_list = [1,2,3,4,5,6,7,8,9,10]
print (data_list)

data_tuple = (1,2,3,4,5,6,7,8,9,10)
print (data_tuple)

data_set={10,5,2,1,3,4,7,6,8,9}
print (data_set)
