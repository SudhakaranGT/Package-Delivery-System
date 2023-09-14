from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import json
from datetime import date


class stack:
    def __init__(self):
        self.st=[]

    def Push(self,node):
        self.st.append(node)
        
    def Pop(self):
        return self.st.pop()

    def top(self):
        if (len(self.st)):
            return self.st[-1]
        return 0
    

    

def signin():
    global currentuser
    Username =user.get()
    Password =password.get()
    f=open("accounts.json","r")
    try:
        l=json.load(f)
    except:
        l={}
    f.close()
 
    if Username =="admin" and Password =="1234":
        AdminMenu()

    elif Username in l and l[Username]["password"]==Password:
        currentuser=Username
        Menu()

    else:
        messagebox.showerror("invalid","Wrong Username or Password")

def signup():
    global pages
    pages.top().withdraw()
    p=Toplevel(root,bg="white")
    p.geometry("925x500+300+200")
    p.iconbitmap("bit.png")
    pages.Push(p)


    frame = Frame(p,width =350,height=350,bg="white")
    frame.place(x=480,y=70)

    head=Label(p,text="Sign up",fg = "#57a1f8",bg="white",font =("Microsoft YaHei UI Light",23,"bold"))
    head.place(x=100,y=5)



    Frame2 = Frame(p,height=200,width =910,bg="white").place(x=5,y=60)

    Label(p,text="Phone number: ",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=150)
    ph_s = Entry(p,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    ph_s.place(x=290,y=152)

    Label(p,text="Password",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=200)
    pas_s= Entry(p,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18),show="*")
    pas_s.place(x=290,y=202)

    Label(p,text="Confirm password",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=250)
    con_s= Entry(p,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18),show="*")
    con_s.place(x=290,y=252)

    
    Button(p,width=15,pady = 7,text="Next",bg ="#57a1f8",fg = "white",border=0,command =lambda:signup2(ph_s.get(),pas_s.get(),con_s.get())).place(x=450,y=385)
    Button(p,width=15,pady = 7,text="Previous",bg ="#57a1f8",fg = "white",border=0,command =navigatebefore).place(x=300,y=385)
    p.mainloop()
           
def signup2(ph,pas,con):
    flag=0
    f=open("accounts.json","r")
    try:
        l=json.load(f)
        if (ph in l):
            flag=1
    except:
        l={}
        pass
    f.close()
    if (not flag and len(ph)==10 and pas==con):
        global pages
        pages.top().withdraw()
        q =Toplevel()
        q.title("Tyson Service System")
        q.geometry("925x500+300+200")
        q.iconbitmap("bit.png")
    
        q.config(bg="white")
        pages.Push(q)

        Frame1 = Frame(q,height=50,width = 925,bg="black",).place(x=0,y=0)
        Frame2 = Frame(q,height=200,width =910,bg="white").place(x=5,y=60)

        Label(q,text="User details",bg="white",fg="#57a1f8",font =("Microsoft YaHei UI Light",20,"bold")).place(x=380,y=70)

        Label(q,text="Name",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=150)
        name_s = Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
        name_s.place(x=290,y=152)

        Label(q,text="Email ID",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=200)
        email_s = Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
        email_s.place(x=290,y=202)

        Label(q,text="Address",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=250)
        ad_s= Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
        ad_s.place(x=290,y=252)

        Label(q,text="Pin Code",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=300)
        loc_s= Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
        loc_s.place(x=290,y=302)
        
        Button(q,width=15,pady = 20,text="Create Account",bg ="#57a1f8",fg = "white",border=0,command =lambda: signup3(ph,pas,name_s.get(), email_s.get(),ad_s.get(),loc_s.get())).place(x=350,y=385)
        
        q.mainloop()
    else:
        messagebox.showerror("Try again","Either the number is already registered/ the password doesn't match/ invalid phone number")
        return
    
