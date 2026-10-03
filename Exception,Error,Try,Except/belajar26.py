#day 62 tanggal 2 oktober 2026
#angka1 = int(input("Masukkan angka : "))
#hasil1 = 10/angka1
#print(f"hasil adalah : {hasil1}")
#program diatas akan error jika angka yang diinput adalah angka 0, karena dalam aturan
#pembagian, jika pembaginya adalah angka 0 maka hasilnya tidak terdefinisi 
#untuk mengatasi masalah ini maka kita menggunakan try except dimana apabila program try itu eror maka program akan menjalankan bagian except 
#try:
#    angka1 = int(input("Masukkan angka : "))
#    hasil1 = 10/angka1
#    print(f"hasil adalah : {hasil1}")
#except:
#    print("terjadi error, pembagi tidak boleh 0")

#day 63 tanggal 3 oktober 2026 
while True:
    try:
        angka2 = int(input("Masukkan angka : "))
        hasil2 = 10/angka2
        print (f"hasil adalah : {hasil2}")
        lanjut1 = input("Lanjut gak? (y/n) : ")
        if lanjut1 == "n":
            break
    except:
        print("terjadi error, pembagi tidak boleh 0")
        break

print ("program pertama selesai")

