from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox


class Oxy_Notify:
    def __init__(self):
        w4=Tk()
        l=Label(w4, text="OXYGEN CYLINDERS AVAILABILTY NOTIFICATION", fg='white',
          bg='royal blue',height=3,width=138,font='Arial,50')
        lbl2=Label(w4, text="One stop for all Covid Emergency Services", fg='black',
          bg='light blue',height=2,width=138,font='Arial,50')
        lbl3=Label(w4, text="Please Wear Mask Properly And Help Fight COVID-19", fg='white',
          bg='royal blue',width=138,font='Arial,50')
        lbl4=Label(w4,text="Select Oxygen Supplier :",font=("Helvetica",18,"bold"))
        lbl5=Label(w4,text="Name :",font=("Helvetica",18,"bold"))
        lbl6=Label(w4,text="Email ID :",font=("Helvetica",18,"bold"))

        e1=Entry(w4,width=25,font=("Helvetica",20))
        e2=Entry(w4,width=25,font=("Helvetica",20))

        b1=Button(w4,text="NOTIFY ME",width=10,font='Calibri,15',bg='YELLOW',command=Msg)
        
        n=StringVar()
        c=ttk.Combobox(w4,width=40,textvariable=n,font=("Helvetica",15,"bold"))
        c['values']=combo_input(self)
        c['state'] = 'readonly'
        

        
    

        l.place(x=1,y=5)
        lbl2.place(x=1,y=90)
        lbl3.place(x=1,y=750)
        lbl4.place(x=200,y=170)
        lbl5.place(x=300,y=250)
        lbl6.place(x=300,y=330)
        c.place(x=500,y=170)
        e1.place(x=500,y=250)
        e2.place(x=500,y=330)
        b1.place(x=600,y=500)






        w4.title('OXYGEN CYLINDERS AVAILABILTY NOTIFICATION')
        w4.geometry("500x500")
        w4.mainloop()


def combo_input(self):
            conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

            c=conn.cursor()
            

            c.execute('SELECT Name from oxy_suppliers')

            data = []

            for row in c.fetchall():
                data.append(row[0])

            return data

def Msg():
  messagebox.showinfo("Notification", "You will be Successfully Notified!!!")
  
