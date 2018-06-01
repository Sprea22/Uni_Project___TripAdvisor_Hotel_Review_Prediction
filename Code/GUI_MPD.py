import Tkinter as tk
import tkMessageBox
import ScrolledText as tkst
from Tkinter import *
from PIL import Image, ImageTk

############ Frequency Filtering ############
def update_overall():
    parameter_1.insert(INSERT, "")
    parameter_1.insert(END, "")
    print(parameter_1.get(1.0, END))
    return -1

############ ############ ############ ############

############ Frequency Filtering ############
def print_BN():
    return -1
############ ############ ############ ############

############ Frequency Filtering ############
def file_selection():
    return -1
############ ############ ############ ############

# Create the main window
print("Building the GUI interface..")
root = tk.Tk()
root.title("GUI Interface - MPD - TripAdvisor Project")
#size windows
#root.geometry("900x900")
#size full windows

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%sx%s' % (width, height))
#change windows color
#root.configure(background='black')

'''
# Set the original image label and initialize it to "no_img"
original_pic = Image.open(r"Original_Photos/no_img.png")
original_pic = original_pic.resize((450, 450), Image.ANTIALIAS)
original_photo = ImageTk.PhotoImage(original_pic)
'''
# Set the entry for the first parameter
var1_descr = " Enter a text review: "
label_descr1 = tk.Label(root, text=var1_descr)
parameter_1 = tkst.ScrolledText(root, width =80, height=5, wrap = WORD, bd = 3)
#parameter_1 = tk.Entry(root, width =100, bd=3)

# Create the buttons
update_button = tk.Button(root, text = "Update", command = update_overall)

# Grid is used to add the widgets to root
# Alternatives are Pack and Place
label_descr1.grid(row = 9, column = 13, padx = 10)
parameter_1.grid(row = 10, column = 13,padx = 40)
update_button.grid(row = 11, column = 13)

print("GUI Interface is ready!\n")

######################### RADIOBUTTON 1 ########################################

def selected():
    print("Value: "+var1.get())

var1 = tk.StringVar()

#label over radiobutton
label_term1 = tk.Label(root, text= "Value:")
label_term1.grid(row = 9, column = 1, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var1, command= selected)
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=9, column=2, pady=10)

rate2 = tk.Radiobutton(text='2', variable=var1, command= selected)
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=9, column=3)

rate3 = tk.Radiobutton(text='3', variable=var1, command= selected)
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=9, column=4)

rate4 = tk.Radiobutton(text='4', variable=var1, command= selected)
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=9, column=5)

rate5 = tk.Radiobutton(text='5', variable=var1, command= selected)
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=9, column=6)

################################################################################

######################### RADIOBUTTON 2 ########################################

def selected():
    print("Rooms: "+var2.get())

var2 = tk.StringVar()

#label over radiobutton
label_term2 = tk.Label(root, text= "Rooms:")
label_term2.grid(row = 10, column = 1, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var2, command= selected)
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=10, column=2,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var2, command= selected)
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=10, column=3)

rate3 = tk.Radiobutton(text='3', variable=var2, command= selected)
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=10, column=4)

rate4 = tk.Radiobutton(text='4', variable=var2, command= selected)
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=10, column=5)

rate5 = tk.Radiobutton(text='5', variable=var2, command= selected)
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=10, column=6)

################################################################################

######################### RADIOBUTTON 3 ########################################

def selected():
    print("Location: "+var3.get())

var3 = tk.StringVar()

#label over radiobutton
label_term3 = tk.Label(root, text= "Location:")
label_term3.grid(row = 11, column = 1, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var3, command= selected)
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=11, column=2,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var3, command= selected)
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=11, column=3)

rate3 = tk.Radiobutton(text='3', variable=var3, command= selected)
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=11, column=4)

rate4 = tk.Radiobutton(text='4', variable=var3, command= selected)
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=11, column=5)

rate5 = tk.Radiobutton(text='5', variable=var3, command= selected)
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=11, column=6)

################################################################################

######################### RADIOBUTTON 4 ########################################

def selected():
    print("Cleanliness: "+var4.get())

var4 = tk.StringVar()

#label over radiobutton
label_term4 = tk.Label(root, text= "Cleanliness:")
label_term4.grid(row = 12, column = 1, padx=10, pady=35)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var4, command= selected)
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=12, column=2, pady=10)

