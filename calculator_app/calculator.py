from tkinter import Tk,END

#click button
def get_input(entry, argu):
    entry.insert(END, argu)


#clear function
def clear(entry):
    entry.delete(0, END)
