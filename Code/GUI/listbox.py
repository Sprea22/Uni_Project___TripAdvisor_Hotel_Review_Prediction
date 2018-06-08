from Tkinter import *

def select_hotel():
    global value
    value = str(listNodes.get(listNodes.curselection()))
    print value
    return value

window = Tk()
window.geometry("680x500")
window.title("Hotel")
Label(window, text="Select Hotel").pack()

frame = Frame(window)
frame.pack()

listNodes = Listbox(frame, width=20, height=20, font=("Helvetica", 12))
listNodes.pack(side="left", fill="y")

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=listNodes.yview)
scrollbar.pack(side="right", fill="y")

listNodes.config(yscrollcommand=scrollbar.set)

hotel = "hotel1","hotel2","hotel3","hotel4"
listNodes.insert(END, *hotel)

invio = Button(window, text="OK", font='Helvetica 10 bold',command = select_hotel).pack()

window.mainloop()
