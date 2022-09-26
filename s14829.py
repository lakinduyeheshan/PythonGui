import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

##--------window-------##
window= Tk()
window.geometry("336x200")
window.title("lakindu kolambage")
window.resizable(False,False)

##------Frames-----##
frame1= Frame(window)
frame1.pack(side="top")
frame2= Frame(window)
frame2.pack()
frame3= Frame(window)
frame3.pack()
frame4= Frame(window)
frame4.pack()
frame5= Frame(window)
frame5.pack()
frame6= Frame(window)
frame6.pack()
frame7= Frame(window)
frame7.pack()
frame8= Frame(window)
frame8.pack(side="bottom")

##------label-------##

lbl1=Label(frame1,text="s14829",foreground="red",background="red",width=200
           )
lbl1.pack()
entry=Entry(frame2,width=200,justify="right")
entry.pack()

##-----buttons--------##

def clicked(word):
    curr=entry.get()
    entry.delete(0,END)
    entry.insert(25,curr+word) 
    return

def revrese():
    a=entry.get()
    entry.delete(0,END)
    a=a[::-1]
    entry.insert(0,a)
    return
def erase(event):
    entry.delete(0,END)
    entry.config(foreground="black")
    return
def entering(event):
    lbl1.config(background="aqua")
    return
def leaving(event):
    lbl1.config(background="red")
    return
 

 
b2=Button(frame3,text="a",command=lambda:clicked("a")).pack(side="left")
b3=Button(frame3,text="b",command=lambda:clicked("b")).pack(side="left")
b4=Button(frame3,text="c",command=lambda:clicked("c")).pack(side="left")
b5=Button(frame3,text="d",command=lambda:clicked("d")).pack(side="left")
b6=Button(frame4,text="e",command=lambda:clicked("e")).pack(side="left")
b7=Button(frame4,text="g",command=lambda:clicked("g")).pack(side="left")
b8=Button(frame4,text="i",command=lambda:clicked("i")).pack(side="left")
b9=Button(frame4,text="k",command=lambda:clicked("k")).pack(side="left")
b10=Button(frame5,text="l",command=lambda:clicked("l")).pack(side="left")
b11=Button(frame5,text="m",command=lambda:clicked("m")).pack(side="left")
b12=Button(frame5,text="n",command=lambda:clicked("n")).pack(side="left")
b12=Button(frame6,text="o",command=lambda:clicked("o")).pack(side="left")
b13=Button(frame5,text="u",command=lambda:clicked("u")).pack(side="left")
b14=Button(frame6,text="space",command=lambda:clicked(" ")).pack(side="left")
b15=Button(frame6,text="reverse",command=revrese).pack(side="left")


entry.bind("<Button-3>",erase)
lbl1.bind("<Enter>",entering)
lbl1.bind("<Leave>",leaving)
entry.bind("<key>")

lbl2=Label(frame7,text="Lakindu Kolambage ",foreground="gold1",background="gold1",width=200)
lbl2.pack()
lbl3=Label(frame8,text="Select the Display Color :")
lbl3.pack(side="left")


def enter(event):
    lbl2.config(background="white")
    return
def leav(event):
    lbl2.config(background="gold1")
    return

lbl2.bind("<Enter>",enter)
lbl2.bind("<Leave>",leav)

def color1(event):
    entry.config(foreground="red")
    return
def color2(event):
    entry.config(foreground="blue")
    return
def color3(event):
    entry.config(foreground="yellow")
    return
def color4(event):
    entry.config(foreground="green")
    return
style=Style()
style.configure('W.TButton',background = "red",foreground="red",focusthickness=3)
style.map('W.TButton',background=[('active','red')])

clbl1=tk.Label(frame8,bg="red",width=5,relief="flat" )
clbl1.pack(side="left" )
clbl1.bind("<Button-1>",color1)
clbl2=tk.Label(frame8,bg="blue",width=5 )
clbl2.pack(side="left")
clbl2.bind("<Button-1>",color2)
clbl3=tk.Label(frame8,bg="yellow",width=5 )
clbl3.pack(side="left")
clbl3.bind("<Button-1>",color3)
clbl4=tk.Label(frame8,bg="green",width=5 )
clbl4.pack(side="left")
clbl4.bind("<Button-1>",color4)
window.mainloop()