def Update():
    global currentuser
    global pages
    f=open("accounts.json","r")
    try:
        d=json.load(f)
    except:
        d={}
    f.close()
    pas=d[currentuser]["password"]
    pages.top().withdraw()
    q =Toplevel()
    q.title("Tyson Service System")
    q.geometry("925x500+300+200")
    q.iconbitmap("bit.png")

    q.config(bg="white")
    pages.Push(q)

    Frame1 = Frame(q,height=50,width = 925,bg="black",).place(x=0,y=0)
    Frame2 = Frame(q,height=200,width =910,bg="white").place(x=5,y=60)

    Label(q,text="User details",bg="white",fg="#57a1f8",font =("Microsoft YaHei UI Light",20,"bold")).place(x=380,y=70)

    Label(q,text="Name",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=150)
    name_s = Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    name_s.place(x=290,y=152)

    Label(q,text="Emil Id",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=200)
    email_s = Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    email_s.place(x=290,y=202)

    Label(q,text="Address",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=250)
    ad_s= Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    ad_s.place(x=290,y=252)

    Label(q,text="City/Town",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=300)
    loc_s= Entry(q,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    loc_s.place(x=290,y=302)

    Button(q,width=15,pady = 20,text="Update",bg ="#57a1f8",fg = "white",border=0,command =lambda: signup3(currentuser,pas,name_s.get(),email_s.get(),ad_s.get(),loc_s.get())).place(x=500,y=385)
    Button(q,width=15,pady = 20,text="Previous",bg ="#57a1f8",fg = "white",border=0,command =navigatebefore).place(x=350,y=385)
    q.mainloop()
    
def signup3(ph,pas,name,eml,ad,loc):
    if (name==""):
        messagebox.showinfo("info","Field(s) are empty!")
        return

    f=open("accounts.json","r")
    try:
        l=json.load(f)
    except:
        l={}
    g=open("temp.json","w")
    l[ph]={"password":pas,"name":name,"email_id":eml,"address":ad,"location":loc}
    g.write(json.dumps(l))
    f.close()
    g.close()
    os.remove("accounts.json")
    os.rename("temp.json","accounts.json")
    messagebox.showinfo("info","Details added succesfully")
    navigatebefore()
    navigatebefore()

    
        

        
        
    



def navigatebefore():
    global pages
    w=pages.Pop()
    if(pages.top()):
        pages.top().deiconify()
    w.withdraw()

    
def printTable(window,l):
    window.attributes('-fullscreen', True)
    fr=Frame(window,bg="white")
    fr.pack(fill=BOTH,expand=1)
    cnv=Canvas(fr,bg="white")
    cnv.pack(side=LEFT, fill=BOTH, expand=1)
    sc=Scrollbar(fr,orient=VERTICAL, command= cnv.yview)
    sc.pack(side=RIGHT,fill=Y)
    cnv.configure(yscrollcommand=sc.set)
    cnv.bind('<Configure>',lambda e: cnv.configure(scrollregion=cnv.bbox("all")))
    fr2=Frame(cnv,bg="white")
    cnv.create_window((0,0),window=fr2,anchor="nw")
    rows=len(l)
    c=list(l[0].keys())
    columns=len(c)
    Button(fr2,pady = 5,border = 5,text="Previous",bg ="#57a1f8",fg = "white",cursor ="hand2",command =navigatebefore).grid(row=0,column=0)
    for i in range(columns):
        e=Label(fr2,text=c[i],borderwidth=1,fg="#57a1f8",bg ="white",font=('Arial',20,'bold'),relief="solid",width=20)
        e.grid(row=1,column=i)
    for i in range(rows):
        temp=list(l[i].values())
        for j in range(columns):
            e = Label(fr2,borderwidth=1,text=temp[j], fg="black",bg ="white",font=('Arial',20,'bold'),relief="solid",width=20)
            e.grid(row=i+2, column=j)

            
    

def writefile(a,b,c,d,e,f,g,h):
    di={}
    di["Sender name"]=a
    di["Sender address"]=b
    di["Sender contact"]=c
    di["Sender city"] =d
    di["Receiver name"]=e
    di["Receiver address"]=f
    di["Receiver contact"]=g
    di["status"]="not delivered"
    di["location"]=h


    i=open("data.json","r")
    j=open("userwise.json","r")
    k=open("temp.json","w")
    l=open("temp1.json","w")
    
    try:
        m=json.load(i)
    except:
        m={}
        
    try:
        n=json.load(j)
    except:
        n={}
        
    if (len(m)):
        t=int(list(m.keys())[-1])+1
        m[t]=di
    else:
        t=0
        m[0]=di

    if c in n:
        n[c]["sent"].append(t)
    else:
        n[c]={"sent":[t],"received":[]}
    if g in n:
        n[g]["received"].append(t)
    else:
        n[g]={"sent":[],"received":[t]}

    k.write(json.dumps(m))
    l.write(json.dumps(n))
    i.close()
    j.close()
    k.close()
    l.close()
    os.remove("data.json")
    os.remove("userwise.json")
    os.rename("temp.json","data.json")
    os.rename("temp1.json","userwise.json")
    messagebox.showinfo("info","package dispatched!")
    navigatebefore()
    #navigatebefore()

def AdminMenu():
        global pages
        next = Toplevel(root)
        pages.top().withdraw()
        next.title("Tyson Service System")
        next.geometry("925x500+300+200")
        next.iconbitmap("bit.png")
        next.resizable(False,False)
        next.config(bg="white")
        pages.Push(next)

        Frame1 = Frame(next,height=50,width = 925,bg="black",).place(x=0,y=0)
        Label(next,text="Final Lap Service System",bg="black",fg="#57a1f8",font =("Microsoft YaHei UI Light",18,"bold")).place(x=10,y=5)
        #Button(next,width=15,pady = 5,text="Admin",bg ="#57a1f8",fg = "black",border=3,command=info).place(x=800,y=10)

        Frame2 = Frame(next,height=425,width =910,bg="white").place(x=5,y=60)
        Frame(next,width =400,height = 400,)
        Label(next,text ="Menu",width = 18,pady = 5,bg ="black",fg ="#57a1f8",font =("Microsoft YaHei UI Light",15,"bold")).place(x=100,y=125)

        button1 = Button(next,text="Parcel Information",width=30,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=track).place(x=100,y=200)
        button2 = Button(next,text="List of deliveries - date wise",width=30,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=date_wise).place(x=100,y=240)
        button3 = Button(next,text="List of deliveries - Location wise",width=30,pady = 5,bg ="#57a1f8",fg ="black",border=3,command =location_wise).place(x=100,y=280)
        logout = Button(next,text="logout",width=30,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=navigatebefore).place(x=100,y=320)
        
   

        image =PhotoImage(file="p.png")
        Label(next,image=image,bg="white").place(x=500,y=80)
        
        next.mainloop()

def Menu():
    global pages
    next = Toplevel(root)
    pages.top().withdraw()
    next.title("Tyson Service System")
    next.geometry("925x500+300+200")
    next.iconbitmap("bit.png")
    next.resizable(False,False)
    next.config(bg="white")
    pages.Push(next)

    Frame1 = Frame(next,height=50,width = 925,bg="black",).place(x=0,y=0)
    Label(next,text="Tyson Service System",bg="black",fg="#57a1f8",font =("Microsoft YaHei UI Light",18,"bold")).place(x=10,y=5)
    #Button(next,width=15,pady = 5,text="Admin",bg ="#57a1f8",fg = "black",border=3,command=info).place(x=800,y=10)

    Frame2 = Frame(next,height=425,width =910,bg="white").place(x=5,y=60)

    Label(next,text ="Menu",width = 30,pady = 5,bg ="black",fg ="#57a1f8",font =("Microsoft YaHei UI Light",15,"bold")).place(x=40,y=80)
    button5 = Button(next,text="Send a package",width=50,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=add_delivery).place(x=40,y=190)
    button5 = Button(next,text="List of packages sent by you",width=50,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=sent).place(x=40,y=230)
    button6 = Button(next,text="List of packages you recieved/yet to receive",width=50,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=received).place(x=40,y=270)
    update=Button(next,text="Update account details",width=50,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=Update).place(x=40,y=310)
    logout = Button(next,text="logout",width=50,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=navigatebefore).place(x=40,y=350)
    button7 = Button(next,text="Help",width=50,pady = 5,bg ="#57a1f8",fg ="black",border=3,command=Help).place(x=40,y=390)
    image =PhotoImage(file="p.png")
    Label(next,image=image,bg="white").place(x=500,y=80)
    next.mainloop()



def add_delivery():
    f=open("accounts.json","r")
    try:
        l=json.load(f)
    except:
        l={}

    a=l[currentuser]["name"]
    b=l[currentuser]["address"]
    c=currentuser
    d=l[currentuser]["location"]
    f.close()
    next2 =Toplevel()
    next2.title("Tyson Service System")
    next2.geometry("925x500+300+200")
    next2.iconbitmap("bit.png")
    next2.resizable(False,True)
    next2.config(bg="white")
    pages.Push(next2)

    Frame1 = Frame(next2,height=50,width = 925,bg="black",).place(x=0,y=0)
    Label(next2,text="Add delivery",bg="black",fg="#57a1f8",font =("Microsoft YaHei UI Light",20,"bold")).place(x=10,y=5)

    Frame2 = Frame(next2,height=200,width =910,bg="white").place(x=5,y=60)

    Label(next2,text="Receiver details",bg="white",fg="#57a1f8",font =("Microsoft YaHei UI Light",20,"bold")).place(x=380,y=70)

    Label(next2,text="Receiver's phone number",bg="#57a1f8",fg="black",font =("Microsoft YaHei UI Light",8,"bold")).place(x=100,y=150)
    ph_r = Entry(next2,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    ph_r.place(x=290,y=152)

    Label(next2,text="re-confirm phone number",bg="#57a1f8",fg="black",font =("Microsoft YaHei UI Light",8,"bold")).place(x=100,y=250)
    re_r= Entry(next2,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    re_r.place(x=290,y=250)

    Label(next2,text="Parcel Product",bg="#57a1f8",fg="black",font =("Microsoft YaHei UI Light",8,"bold")).place(x=100,y=350)
    ke_w=Entry(next2,width = 40,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    ke_w.place(x=290,y=350)


    Button(next2,width=39,pady = 7,text="Add delivery",bg ="#57a1f8",fg = "white",border=0,command = lambda:process(a,b,c,d,ph_r.get(),re_r.get(),l)).place(x=500,y=425)

    Button(next2,width=39,pady = 7,text="Previous",bg ="#57a1f8",fg = "white",border=0,command = navigatebefore).place(x=200,y=425)

    next2.mainloop()

    
def process(a,b,c,d,ph,re,l):
    if (ph==re):
        if (ph in l):
            if(ph!=currentuser):
                e=l[ph]["name"]
                f=l[ph]["address"]
                g=ph
                h=l[ph]["location"]
            else:
                messagebox.showerror("error","you can't send package to yourselves!")
        else:
            messagebox.showerror("error","Receiver isn't our user!")
            return
    else:
        messagebox.showerror("Error","Numbers aren't matching!")
        return
    writefile(a,b,c,d,e,f,g,h)

    
    
    
    

def track():
    next3 =Toplevel()
    next3.title("Tyson Service System")
    next3.geometry("925x500+300+200")
    next3.iconbitmap("bit.png")
    
    next3.config(bg="white")
    pages.Push(next3)
    
    Frame1 = Frame(next3,height=50,width = 925,bg="black",).place(x=0,y=0)
    Label(next3,text="Track Consignment",bg="black",fg="#57a1f8",font =("Microsoft YaHei UI Light",18,"bold")).place(x=10,y=5)
    #Button(next3,width=15,pady = 5,text="Admin",bg ="#57a1f8",fg = "black",border=3,command=info).place(x=800,y=10)

    Frame2 = Frame(next3,height=425,width =910,bg="white").place(x=5,y=60)

    image = PhotoImage(file ="cons.png")
    Label(next3,image = image).place(x=550,y=80)
    
    head=Label(next3,text="Track No",fg = "#57a1f8",bg="black",padx = 10,pady=2,font =("Microsoft YaHei UI Light",15,"bold"))
    head.place(x=56,y=91)

    num=Entry(next3,width = 20,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    num.place(x=175,y=91)
    
    
    Button(next3,width=39,pady = 5,border = 5,text="Track",bg ="#57a1f8",fg = "white",cursor ="hand2",command =lambda:tab3(num.get())).place(x=100,y=150)
    Button(next3,width=15,pady = 5,border = 5,text="Previous",bg ="#57a1f8",fg = "white",cursor ="hand2",command =navigatebefore).place(x=50,y=350)
    next3.mainloop()

def status(x,trackno,saddress,raddress,fcity,tocity):
    try:
        dt=date.today().strftime("%d/%m/%Y")
        f=open("data.json","r")
        g=open("temp.json","w")
        l=json.load(f)
        l[trackno]["status"]=x
        l[trackno]["date"]=dt
        g.write(json.dumps(l))
        g.close()
        f.close()
        os.remove("data.json")
        os.rename("temp.json","data.json")
        messagebox.showinfo("Status","Status Changed")
    except:
        messagebox.showerror("Status","Something Went Wrong")


def tab3(trackno):

    f=open("data.json",'r')
    try:
        l=json.load(f)
        Status=l[trackno]["status"]
        sname=l[trackno]["Sender name"]
        rname=l[trackno]["Receiver name"]
        saddress=l[trackno]["Sender address"]
        raddress=l[trackno]["Receiver address"]
        scontact=l[trackno]["Sender contact"]
        rcontact=l[trackno]["Receiver contact"]
        scity=l[trackno]["Sender city"]
        location = l[trackno]["location"]
    except:
        messagebox.showerror("Tracking","Tracking doesn't Exist")
        f.close()
        return
        
    if trackno == "":
        messagebox.showerror("Tracking","Please Enter the \n \n Track No")
        track()
    else:
        next4 =Toplevel()
        next4.attributes('-fullscreen', True)
        next4.title("Tyson Service System")
        next4.geometry("925x500+300+200")
        next4.iconbitmap("bit.png")
        next4.resizable(False,True)
        next4.config(bg="white")
        pages.Push(next4)
        

     
        Label(next4,text="Sender details",bg="white",fg="#57a1f8",font =("Microsoft YaHei UI Light",20,"bold")).place(x=380,y=0)

        Label(next4,text="Name",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=50)
        Label(next4,text=sname,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=50)
        
        Label(next4,text="Address",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=100)
        Label(next4,text=saddress,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=100)

        Label(next4,text="Contact",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=150)
        Label(next4,text=scontact,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=150)

        Label(next4,text="City",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=200)
        Label(next4,text=scity,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=200)

        Label(next4,text="Receiver details",bg="white",fg="#57a1f8",font =("Microsoft YaHei UI Light",20,"bold")).place(x=380,y=300)

        Label(next4,text="Name",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=350)
        Label(next4,text=rname,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=350)
        
        Label(next4,text="Address",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=400)
        Label(next4,text=raddress,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=400)
        
        Label(next4,text="Contact",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=450)
        Label(next4,text=rcontact,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=450)

        Label(next4,text="city",bg="#57a1f8",fg="black",width=10,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=50,y=500)
        Label(next4,text=location,bg="white",fg="black",pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold")).place(x=250,y=500)

        Label(next4,text="Status",bg="white",fg="#57a1f8",font =("Microsoft YaHei UI Light",20,"bold")).place(x=380,y=550)
        if Status=="delivered":
            colour="green"
        else:
            colour="red"
        lbl=Label(next4,text=Status,bg="white",fg=colour,pady=5,padx =30,font =("Microsoft YaHei UI Light",15,"bold"))
        lbl.place(x=320,y=600)
        
        Button(next4,width=40,pady=10,text="Previous",bg ="#57a1f8",fg = "white",border=0 ,command=navigatebefore).place(x=100,y=650)
        Button(next4,width=40,pady=10,text="set to delivered",bg ="#57a1f8",fg = "white",border=0 ,command=lambda:change(lbl,Status,trackno,scontact,rcontact,location)).place(x=350,y=650)

        """mscroll=Scrollbar(next4,orient="vertical",command= next4.yview)
        mscroll.pack(side="right",fill="y")
        next4.configure(yscrollcommand=mscroll.set)
        next4.bind("<Configure>",lambda e:next4.configure(scrollregion=next4.bbox("all")))
        #scroll=Scrollbar(next4)
        #scroll.pack(side=RIGHT,fill=Y)
        #scroll.set(next4)"""
        
def change(lbl,status,trackno,scontact,rcontact,location):
    
    if (status=="not delivered"):
        dt=date.today().strftime("%d/%m/%Y")
        f=open("data.json","r")
        g=open("temp.json","w")
        l=json.load(f)
        l[trackno]["status"]="delivered"
        l[trackno]["date"]=dt
        g.write(json.dumps(l))
        g.close()
        f.close()
        os.remove("data.json")
        os.rename("temp.json","data.json")
        
        lbl.config(text="delivered")
        lbl.config(fg="green")
    
        s1={"from":scontact,"to":rcontact,"trackno":trackno}
        s2={"from":scontact,"to":rcontact,"date of delivery":dt,"trackno":trackno}
        f=open("datewise.json","r")
        g=open("locationwise.json","r")
        h=open("temp1.json","w")
        i=open("temp2.json","w")
        try:
            d1=json.load(f)
        except:
            d1={}
        try:
            d2=json.load(g)
        except:
            d2={}
        if dt in d1.keys():
            d1[dt].append(s1)
        else:
            d1[dt]=[s1]

        if location.lower() in d2.keys():
            d2[location.lower()].append(s2)
        else:
            d2[location.lower()]=[s2]
   
        h.write(json.dumps(d1))
        i.write(json.dumps(d2))
        f.close()
        g.close()
        h.close()
        i.close()
        os.remove("datewise.json")
        os.remove("locationwise.json")
        os.rename("temp1.json","datewise.json")
        os.rename("temp2.json","locationwise.json")


def date_wise():
    next5 =Toplevel()
    next5.title("Tyson Service System")
    next5.geometry("925x500+300+200")
    next5.iconbitmap("bit.png")
    next5.resizable(False,False)
    next5.config(bg="white")
    pages.Push(next5)
    Frame1 = Frame(next5,height=50,width = 925,bg="black",).place(x=0,y=0)
    Label(next5,text="List of packages Date wise",bg="black",fg="#57a1f8",font =("Microsoft YaHei UI Light",18,"bold")).place(x=10,y=5)
    #Button(next5,width=15,pady = 5,text="Admin",bg ="#57a1f8",fg = "black",border=3,command=info).place(x=800,y=10)

    Frame2 = Frame(next5,height=425,width =910,bg="white").place(x=5,y=60)

    image = PhotoImage(file ="cons.png")
    Label(next5,image = image).place(x=550,y=80)

    head=Label(next5,text="Date",fg = "#57a1f8",bg="black",width =5,padx = 10,pady=2,font =("Microsoft YaHei UI Light",15,"bold"))
    head.place(x=100,y=91)

    date=Entry(next5,width = 20,bg ="white",fg ="black",font=("Microsoft YaHei UI Light",18))
    date.place(x=175,y=91)
    
    Button(next5,width=39,pady = 5,border = 5,text="Track",bg ="#57a1f8",fg = "white",cursor ="hand2",command =lambda:tab4(date.get())).place(x=100,y=150)
    Button(next5,width=15,pady = 5,border = 5,text="Previous",bg ="#57a1f8",fg = "white",cursor ="hand2",command =navigatebefore).place(x=50,y=350)
    next5.mainloop()


def tab4(dt):
    global pages
    # date wise list of customers
    next8 =Toplevel()
    next8.title("Tyson Service System")
    next8.attributes('-fullscreen', False)
    next8.geometry("925x500+300+200")
    next8.iconbitmap("bit.png")
    next8.resizable(0,0)
    next8.config(bg="white")
    pages.Push(next8)

    f=open("datewise.json","r")
    try:
        l=json.load(f)
        lst=l[dt]
    except:
        navigatebefore()
        messagebox.showerror("No records","No records present in the given date/ invalid date format")
        return
   
    printTable(next8,lst)
    f.close()
    pages.Push(next8)
    
    next8.mainloop()

def location_wise():
    next7 =Toplevel()
    next7.title("Tyson Service System")
    next7.geometry("925x500+300+200")
    next7.iconbitmap("bit.png")
    next7.resizable(False,False)
    next7.config(bg="white")

    pages.Push(next7)
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
    
    Button(next7,width=39,pady = 5,border = 5,text="Track",bg ="#57a1f8",fg = "white",cursor ="hand2",command =lambda:tab5(location.get())).place(x=100,y=150)
    Button(next7,pady = 5,width=15,border = 5,text="Previous",bg ="#57a1f8",fg = "white",cursor ="hand2",command =navigatebefore).place(x=50,y=350)
    next7.mainloop()

def tab5(loc):
    
    # location wise list of customers
    next6 =Toplevel()
    next6.title("Tyson Service System")
    next6.geometry("925x500+300+200")
    next6.iconbitmap("bit.png")
   
    next6.config(bg="white")
    pages.Push(next6)
    
    f=open("locationwise.json","r")
    try:
        l=json.load(f)
        lst=l[loc.lower()]
    except:
        navigatebefore()
        messagebox.showerror("No records","No records present in the given location")
        return

    printTable(next6,lst)
    #Button(next6,pady = 5,border = 5,width=15,text="Previous",bg ="#57a1f8",fg = "white",cursor ="hand2",command =navigatebefore).grid(row=0,column=0)
    next6.mainloop()

def sent():
    
    
    global currentuser
  
    f=open("userwise.json","r")
    g=open("data.json","r")
    try:
       d=json.load(f)
       lst=d[currentuser]["sent"]
       r=lst[0]
    except:
        #navigatebefore()
        messagebox.showinfo("title","no packages sent")
        return
        
    try:
        k=json.load(g)
    except:
        k={}


    temp=[]
    for i in lst:
        d={}
        d["track number"]=i
        d["From"]=currentuser
        d["To"]=k[str(i)]["Receiver contact"]
        d["status"]=k[str(i)]["status"]
        temp.append(d)
    f.close()
    g.close()
    next9 =Toplevel()
    next9.title("Tyson Service System")
    next9.geometry("925x500+300+200")
    next9.iconbitmap("bit.png")
    next9.config(bg="white")
    pages.Push(next9)

    printTable(next9,temp)
    next9.mainloop()

def received():
    global currentuser
    f=open("userwise.json","r")
    g=open("data.json","r")
    
    try:
       d=json.load(f)
       lst=d[currentuser]["received"]
       r=lst[0]
    except:
        #navigatebefore()
        messagebox.showinfo("title","no packages received")
        return
    try:
        k=json.load(g)
    except:
        k={}

    temp=[]
    for i in lst:
        d={}
        d["track number"]=i
        d["From"]=k[str(i)]["Sender contact"]
        d["To"]=currentuser
        d["status"]=k[str(i)]["status"]
        temp.append(d)
    f.close()
    g.close()
    next10 =Toplevel(bg="white")
    next10.title("Tyson Service System")
    next10.geometry("925x500+300+200")
    next10.iconbitmap("bit.png")
    next10.config(bg="white")
    pages.Push(next10)
    printTable(next10,temp)
    next10.mainloop()

def Help():


    next11 =Toplevel()
    next11.title("Tyson Service System")
    next11.geometry("925x500+300+200")
    next11.iconbitmap("bit.png")
    next11.resizable(False,False)
    next11.config(bg="white")
    pages.Push(next11)


    Frame1 = Frame(next11,height=50,width = 925,bg="black",).place(x=0,y=0)
    Label(next11,text="Help Centre",bg="black",fg="#57a1f8",font =("Microsoft YaHei UI Light",18,"bold")).place(x=10,y=5)
    #Button(next11,width=15,pady = 5,text="Admin",bg ="#57a1f8",fg = "black",border=3,command=info).place(x=800,y=10)

    Frame2 = Frame(next11,height=425,width =910,bg="white").place(x=5,y=60)

    #img = PhotoImage(file = "help.png")
    #Label(next11,image = image).place(x=400,y=50)

    Label(next11,text = "Status helps us to track the parcel by entering the tracking number Parcel Information helps us to check the deatails of the parcel DateWise List helps us to show the parcel delivered at entered location"
    ,bg="white",fg="black",font =("Microsoft YaHei UI Light",10,"bold")).place(x =20,y=50)
    Label(next11,text="Send a package used to send your delivery products by entering the receiver details",bg="white",fg="black",font =("Microsoft YaHei UI Light",10,"bold")).place(x=20,y=75)
    Label(next11,text="Packages sent by you gives the list of packages that you have sent from your specified ID",bg="white",fg="black",font =("Microsoft YaHei UI Light",10,"bold")).place(x=20,y=100)
    Label(next11,text="Packages yet to receive gives the list of packages that you will receive or already received",bg="white",fg="black",font =("Microsoft YaHei UI Light",10,"bold")).place(x=20,y=125)
    Label(next11,text="Update details let you to update the details of your account",bg="white",fg="black",font =("Microsoft YaHei UI Light",10,"bold")).place(x=20,y=150)
    Label(next11,text="Logout will let you to go out of the account that you have entered",bg="white",fg="black",font =("Microsoft YaHei UI Light",10,"bold")).place(x=20,y=175)
    Label(next11,text="track will allow you to track the parcel that you have sent or that you are going to receive",bg="white",fg="black",font =("Microsoft YaHei UI Light",10,"bold")).place(x=20,y=200)
    Button(next11,pady = 5,width=15,border = 5,text="Previous",bg ="#57a1f8",fg = "white",cursor ="hand2",command =navigatebefore).place(x=100,y=350) 

   


pages=stack()
root = Tk()
root.title("Parcel Sevice System")
root.geometry("925x500+300+200")
root.iconbitmap("bit.png")
root.configure(bg="#fff")
root.resizable(False,False)
pages.Push(root)

#image0 = PhotoImage(file="bty.png")
#Label(root,image=image0).pack()

image1 = PhotoImage(file="login.png")
image2= PhotoImage(file="truck.png")
Label(root,image = image1,bg = "white").place(x=50,y=50)

frame = Frame(root,width =350,height=350,bg="white")
frame.place(x=480,y=70)

head=Label(frame,text="Login",fg = "#57a1f8",bg="white",font =("Microsoft YaHei UI Light",23,"bold"))
head.place(x=100,y=5)


def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    Username = user.get()
    if Username =='':
        user.insert(0,"phone number/ID")


user = Entry(frame,width=25,fg= 'black',border=0,bg="white",font =("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"phone number/ID")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)


def on_enter(e):
    password.delete(0,"end")
    password.config(show='*')

def on_leave(e):
    Password = password.get()
    if Password =='':
        password.config(show='')
        password.insert(0,"Password")




password = Entry(frame,width=25,fg= 'black',border=0,bg="white",font =("Microsoft YaHei UI Light",11))
password.place(x=30,y=150)
password.insert(0,"Password")
password.bind("<FocusIn>",on_enter)
password.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)
currentuser="admin"


Button(frame,width=39,pady = 7,text="Login",bg ="#57a1f8",fg = "white",border=0,command = lambda:signin()).place(x=35,y=204)
label = Label(frame,text = "Don't have an Account..? ",fg="black",bg="white",font =("Microsoft YaHei UI Light",9))
label.place(x=75,y=270)

sign_up = Button(frame,width = 6,text ="Sign up",border=0,bg="white",cursor="hand2",fg ="#57a1f8",command=signup)
sign_up.place(x=215,y=270)

root.mainloop()