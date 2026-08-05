#day 13 tanggal 5 agustus 2026
#if else statement adalah salah satu struktur kontrol alur dalam pemrograman Python yang memungkinkan kita untuk membuat keputusan berdasarkan kondisi tertentu. Berikut adalah contoh kode yang menggunakan if else statement untuk menentukan apakah sebuah angka adalah bilangan genap atau ganjil:
angka = int(input("Masukkan sebuah angka: "))
if angka % 2 == 0:
    print(angka, "adalah bilangan genap.")
else:
    print(angka, "adalah bilangan ganjil.")
#jadi, jika kita memasukkan angka 4, maka outputnya akan menjadi "4 adalah bilangan genap." dan jika kita memasukkan angka 5, maka outputnya akan menjadi "5 adalah bilangan ganjil."
#tetapi operasi di atas masih terbatas pada bilangan bulat. Jika kita ingin memeriksa apakah sebuah angka adalah bilangan positif, negatif, atau nol, kita bisa menggunakan if else statement dengan beberapa kondisi. Berikut adalah contoh kode untuk menentukan apakah sebuah angka adalah positif, negatif, atau nol:
angka = float(input("Masukkan sebuah angka: "))
if angka > 0:
    print(angka, "adalah bilangan positif.")
elif angka < 0:
    print(angka, "adalah bilangan negatif.")
else:
    print(angka, "adalah nol.")
#if else maupun elif statement dapat digunakan untuk membuat keputusan yang lebih kompleks. Misalnya, kita bisa menggunakan if else statement untuk menentukan apakah sebuah angka adalah bilangan prima atau bukan. Berikut adalah contoh kode untuk menentukan apakah sebuah angka adalah bilangan prima:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#def ini sebagai fungsi untuk memeriksa apakah sebuah angka adalah bilangan prima. Fungsi ini akan mengembalikan True jika angka tersebut adalah bilangan prima, dan False jika tidak. Kita bisa menggunakan fungsi ini dalam if else statement untuk menentukan apakah sebuah angka adalah bilangan prima atau bukan:
angka = int(input("Masukkan sebuah angka: "))
if is_prime(angka):
    print(angka, "adalah bilangan prima.")
else:
    print(angka, "bukan bilangan prima.")
    