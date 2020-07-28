import sys
from tkinter import *
from tkinter import ttk
from beeply import notes
import time

_pause = False
_snooze = False
_skip = False
_exit = False

f = open("config")
options = [int(i) for i in f.read().split("\n")]

mybeep = notes.beeps()

root = Tk()
root.overrideredirect(1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(background='#2c3e50')

def pause():
    global _pause
    _pause = True

def snooze():
    global _snooze
    _snooze = True

def skip():
    global _skip
    _skip = True

def exit_():
    global _exit
    _exit = True

def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()

f = Frame(root)
f.configure(background='#2c3e50')
mainlabel = Label(f, text="Look at something 20 feet away for " + str(options[1]) + " seconds.", font=("Calibri", 48), foreground="#ecf0f1", background="#2c3e50")
mainlabel.pack()
progress_var = DoubleVar()
s = ttk.Style()
s.theme_use("default")
s.configure("TProgressbar", thickness=10, foreground="#ecf0f1", background='#2c3e50', troughrelief = 'flat')
progress = ttk.Progressbar(f, orient=HORIZONTAL, length=1000, style="TProgressbar", variable=progress_var)
progress.pack()

btns = Frame(f)
btns.configure(background='#2c3e50')
b = Button(btns, text="Let me pause my work", font=("Calibri", 20), relief=FLAT, foreground='#95a5a6', background='#2c3e50', activeforeground='#95a5a6', activebackground='#2c3e50', command=pause)
b.pack(side=LEFT)
b1 = Button(btns, text="Snooze for 5 min", font=("Calibri", 20), relief=FLAT, foreground='#95a5a6', background='#2c3e50', activeforeground='#95a5a6', activebackground='#2c3e50', command=snooze)
b1.pack(side=LEFT)
b2 = Button(btns, text="Skip for now", font=("Calibri", 20), relief=FLAT, foreground='#95a5a6', background='#2c3e50', activeforeground='#95a5a6', activebackground='#2c3e50', command=skip)
b2.pack(side=LEFT)
b3 = Button(btns, text="Close the app", font=("Calibri", 20), relief=FLAT, foreground='#95a5a6', background='#2c3e50', activeforeground='#95a5a6', activebackground='#2c3e50', command=exit_)
b3.pack(side=LEFT)
btns.pack(expand=True)
f.pack(expand=True)

while True:
    for i in range(options[0] * 60):
        time.sleep(1)

    root.deiconify()
    progress.step(0)
    root.attributes('-topmost', True)
    root.update()

    i = 0
    while i < (options[1] * 50):
        progress_var.set(100 - (i / (options[1] * 50) * 100))
        root.update()
        sleep(0.02)
        if _pause == True:
            _pause = False
            root.withdraw()
            time.sleep(options[2])
            root.deiconify()
            root.update()
            i = 0
        if _snooze:
            _snooze = False
            root.withdraw()
            time.sleep(300)
            root.deiconify()
            root.update()
            i = 0
        if _skip:
            _skip = False
            break
        if _exit == True:
            break
        i += 1
    mybeep.hear('D', 500)
    root.withdraw()

    if _exit == True:
        break