#day 48 tanggal 13 september 2026 
#kita bisa mengimport file python lain ke dalam file python kita. Dengan mengimpor file python lain, kita dapat menggunakan fungsi, variabel, dan kelas yang didefinisikan di dalam file tersebut. Berikut contohnya:
#misalkan kita memiliki file python bernama "my_module.py" yang berisi fungsi dan variabel. Kita dapat mengimpor file tersebut ke dalam file python kita dengan menggunakan kata kunci "import". Berikut contohnya:
#kita akan mengimport file belajar18.py ke dalam file belajar19.py
import belajar18  # mengimpor file belajar18.py
# setelah mengimpor file belajar18.py, kita dapat menggunakan fungsi dan variabel yang didefinisikan di dalam file tersebut. Berikut contohnya:
print("Nilai x dari file belajar18.py:", belajar18.x)  # Output: 20
# kita juga dapat mengimpor fungsi dari file belajar18.py dan memanggilnya di dalam file belajar19.py
# misalkan kita ingin memanggil fungsi change_global_variable() dari file belajar18.py, kita dapat melakukannya dengan cara berikut:
belajar18.change_global_variable()  # memanggil fungsi change_global_variable() dari file belajar18.py
print("Nilai x setelah memanggil fungsi change_global_variable() dari file belajar18.py:", belajar18.x)  # Output: 20
# kita juga dapat mengimpor variabel dari file belajar18.py dan menggunakannya di dalam file belajar19.py. Misalkan kita ingin mengimpor variabel z dari file belajar18.py, kita dapat melakukannya dengan cara berikut:
print("Nilai z dari file belajar18.py:", belajar18.z)  # Output: 15 

#day 49 tanggal 14 september 2026
#kita juga dapat mengimpor file python lain dengan menggunakan kata kunci "from".
#misalkan kita ingin mengimpor fungsi change_global_variable() dari file belajar18.py, kita dapat melakukannya dengan cara berikut:
from belajar18 import change_global_variable  # mengimpor fungsi change_global_variable() dari file belajar18.py
# setelah mengimpor fungsi change_global_variable(), kita dapat memanggilnya di dalam file belajar19.py tanpa harus menulis nama file belajar18.py. Berikut contohnya:
change_global_variable()  # memanggil fungsi change_global_variable() dari file belajar18.py

