#day 19 tanggal 11 agustus 2026
#cara membuat list 
print("="*5+"data angka"+"="*5)
data_list = [1,2,3,4,5,6,7]
print (data_list)
print("="*5+"data string"+"="*5)
data_string = ("aku","suka","belajar")
print (data_string)
print("="*5+"data boolean"+"="*5)
data_boolean = [True,False,False,True]#huruf awalnya kapital
print (data_boolean)
print("="*5+"data campuran"+"="*5)
data_campuran = [1,True, 10, False,"bisa","dong"]
print(data_campuran)
print("="*5+"data range"+"="*5)
#list menggunakan range 
data_range = range(1,11)
print (data_range)
data_listrange = list(data_range)
print (data_listrange)
print("="*5+"data menggunakan for"+"="*5)
#list menggunakan for dan if 
data_pake_for = [i for i in range(1,11)]
print (data_pake_for)
data_pake_for = [i**2 for i in range(1,11)]
print (data_pake_for)
data_pake_for = [i**3 for i in range(1,11)]
print (data_pake_for)
data_pake_for_if = [i for i in range(1,11) if i%2 ==0]
print (data_pake_for_if)
data_pake_for_if = [i for i in range(1,11) if i%2]
print (data_pake_for_if)




