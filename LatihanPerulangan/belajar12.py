#membuat perulangan menggunakan for loop 
variabel = "O"
print ("membuat segitiga siku-siku menggunakan perulangan for")
for i in range(20):
    print(variabel)
    variabel += "O"

print ("akhir dari program")
#jika memakai while 

print ("membuat segitiga siku-siku menggunakan perulangan while")
#jika ingin panjang jumlah char yang ada di variabel kedua selalu ganjil maka
kedua = "A"
jumlah = int(1) 
while True:
    if jumlah%2:
        hasil = kedua*jumlah
        print (hasil)
        jumlah +=1
    else:
        jumlah +=1
        continue
    if jumlah>20:
        break
print ("akhir dari program 2")

#jika ingin membuat segitiga sama kaki 
print ("segitiga sama kaki")
spasi = 10
angka = 1
ketiga= "W"
while True:
    if angka%2:
        print (" "*spasi,ketiga*angka)
        spasi -= 1
        angka += 1
    else:
        angka += 1
        continue 
    if angka > 20:
        break

print ("akhir dari program 3")

#jika ingin membuat ketupat 
print ("belah ketupat")
spasieh = 10
angkaeh = 1
keempat = "|"
while True:
    if angkaeh%2:
        print (" "*spasieh,keempat*angkaeh)
        spasieh -= 1
        angkaeh += 1
    else:
        angkaeh += 1
        continue
    if angkaeh > 20:
        break
angkaih = 19
spasiih = 1
kelima ="|"
while True:
    if angkaih%2:
        print (" "*spasiih, kelima*angkaih)
        spasiih += 1
        angkaih -= 1
    else :
        angkaih -= 1
        continue
    if angkaih < 1:
        break

#jika menggunakan for (lebih efektif)
n = 10
for i in range(1,(n+1)):
    print (" "*(n-i),"|"*(2*i-1))
for i in range ((n-1),0,-1):
    print (" "*(i-(i-(n-i))), "|"*(2*i-1))
