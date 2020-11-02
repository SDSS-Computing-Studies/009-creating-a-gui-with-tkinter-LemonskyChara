import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("600x180")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Search by Name")
entry1 = tk.Entry(window, text="Enter", width = 18)
label4 = tk.Label(window, text="Client Database")
label5 = tk.Label(window, text="Name")
label6 = tk.Label(window, text="Type")
label7 = tk.Label(window, text="Breed")
label8 = tk.Label(window, text="Owner")
label9 = tk.Label(window, text="Birthdate")
enter2 = tk.Entry(window, width = 15)
enter3 = tk.Entry(window, width = 15)
enter4 = tk.Entry(window, width = 15)
enter5 = tk.Entry(window, width = 15)
enter6 = tk.Entry(window, width = 15)
button1 = tk.Button(window, text="Save Entry")
button2 = tk.Button(window, text="< Previous")
button3 = tk.Button(window, text="Next >")


label5.place(x = 15, y = 95)
label6.place(x = 135, y = 95)
label7.place(x = 255, y = 95)
label8.place(x = 375, y = 95)
label9.place(x = 495, y = 95)
label1.place(x = 0, y = 0)
label2.place(x = 380, y = 0)
entry1.place(x = 480, y = 0)
label4.place(x = 230, y = 40)
enter2.place(x = 5, y = 120)
enter3.place(x = 105, y = 120)
enter4.place(x = 235, y = 120)
enter5.place(x = 355, y = 120)
enter6.place(x = 475, y = 120)
button1.place(x = 245, y = 150)
button2.place(x = 0, y = 150)
button3.place(x = 550, y = 150)


window.mainloop()