from . import Operasi 

NAMA = "data.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "date_dt" :"yyyy-mm-dd",
    "penulis" : " "*255,
    "judul" : " "*255,
    "tahun" : "yyyy"
}
from pathlib import Path 
lokasipasti = Path(__file__).parent
akhirnya= lokasipasti / NAMA
def nulis():
    try :
        with open(akhirnya,"r") as file:
            print("File tersedia, segera membaca file")
    except :
        print("File tidak tersedia, segera membuat file baru: ")
        Operasi.file_baru()