from tkinter import *
from bedavail import *
from oxygen import *
from covid_app import *
import mysql.connector



def bed_analysis():
    import matplotlib.pyplot as plt
    import numpy as np
    conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

    c=conn.cursor()
    
    c.execute("SELECT Name,Total,Vacant FROM beds_avail")
    x=[]
    ava=[]
    pre=[]


    for row in c.fetchall():
        x.append(row[0])
        ava.append(row[2])
        pre.append(row[1])
    

    w=0.4
    
    bar1 = np.arange(len(x))
    bar2 = [i+w for i in bar1]

    plt.bar(bar1,ava,w,label="available beds")
    plt.bar(bar2,pre,w,label="Total beds")

    plt.xlabel("COVID HOSPITALS")
    plt.ylabel("BEDS")
    plt.title("COVID BED AVAILABILITY")
    plt.xticks(bar1+w/2,x)
    plt.legend()
    plt.show()

def oxy_analysis():
    import matplotlib.pyplot as plt
    conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

    c=conn.cursor()
    c.execute("SELECT Name , Cyl_avail FROM oxy_suppliers")
    x=[]
    h=[]
    


    for row in c.fetchall():
        x.append(row[0])
        h.append(row[1])
        
    
    plt.bar(x,h,label="Available Cylinders")
    plt.xlabel("Suppliers")
    plt.ylabel("Cyliders Available")
    plt.show()

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



btn1=Button(window,text="Hospital Bed Availability",width=20,font='Calibri,10',bg='grey',
            command=lambda:[Bed()])

btn1.place(x=650,y=350)

btn2=Button(window,text="Oxygen Suppliers",width=20,font='Calibri,10',bg='grey',
            command=lambda:[Oxygen()])
btn2.place(x=650,y=420)

#btn3=Button(window,text="COVID LIVE CASES",width=20,font='Calibri,10',bg='grey')
#btn3.place(x=650,y=490)
#btn3.config(command=(Application))


btn4=Button(window,text="BED ANALYSIS",width=20,font='Calibri,10',bg='grey',command=bed_analysis)
btn4.place(x=650,y=490)

btn5=Button(window,text="OXYGEN ANALYSIS",width=20,font='Calibri,10',bg='grey',command=oxy_analysis)
btn5.place(x=650,y=560)


window.title('COVID EMERGENCY INFORMATION SYSTEM')
window.geometry("500x500")
window.mainloop()



