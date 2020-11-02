import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("550x25")

entry1 = tk.Entry(window, text="Enter a number", width=20)
entry2 = tk.Entry(window, text="Enter a number", width=20)
entry3 = tk.Entry(window, text="Enter a number", width=45)
label1 = tk.Label(window, text=" X ")
label2 = tk.Label(window, text=" = ")

entry1.grid(row = 1, column = 1)
label1.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
label2.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)
window.mainloop()



