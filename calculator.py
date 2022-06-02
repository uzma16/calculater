from tkinter import *
def click(event):
      global scvalue
      text=event.widget.cget("text")
      if text =="=":
           if scvalue.get().isdigit():
                value=int(scvalue.get())
           else:
                try:
                     value=eval(screen.get())
                except Exception as e:
                     scvalue.set("Error")
                     screen.update()


           scvalue.set(value)
           screen.update()

      elif text=="C":
        scvalue.set("")
        screen.update()

      else:
        scvalue.set(scvalue.get()+text)
        screen.update()

    


root=Tk()
root.geometry("644x900")
root.title("My calculator")
#root.wm_iconbitmap("1.ico")


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 50 bold")
screen.pack(fill=X,ipadx=10,padx=12,pady=12)

f=Frame(root,background="skyblue")

b=Button(f,text="9",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=15,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,background="skyblue")
b=Button(f,text="6",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=15,pady=10,font="lucida 30 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,background="skyblue")
b=Button(f,text="3",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="x",padx=15,pady=10,font="lucida 24 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,background="skyblue")
b=Button(f,text="0",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="00",padx=15,pady=10,font="lucida 25 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=15,pady=10,font="lucida 28 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,background="skyblue")
b=Button(f,text="C",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="000",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b=Button(f,text="log",padx=15,pady=10,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()