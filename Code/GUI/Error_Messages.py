import matplotlib
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tkst

############ Windows Valori Null eccessivi ############
def max_null():
    subrootnull = Toplevel()
    subrootnull.title("ERROR!!! too much null")
    subrootnull.configure(background='#B22222')
    subrootnull.geometry('330x100')
    label_null = tk.Label(subrootnull, text= "E' necessario compilare almeno 4 campi!!", font='Helvetica 13 bold',bg = '#B22222')
    label_null.grid(row = 1, column = 1)
    subrootnull.after(4000, lambda: subrootnull.destroy()) # Destroy the widget after 4 seconds
    subrootnull.mainloop()
############ ############ ############ ############

############ Windows Valori Real Value Error ############
def error_realvalue():
    subrooterr = Toplevel()
    subrooterr.title("ERROR!!! No overall value")
    subrooterr.configure(background='#B22222')
    subrooterr.geometry('330x100')
    label_null = tk.Label(subrooterr, text= "E' necessario inserire l'Overall value!!", font='Helvetica 13 bold',bg = '#B22222')
    label_null.grid(row = 1, column = 1)
    subrooterr.after(4000, lambda: subrooterr.destroy()) # Destroy the widget after 4 seconds
    subrooterr.mainloop()
############ ############ ############ ############