rate2 = tk.Radiobutton(text='2', variable=var4, command= selected)
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=12, column=3)

rate3 = tk.Radiobutton(text='3', variable=var4, command= selected)
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=12, column=4)

rate4 = tk.Radiobutton(text='4', variable=var4, command= selected)
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=12, column=5)

rate5 = tk.Radiobutton(text='5', variable=var4, command= selected)
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=12, column=6)

################################################################################

######################### RADIOBUTTON 5 ########################################

def selected():
    print("Check in :"+var5.get())

var5 = tk.StringVar()

#label over radiobutton
label_term5 = tk.Label(root, text= "Check in:")
label_term5.grid(row = 9, column = 7, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var5, command= selected)
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=9, column=8,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var5, command= selected)
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=9, column=9)

rate3 = tk.Radiobutton(text='3', variable=var5, command= selected)
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=9, column=10)

rate4 = tk.Radiobutton(text='4', variable=var5, command= selected)
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=9, column=11)

rate5 = tk.Radiobutton(text='5', variable=var5, command= selected)
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=9, column=12)

################################################################################

######################### RADIOBUTTON 6 ########################################

def selected():
    print("Service: "+var6.get())

var6 = tk.StringVar()

#label over radiobutton
label_term6 = tk.Label(root, text= "Service:")
label_term6.grid(row = 10, column = 7, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var6, command= selected)
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=10, column=8,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var6, command= selected)
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=10, column=9)

rate3 = tk.Radiobutton(text='3', variable=var6, command= selected)
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=10, column=10)

rate4 = tk.Radiobutton(text='4', variable=var6, command= selected)
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=10, column=11)

rate5 = tk.Radiobutton(text='5', variable=var6, command= selected)
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=10, column=12)

################################################################################

######################### RADIOBUTTON 7 ########################################

def selected():
    print("Businness Service: "+var7.get())

var7 = tk.StringVar()

#label over radiobutton
label_term7 = tk.Label(root, text= "Businness Service:")
label_term7.grid(row = 11, column = 7, padx=10, pady=10)

#radiobutton
rate1 = tk.Radiobutton(text='1', variable=var7, command= selected)
rate1.config(indicatoron=0, bd=1, width=2, value='rate1')
rate1.grid(row=11, column=8,pady=10)

rate2 = tk.Radiobutton(text='2', variable=var7, command= selected)
rate2.config(indicatoron=0, bd=1, width=2, value='rate2')
rate2.grid(row=11, column=9)

rate3 = tk.Radiobutton(text='3', variable=var7, command= selected)
rate3.config(indicatoron=0, bd=1, width=2, value='rate3')
rate3.grid(row=11, column=10)

rate4 = tk.Radiobutton(text='4', variable=var7, command= selected)
rate4.config(indicatoron=0, bd=1, width=2, value='rate4')
rate4.grid(row=11, column=11)

rate5 = tk.Radiobutton(text='5', variable=var7, command= selected)
rate5.config(indicatoron=0, bd=1, width=2, value='rate5')
rate5.grid(row=11, column=12)

############################### PRINT BN #######################################

def show_image():
    x = canvas.create_image(220, 160, image=tk_img)
    while True:
        print('show')
        canvas.itemconfigure(x, state=tk.NORMAL)
        print_button.configure(text = 'Hide Bayesian Network Model')
        yield
        print('hide')
        canvas.itemconfigure(x, state=tk.HIDDEN)
        print_button.configure(text = 'Show Bayesian Network Model')
        yield
canvas = tk.Canvas(root, width=450, height=320)
canvas.grid(row=13, column=13)
tk_img = ImageTk.PhotoImage(file='ImageBayesianNet.png')

print_button = tk.Button(
    root, text="Print Bayesian Network Model", command=show_image().next, anchor='w',
     activebackground="#33B5E5")
print_button.grid(row = 12, column = 13)

################################################################################

tripadvisor_img = ImageTk.PhotoImage(file = 'tripadvisor.jpg')
canvas1 = tk.Canvas(root, width=340, height=110)
canvas1.create_image(170, 55, image=tripadvisor_img, anchor = CENTER)
canvas1.grid(row=1, column=13, pady = 3)

################################################################################

root.mainloop()
