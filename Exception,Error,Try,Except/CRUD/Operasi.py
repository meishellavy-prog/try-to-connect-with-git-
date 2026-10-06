from . import Database
from . import Kode 
import time

def file_baru():
    with open(Database.akhirnya,"w",encoding="utf-8") as file:
        penulis = input("Penulis: ")
        judul = input("Judul Buku: ")
        tahun = input("Tahun :")
        data = Database.TEMPLATE.copy()
        data["pk"] = Kode.string_format(6)
        data["date_dt"] = time.strftime("%Y-%m-%d-%H:%M:%S%z", time.gmtime())
        data["penulis"] = penulis
        data["judul"] = judul
        data["tahun"] = tahun
        file.write(str(data))
        