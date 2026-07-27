print ("====Operasi Matematika====")
#day 5 tanggal 24 juli 2026 
a = 4
b = 6
c = 9
hasil = a + b * c // a ** b % a 
print ("hasil dari", a, "+", b, "*", c, "//", a, "**", b, "%", a, "adalah :", hasil)
#urutan operasi matematika adalah sebagai berikut :
#1. operasi pangkat (**)
#2. operasi perkalian (*) dan pembagian (/) dan pembagian bulat atau floor division (//) dan sisa bagi atau modulus (%)
#3. operasi penjumlahan (+) dan pengurangan (-)

#tanggal 25 Juli 2026 day 6 
print ("====Konversi satuan temperatur====")
#konversi satuan temperatur dari celcius ke fahrenheit, kelvin, reamur, dan rankine
celcius = float(input("masukkan suhu dalam celcius : "))
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15
reamur = celcius * 4/5
rankine = (celcius + 273.15) * 9/5
print ("suhu dalam celcius : ", celcius, "°C")
print ("suhu dalam fahrenheit : ", fahrenheit, "°F")
print ("suhu dalam kelvin : ", kelvin, "K")
print ("suhu dalam reamur : ", reamur, "°R")
print ("suhu dalam rankine : ", rankine, "°Ra")
#konversi satuan temperatur dari fahrenheit ke celcius, kelvin, reamur, dan rankine  
fahrenheit = float(input("masukkan suhu dalam fahrenheit : "))
celcius = (fahrenheit - 32) * 5/9
kelvin = celcius + 273.15
reamur = (fahrenheit - 32) * 4/9
rankine = (celcius + 273.15) * 9/5
print ("suhu dalam fahrenheit : ", fahrenheit, "°F")
print ("suhu dalam celcius : ", celcius, "°C")
print ("suhu dalam kelvin : ", kelvin, "K")
print ("suhu dalam reamur : ", reamur, "°R")
print ("suhu dalam rankine : ", rankine, "°Ra")

#konversi satuan temperatur dari kelvin ke celcius, fahrenheit, reamur, dan rankine
kelvin = float(input("masukkan suhu dalam kelvin : "))
celcius = kelvin - 273.15
fahrenheit = (celcius * 9/5) + 32
reamur = (kelvin - 273.15) * 4/5
rankine = (celcius + 273.15) * 9/5
print ("suhu dalam kelvin : ", kelvin, "K")
print ("suhu dalam celcius : ", celcius, "°C")
print ("suhu dalam fahrenheit : ", fahrenheit, "°F")
print ("suhu dalam reamur : ", reamur, "°R")
print ("suhu dalam rankine : ", rankine, "°Ra")

#satuan farenheit tidak bisa dikonversi ke satuan rankine, karena satuan rankine adalah satuan yang digunakan untuk mengukur suhu dalam skala absolut, sedangkan satuan fahrenheit adalah satuan yang digunakan untuk mengukur suhu dalam skala relatif.
#satuan farenheit tidak bisa secara langsung dikonversi ke satuan kelvin dan r