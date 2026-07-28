#---------0++++++++5--------8+++++++11---------
#belajar komparasi dan logika day 7 tanggal 28 Juli 2026 
print ("====belajar komparasi dan logika====")
#komparasi adalah perbandingan antara dua nilai atau lebih
#operator komparasi adalah sebagai berikut :
#1. operator sama dengan (==)
#2. operator tidak sama dengan (!=)
#3. operator lebih besar dari (>)
#4. operator lebih kecil dari (<)
#5. operator lebih besar dari atau sama dengan (>=)
#6. operator lebih kecil dari atau sama dengan (<=)
#operator logika adalah sebagai berikut :
#1. operator and (dan)
#2. operator or (atau)
#3. operator not (tidak)
print ("masukkan angka: \nlebih dari 0 \ndan kurang dari 5 \natau \nlebih dari 8 \ndan kurang dari 11")
komparasiAngka = int(input("masukkan angka : "))
lebihdari3AtauKurangdari5 = (komparasiAngka > 0) and (komparasiAngka < 5)
lebihdari8AtauKurangdari11 = (komparasiAngka > 8) and (komparasiAngka < 11)
print ("hasil dari komparasi lebih dari 0 dan kurang dari 5 adalah : ", lebihdari3AtauKurangdari5)
print ("hasil dari komparasi lebih dari 8 dan kurang dari 11 adalah : ", lebihdari8AtauKurangdari11)    

hasil = lebihdari3AtauKurangdari5 or lebihdari8AtauKurangdari11     
print ("hasil dari komparasi dan logika adalah : ", hasil)  

#operator bitwise, biner, dan binary
a = 7
b= 3
# bitwise OR (|)
c = a|b
print ("======OPERATOR 'OR'========")
print ('nilai a =', a, ', binary =', format(a, '08b'))
print ('nilai b =', b, ', binary =', format(b, '08b'))
print ('-----------------------------or')
print ('nilai c =', c, ', binary =', format(c, '08b'))

# bitwise AND (&)
d = a&b
print ("======OPERATOR 'AND'========")
print ('nilai a =', a, ', binary =', format(a, '08b'))
print ('nilai b =', b, ', binary =', format(b, '08b'))
print ('-----------------------------&')
print ('nilai d =', d, ', binary =', format(d, '08b'))

# bitwise XOR (^)
e = a^b
print ("======OPERATOR 'XOR'========")
print ('nilai a =', a, ', binary =', format(a, '08b'))
print ('nilai b =', b, ', binary =', format(b, '08b'))
print ('-----------------------------^')
print ('nilai e =', e, ', binary =', format(e, '08b'))

#bitwise NOT (~)
f = ~a
print ("======OPERATOR 'NOT'========")
print ('nilai a =', a, ', binary =', format(a, '08b'))
print ('-----------------------------~')
print ('nilai f =', f, ', binary =', format(f, '08b'))

#bitwise shift left (<<)
g = a<<2
print ("======OPERATOR 'SHIFT LEFT'========")
print ('nilai a =', a, ', binary =', format(a, '08b'))
print ('-----------------------------<<')
print ('nilai g =', g, ', binary =', format(g, '08b'))

#bitwise shift right (>>)
h = a>>2
print ("======OPERATOR 'SHIFT RIGHT'========")
print ('nilai a =', a, ', binary =', format(a, '08b'))
print ('----------------------------->>')
print ('nilai h =', h, ', binary =', format(h, '08b'))
#bitwise adalah operator yang digunakan untuk melakukan operasi pada level bit dari bilangan biner. Operator ini bekerja dengan membandingkan setiap bit dari dua bilangan biner dan menghasilkan bilangan biner baru berdasarkan aturan tertentu. Operator bitwise sering digunakan dalam pemrograman untuk manipulasi data, pengaturan flag, dan optimisasi kinerja.  
