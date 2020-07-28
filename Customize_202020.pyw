from tkinter import *
from tkinter import messagebox  

f = open("config")
options = [int(i) for i in f.read().split("\n")]
f.close()

root = Tk()
root.title('Customize')
root.geometry(f"400x350")
l1 = Label(root, text='Customize 202020', font=("Calibri", 20))
l2 = Label(root, text='Computer usage time (in minutes)')
ctime = Scale(root, from_=10, to=60, tickinterval=10, resolution=5, length=300, orient=HORIZONTAL)
ctime.set(options[0])
l3 = Label(root, text='Look away time (in seconds)')
ltime = Scale(root, from_=10, to=60, tickinterval=10, resolution=5, length=300, orient=HORIZONTAL)
ltime.set(options[0])
l4 = Label(root, text='Time to pause work (in seconds)')
ptime = Scale(root, from_=1, to=10, tickinterval=1, resolution=1, length=300, orient=HORIZONTAL)
ptime.set(options[2])

def set_():
    f = open("config", "w")
    f.write(str(ctime.get()))
    f.write("\n")
    f.write(str(ltime.get()))
    f.write("\n")
    f.write(str(ptime.get()))
    f.close()

    messagebox.showinfo("Values set","The specified values have been set.\nPlease restart the application to use the new values.")

b = Button(root, text='Save Settings', command=set_)


l1.pack()
l2.place(x=50, y=50)
ctime.place(x=50, y=70)
l3.place(x=50, y=130)
ltime.place(x=50, y=150)
l4.place(x=50, y=210)
ptime.place(x=50, y=230)
b.place(x=160, y=310)
root.mainloop()