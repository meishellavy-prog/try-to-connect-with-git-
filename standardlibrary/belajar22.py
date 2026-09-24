#day 56 tanggal 24 september 2026
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg="green")
window.geometry("1000x1000")
window.title("MEISHELLAPROG")

#FRAME INPUT
frame_input = ttk.Frame(window)
#penempatan grid,pack, place
frame_input.pack(padx=30,pady=30,fill="x",expand=True)

#window.mainloop()