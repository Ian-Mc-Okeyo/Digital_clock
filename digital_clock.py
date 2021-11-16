from tkinter import *
from datetime import datetime
root = Tk()
root.geometry("600x300")
root.config(bg="steelblue")
root.title("Digital Clock")
label = Label(root, text="Welcome", font=("Arial Black", 78, "bold"), bg="steelblue", fg="white")
label.pack(pady=100)
def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.config(text=time)
    label.after(1000, clock)

clock()
root.mainloop()