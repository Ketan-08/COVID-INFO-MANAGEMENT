from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox


class Bed_Notify:
    def __init__(self):
        def combo_input(self):
            conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

            c=conn.cursor()
            

            c.execute('SELECT Name from beds_avail')

            data = []

            for row in c.fetchall():
                data.append(row[0])

            return data
        w3=Tk()
        l=Label(w3, text="BED AVAILABILITY NOTIFICATION", fg='white',
          bg='royal blue',height=3,width=138,font='Arial,50')
        lbl2=Label(w3, text="One stop for all Covid Emergency Services", fg='black',
          bg='light blue',height=2,width=138,font='Arial,50')
        lbl3=Label(w3, text="Please Wear Mask Properly And Help Fight COVID-19", fg='white',
          bg='royal blue',width=138,font='Arial,50')
        lbl4=Label(w3,text="Select Hospital :",font=("Helvetica",18,"bold"))
        lbl5=Label(w3,text="Name :",font=("Helvetica",18,"bold"))
        lbl6=Label(w3,text="Email ID :",font=("Helvetica",18,"bold"))

        e1=Entry(w3,width=25,font=("Helvetica",20))
        e2=Entry(w3,width=25,font=("Helvetica",20))

        n=StringVar()
        cBox=ttk.Combobox(w3,width=40,textvariable=n,font=("Helvetica",15,"bold"))
        

        def Info():
            print("Hellooooo")

            conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

            c=conn.cursor()
            l=e2.get()
            m=e1.get()
            n=cBox.get()
            print(l,m,n)

            c.execute("""Insert into notify values (%s,%s,%s)""",(l,m,n))
            conn.commit()

            def Msg():
                 messagebox.showinfo("Notification", "You will be Successfully Notified!!!")
            Msg()

        b1=Button(w3,text="NOTIFY ME",width=10,font='Calibri,15',bg='YELLOW',command=Info)

       
        cBox['values']=combo_input(self)
        cBox['state'] = 'readonly'
        
    

        l.place(x=1,y=5)
        lbl2.place(x=1,y=90)
        lbl3.place(x=1,y=750)
        lbl4.place(x=200,y=170)
        lbl5.place(x=200,y=250)
        lbl6.place(x=200,y=330)
        cBox.place(x=400,y=170)
        e1.place(x=400,y=250)
        e2.place(x=400,y=330)
        b1.place(x=600,y=500)






        w3.title('BED AVAILABILITY NOTIFICATION')
        w3.geometry("500x500")
        w3.mainloop()




    
  

