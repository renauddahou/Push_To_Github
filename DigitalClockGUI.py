import tkinter
import time
import sys
window = tkinter.Tk()
window.geometry("500x500")
window.title("GUI Project 1")
label = tkinter.Label(window,font=("Arial",90),fg="blue",bg="orange")
label.pack()
def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    label.config(text=timeVar)
    label.after(200, get_time)
get_time()
window.mainloop()