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

label3.place(x = 120, y = 40)
label1.place(x = 70, y = 0 )
label2.place(x = 0, y = 101)
window.mainloop()