from tkinter import Tk,END,Entry

#click button
def get_input(entry, argu):
    entry.insert(END, argu)

#
def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

#clear function
def clear(entry):
    entry.delete(0, END)

#calcul funct 
def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END, output)

#
def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("120x100")
    popup.title("Alert")
 