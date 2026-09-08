#day 43 tanggal 6 september 2026 
#bedanya lambda function dan regular function
#regular function
def regular_function(x):
    return x * 2

result_regular = regular_function(5)
print("Regular Function Result:", result_regular)
#jadi, regular function adalah fungsi biasa yang didefinisikan dengan kata kunci def, dan dapat memiliki nama, parameter, dan blok kode yang lebih kompleks.
#sedangkan lambda function adalah fungsi anonim yang didefinisikan dengan kata kunci lambda, biasanya digunakan untuk operasi sederhana dan sering digunakan sebagai argumen untuk fungsi lain.

#contoh lambda function
lambda_function = lambda x: x * 2
result_lambda = lambda_function(5)
print("Lambda Function Result:", result_lambda)
#begitupun dengan data yang lebih kompleks, contoh lambda yang lebih kompleks
complex_lambda = lambda x, y: (x + y) * 2
result_complex_lambda = complex_lambda(3, 4)
print("Complex Lambda Function Result:", result_complex_lambda)
#jika ingin menyortir data menggunakan lambda function, kita bisa menggunakan fungsi sorted() dengan key parameter.
data = [5, 2, 9, 1, 5, 6]
sorted_data = sorted(data, key=lambda x: x)
print("Sorted Data:", sorted_data)
#jika ingin menyortir data berdasarkan panjang elemen string, kita bisa menggunakan lambda function sebagai berikut:
string_data = ["apple", "banana", "kiwi", "cherry"]
sorted_string_data = sorted(string_data, key=lambda x: len(x))
print("Sorted String Data by Length:", sorted_string_data)

#day 44 tanggal 7 september 2026
#anonimous function adalah fungsi yang tidak memiliki nama, biasanya digunakan untuk operasi sederhana dan sering digunakan sebagai argumen untuk fungsi lain. Lambda function adalah salah satu contoh dari anonymous function di Python.  
#contoh penggunaan anonymous function dengan lambda function:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers using Lambda:", squared_numbers)
#maksud dari map adalah fungsi yang digunakan untuk menerapkan fungsi tertentu ke setiap elemen dalam iterable (seperti list) dan mengembalikan hasilnya sebagai map object. Dalam contoh di atas, kita menggunakan lambda function untuk mengkuadratkan setiap elemen dalam list numbers. Hasilnya kemudian dikonversi menjadi list menggunakan fungsi list().
#tahap logikanya seperti ini:
#1. Kita memiliki list numbers = [1, 2, 3, 4, 5].
#2. Kita menggunakan fungsi map() untuk menerapkan lambda function ke setiap elemen dalam list numbers.
#3. Lambda function mengambil setiap elemen x dari list dan mengembalikan x ** 2 (kuadrat dari x).
#4. Hasil dari map() adalah map object yang berisi hasil kuadrat dari setiap elemen dalam list numbers.
#5. Kita mengkonversi map object menjadi list menggunakan fungsi list(), sehingga kita mendapatkan list baru squared_numbers yang berisi hasil kuadrat dari setiap elemen dalam list numbers.

#contoh lain penggunaan anonymous function dengan lambda function:  
numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print("Cubed Numbers using Lambda:", cubed_numbers)

#contoh penggunaan anonymous function dengan lambda function untuk filter data:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers using Lambda:", even_numbers)
#cara kerja filter adalah sebagai berikut:
#1. Kita memiliki list numbers = [1, 2, 3, 4, 5].
#2. Kita menggunakan fungsi filter() untuk menyaring elemen dalam list numbers berdasarkan kondisi tertentu.
#3. Lambda function digunakan untuk menentukan kondisi penyaringan, dalam hal ini kita ingin menyaring elemen yang genap (x % 2 == 0).
#4. Hasil dari filter() adalah filter object yang berisi elemen-elemen yang memenuhi kondisi penyaringan.
#5. Kita mengkonversi filter object menjadi list menggunakan fungsi list(), sehingga kita mendapatkan list baru even_numbers yang berisi elemen-elemen genap dari list numbers.
#day 45 tanggal 8 september 2026 
#kelipatan 3 menggunakan anonymous function dengan lambda function:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiples_of_3 = list
(filter(lambda x: x % 3 == 0, numbers))
print("Multiples of 3 using Lambda:", multiples_of_3)
