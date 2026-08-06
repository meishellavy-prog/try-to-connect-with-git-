#day 14 tanggal 6 agustus 2026
kalkulator sederhana
print(20*"=","SELAMAT DATANG DI KALKULATOR SEDERHANA",20*"=")
angka1 = float(input("masukkan angka pertama: "))
operator = input("masukkan operator (+, -, *, /): ")
angka2 = float(input("masukkan angka kedua: "))
if operator == "+":
    hasil = angka1 + angka2
    print("Hasil dari", angka1, "+", angka2, "adalah:", hasil)
elif operator == "-":
    hasil = angka1 - angka2
    print("Hasil dari", angka1, "-", angka2, "adalah:", hasil)
elif operator == "*":
    hasil = angka1 * angka2
    print("Hasil dari", angka1, "*", angka2, "adalah:", hasil)
elif operator == "/":
        hasil = angka1 / angka2
        print("Hasil dari", angka1, "/", angka2, "adalah:", hasil)
else:
    print("Operator tidak valid. Silakan gunakan +, -, *, atau /.")

