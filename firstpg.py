from tkinter import *
from bedavail import *
from oxygen import *

window=Tk()

lbl1=Label(window, text="COVID EMERGENCY INFORMATION SYSTEM", fg='white',
          bg='royal blue',height=3,width=138,font='Arial,50')

lbl2=Label(window, text="One stop for all Covid Emergency Services", fg='black',
          bg='light blue',height=2,width=138,font='Arial,50')

lbl3=Label(window, text="Please Wear Mask Properly And Help Fight COVID-19", fg='white',
          bg='royal blue',width=138,font='Arial,50')

lbl1.place(x=1,y=5)
lbl2.place(x=1,y=90)
lbl3.place(x=1,y=750) 

icon = PhotoImage(file="dp.png")
window.iconphoto(True,icon)

image=PhotoImage(file="dp2.png")
img=Label(window,image=image)
img.place(x=600,y=200)

btn1=Button(window,text="Hospital Bed Availability",width=20,font='Calibri,10',bg='grey',command=Bed)
btn1.place(x=650,y=350)

btn2=Button(window,text="Oxygen Suppliers",width=20,font='Calibri,10',bg='grey',command=Oxygen)
btn2.place(x=650,y=420)

btn3=Button(window,text="Essential Medicines",width=20,font='Calibri,10',bg='grey')
btn3.place(x=650,y=490)

btn4=Button(window,text="Vaccine Availability",width=20,font='Calibri,10',bg='grey')
btn4.place(x=650,y=560)

btn5=Button(window,text="HELP ME BOT",width=20,font='Calibri,10',bg='grey')
btn5.place(x=1250,y=650)



window.title('COVID EMERGENCY INFORMATION SYSTEM')
window.geometry("500x500")
window.mainloop()