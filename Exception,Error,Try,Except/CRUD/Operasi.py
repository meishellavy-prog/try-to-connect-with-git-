from . import Database
from . import Kode 
import time
def file_baru():
    penulis = input("Penulis: ")
    judul = input("Judul Buku: ")
    tahun = input("Tahun :")
    data = Database.TEMPLATE.copy()
    data["pk"] = Kode.string_format(6)
    data["date_dt"] = time.strftime("%Y-%m-%d-%H:%M:%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun
    tampilan = f"{data['pk']},{data['date_dt']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    try:
        with open(Database.akhirnya,"w",encoding='utf-8') as file:
            file.write(tampilan)
    except:
        print("Gagal deh")


        