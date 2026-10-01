#day 60 tanggal 30 september 2026 
print (f"hasil dari __name__ adalah '{__name__}'")

import file2
print (f"hasil dari __name__ pada file2 adalah '{file2.__name__}'")

def deklarasi_fungsi(a:int, b:int)->int:
    return a+b

if __name__ == "__main__":
    angka1 = 10
    angka2 = 20
    hasil = deklarasi_fungsi(angka1,angka2)
    print (f"hasil dari penjumlahan {angka1} + {angka2} = {hasil}")
else:
    print ("file ini diimport dari file lain")
    