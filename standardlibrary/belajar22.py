#day 56 tanggal 24 september 2026
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
window = tk.Tk()
window.configure(bg="green")
window.geometry("1000x1000")
window.title("MEISHELLAPROG")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

#FRAME INPUT
frame_input = ttk.Frame(window)
#penempatan grid,pack, place
frame_input.pack(padx=30,pady=30,fill="x",expand=True)

input_nama_depan = ttk.Label(frame_input, text="Nama Depan")
input_nama_depan.pack(padx=10, pady=2,fill="x",expand=True)
entry_nama_depan = ttk.Entry(frame_input, textvariable=NAMA_DEPAN)
entry_nama_depan.pack(padx=10,pady=10,fill="x",expand=True)
input_nama_belakang = ttk.Label(frame_input,text="Nama Belakang" )
input_nama_belakang.pack(padx=10,pady=2,fill="x",expand=True)
entry_nama_belakang = ttk.Entry(frame_input, textvariable=NAMA_BELAKANG)
entry_nama_belakang.pack(padx=10,pady=10,fill="x",expand=True)

def fungsi_tombol():
    '''ini adalah fungsi dan akan running jika tombol di tekan'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} selamat datang di program ini!"
    showinfo(title="program",message=pesan)

button = ttk.Button(frame_input,text="masuk",command=fungsi_tombol)
button.pack(padx=30,pady=30,fill="x",expand=True)

#window.mainloop()