from tkinter import *
from tkinter import ttk
from tkinter import messagebox
next7 =Toplevel()
next7.title("Tyson Service System")
next7.geometry("925x500+300+200")
next7.iconbitmap("bit.png")
next7.resizable(False,False)
next7.config(bg="white")
#pages.Push(next5)

image = PhotoImage(file ="location1.png")
Label(next7,image = image).pack()

Frame1 = Frame(next7,height=50,width = 925,bg="black",).place(x=0,y=0)
Label(next7,text="List of packages Locaton wise",bg="black",fg="#57a1f8",font =("Microsoft YaHei UI Light",18,"bold")).place(x=10,y=5)
#Button(next7,width=15,pady = 5,text="Admin",bg ="#57a1f8",fg = "black",border=3,command=info).place(x=800,y=10)
Frame2 = Frame(next7,height=425,width =910,bg="white").place(x=5,y=60)
image = PhotoImage(file ="cons.png")
Label(next7,image = image).place(x=550,y=80)

head=Label(next7,text="Location",fg = "#57a1f8",bg="black",padx = 10,pady=2,font =("Microsoft YaHei UI Light",15,"bold"))
head.place(x=56,y=91)

location=Entry(next7,width = 20,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
location.place(x=175,y=91)
    
Button(next7,width=39,pady = 5,border = 5,text="Track",bg ="#57a1f8",fg = "white",cursor ="hand2").place(x=100,y=150)
Button(next7,pady = 5,width=15,border = 5,text="Previous",bg ="#57a1f8",fg = "white",cursor ="hand2").place(x=50,y=350)
next7.mainloop()