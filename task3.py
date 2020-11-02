import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("255x137")

label2 = tk.Label(window, text = "A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#A3FFF0")
label3 = tk.Label(window, text="Pochacco!")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2.grid(row = 4, column = 1, columnspan = 5)
label1.grid(row = 1, column = 2, rowspan = 3)
label3.grid(row = 2, column = 3)
window.mainloop()