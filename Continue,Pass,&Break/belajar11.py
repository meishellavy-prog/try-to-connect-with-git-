#day 16 tanggal 8 agustus 2026 
 #continue statement
#jika kita menggunakan continue statement, maka program akan melanjutkan ke iterasi berikutnya dan melewati kode yang ada di bawahnya dalam loop saat kondisi tertentu terpenuhi.
#contoh :
print ("contoh penggunaan continue statement")
nama = ["andi", "budi", "caca", "didi", "erik"]
for i in nama:
    if i == "caca":
        continue
    print(f"selamat {i}, kamu lulus ujian")


print ("\njika tidak menggunakan continue statement")
for i in nama:
    print(f"selamat {i}, kamu lulus ujian")
print ("\nCONTOH PENGGUNAAN PASS STATEMENT")
for i in nama:
    if i == "caca":
        pass
    print(f"selamat {i}, kamu lulus ujian")

#jadi pass statement digunakan untuk menandai bahwa kita sengaja tidak melakukan apa-apa pada kondisi tertentu, sedangkan continue statement digunakan untuk melewati iterasi saat kondisi tertentu terpenuhi.

print ("\nCONTOH PENGGUNAAN BREAK STATEMENT")
for i in nama:
    if i == "caca":
        break
    print(f"selamat {i}, kamu lulus ujian")
print ("loh jadi hanya ini yang lulus ujian?")

