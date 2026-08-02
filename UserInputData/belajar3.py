print ("====belajar input data dari user====")
#input data dari user menggunakan fungsi input
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
