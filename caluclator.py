from tkinter import *


def click(event) :
  text=event.widget.cget("text")
  print(text)
  if text == "=" :
      if a.get().isdigit() :
          value=int(a.get())
      else :
          value= eval(screen.get())
      a.set(value) 
      screen.update()   
  elif text == "C"  :    
         a.set("")
         screen.update()
  else :
    a.set(a.get()+text)
    screen.update()      
         
          
shiva=Tk()       
a=StringVar()
a.set("")
shiva.geometry("644x434")
shiva.title("sky caluclator")
screen=Entry(shiva,textvar=a,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f=Frame(shiva,bg="blue")
b=Button(f,text="7",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="9",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(shiva,bg="blue")
b=Button(f,text="4",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="6",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()
f=Frame(shiva,bg="blue")
b=Button(f,text="1",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="3",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(shiva,bg="blue")
b=Button(f,text="0",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(shiva,bg="blue")
b=Button(f,text="C",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=".",padx=10,pady=5,font="lucida 35 bold ")
b.pack(side=LEFT,padx=18,pady=5)
b.pack
b.bind("<Button-1>",click)
b=Button(f,text="00",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(shiva,bg="blue")
b=Button(f,text="+",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=10,pady=5,font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()

shiva.mainloop()


