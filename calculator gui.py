from tkinter import*
root=Tk()
root.configure(bg="#636e72")

label1=Label(root,text="CALCULATOR",font=("Time bold",20),bg="#636e72",fg="black")
label1.grid(row=0,columnspan=8)

eq=""
equation=StringVar()

textbox=Entry(root,font=("Times bold",15),bg="white",fg="black",width=20,justify="right",textvariable=equation)
textbox.grid(row=2,columnspan=100,sticky=E,ipadx=10,ipady=10,padx=50,pady=20)


def btnclick(num):
    global eq
    eq=eq+str(num)
    equation.set(eq)
def result():
    global eq
    total=str(eval(eq))
    equation.set(total)
    eq=""
def clear():
    global eq
    eq=""
    equation.set("")


button1=Button(root,text="1",font=("Times bold",12),command=lambda:btnclick(1),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button1.grid(row=3,column=1,padx=10,pady=10)
button2=Button(root,text="2",font=("Times bold",12),command=lambda:btnclick(2),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button2.grid(row=3,column=2,padx=10,pady=10)
button3=Button(root,text="3",font=("Times bold",12),command=lambda:btnclick(3),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button3.grid(row=3,column=3,padx=10,pady=10)
button4=Button(root,text="4",font=("Times bold",12),command=lambda:btnclick(4),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button4.grid(row=4,column=1,padx=10,pady=10)
button5=Button(root,text="5",font=("Times bold",12),command=lambda:btnclick(5),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button5.grid(row=4,column=2,padx=10,pady=10)
button6=Button(root,text="6",font=("Times bold",12),command=lambda:btnclick(6),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button6.grid(row=4,column=3,padx=10,pady=10)
button7=Button(root,text="7",font=("Times bold",12),command=lambda:btnclick(7),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button7.grid(row=5,column=1,padx=10,pady=10)
button8=Button(root,text="8",font=("Times bold",12),command=lambda:btnclick(8),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button8.grid(row=5,column=2,padx=10,pady=10)
button9=Button(root,text="9",font=("Times bold",12),command=lambda:btnclick(9),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button9.grid(row=5,column=3,padx=10,pady=10)
button0=Button(root,text="0",font=("Times bold",12),command=lambda:btnclick(0),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
button0.grid(row=6,column=2,padx=10,pady=10)

add=Button(root,text="+",font=("Times bold",12),command=lambda:btnclick("+"),borderwidth=1,relief=SOLID,height=2,width=8,fg="black",bg="#b2bec3")
add.grid(row=3,column=4,padx=10,pady=10)
sub=Button(root,text="-",font=("Times bold",12),command=lambda:btnclick("-"),borderwidth=1,relief=SOLID,height=2,width=8,fg="black",bg="#b2bec3")
sub.grid(row=4,column=4,padx=10,pady=10)
mul=Button(root,text="x",font=("Times bold",12),command=lambda:btnclick("*"),borderwidth=1,relief=SOLID,height=2,width=8,fg="black",bg="#b2bec3")
mul.grid(row=5,column=4,padx=10,pady=10)
div=Button(root,text="/",font=("Times bold",12),command=lambda:btnclick("/"),borderwidth=1,relief=SOLID,height=2,width=8,fg="black",bg="#b2bec3")
div.grid(row=6,column=4,padx=10,pady=10)

equal=Button(root,text="=",font=("Times bold",12),command=result,borderwidth=1,relief=SOLID,height=2,width=8,fg="black",bg="#b2bec3")
equal.grid(row=6,column=3,padx=10,pady=10)

dot=Button(root,text=".",font=("Times bold",12),command=lambda:btnclick("."),borderwidth=1,relief=SOLID,height=2,width=8,fg="white",bg="black")
dot.grid(row=6,column=1,padx=10,pady=10)
clear=Button(root,text="C",font=("Times bold",12),command=clear,borderwidth=1,relief=SOLID,height=2,width=8,fg="black",bg="#b2bec3")
clear.grid(row=2,column=1,padx=10,pady=10)

root.mainloop()

