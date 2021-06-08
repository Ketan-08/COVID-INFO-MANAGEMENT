from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from smtplib import *
from Bed_Notify import *

class Update_Bed:
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
        w5=Tk()
        l=Label(w5, text="UPDATE BEDS", fg='white',
          bg='royal blue',height=3,width=138,font='Arial,50')
        lbl2=Label(w5, text="One stop for all Covid Emergency Services", fg='black',
          bg='light blue',height=2,width=138,font='Arial,50')
        lbl3=Label(w5, text="Please Wear Mask Properly And Help Fight COVID-19", fg='white',
          bg='royal blue',width=138,font='Arial,50')
        lbl4=Label(w5,text="Select Hospital :",font=("Helvetica",18,"bold"))
        lbl5=Label(w5,text="Total Beds :",font=("Helvetica",18,"bold"))
        lbl6=Label(w5,text="Vacant Beds :",font=("Helvetica",18,"bold"))

        e1=Entry(w5,width=25,font=("Helvetica",20))
        e2=Entry(w5,width=25,font=("Helvetica",20))

        n=StringVar()
        cBox=ttk.Combobox(w5,width=40,textvariable=n,font=("Helvetica",15,"bold"))

        def Info():
            conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

            c=conn.cursor()
            x=e1.get()
            y=e2.get()
            z=cBox.get()
            print(x,y,z)

            c.execute("""UPDATE beds_avail SET Total= %s,Vacant=%s WHERE Name=%s"""
                       ,(x,y,z))
            conn.commit()
            
            Vacant=y
            Name=z

            if  Vacant!=0:
              c.execute("SELECT email_id FROM notify WHERE Hospital=%s",[Name])
              li = c.fetchall()

              if li:
                subject = "COVID 19 mini Project"
                body = f'{Vacant} beds are available in {Name}'

                msg = f'Subject : {subject}\n\n{body}'

                for dest in li:
                    s = SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login("covid19miniproject@gmail.com","Covid19_@#")
                    s.sendmail("covid19miniproject@gmail.com", dest, msg)
                    s.quit()

            

            def Msg():
              messagebox.showinfo("Updation", "You have Successfully Updated the Information!!!")
            Msg()

        b1=Button(w5,text="UPDATE",width=10,font='Calibri,15',bg='MAROON',command=Info)
        
        
        cBox['values']=combo_input(self)
        cBox['state'] = 'readonly'
        
        
        
        
        l.place(x=1,y=5)
        lbl2.place(x=1,y=90)
        lbl3.place(x=1,y=750)
        lbl4.place(x=200,y=170)
        lbl5.place(x=300,y=250)
        lbl6.place(x=300,y=330)
        e1.place(x=500,y=250)
        e2.place(x=500,y=330)
        cBox.place(x=500,y=170)
        b1.place(x=600,y=500)





        w5.title('UPDATE BEDS')
        w5.geometry("500x500")
        w5.mainloop()

        

        
        