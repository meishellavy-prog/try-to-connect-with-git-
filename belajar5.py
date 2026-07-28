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
