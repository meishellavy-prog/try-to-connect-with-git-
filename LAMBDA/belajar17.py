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

