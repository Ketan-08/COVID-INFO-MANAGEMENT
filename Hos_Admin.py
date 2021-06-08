from tkinter import *
import mysql.connector
from tkinter import ttk
from Update_Bed import *




class Admin:
    
    def __init__(self):
        w1=Tk()
        l=Label(w1, text="HOSPITAL BED AVAILABILITY - ADMIN", fg='white',
          bg='royal blue',height=3,width=138,font='Arial,50')
        lbl2=Label(w1, text="One stop for all Covid Emergency Services", fg='black',
          bg='light blue',height=2,width=138,font='Arial,50')
        lbl3=Label(w1, text="Please Wear Mask Properly And Help Fight COVID-19", fg='white',
          bg='royal blue',width=138,font='Arial,50')
        lbl4=Label(w1,text="ADMIN ID :",font=("Helvetica",18,"bold"))
        lbl5=Label(w1,text="PASSWORD :",font=("Helvetica",18,"bold"))

        self.e1=Entry(w1,width=25,font=("Helvetica",20,"bold"))
        self.e2=Entry(w1,width=25,font=("Helvetica",20,"bold"))       
        self.e2.config(show="*")

        

        def Check(x,y):
               
                conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

                c=conn.cursor()
                c.execute("""SELECT * FROM admin where ID=%s and Password=%s""",(x,y))
                record=c.fetchall()
                print(record)


                if not record:
                  messagebox.showerror("Error","Incorrect ID or Password!!!")
                else:
                  Update_Bed()
                  
  
        b1=Button(w1,text="LOGIN",width=10,font='Calibri,15',bg='GREEN',
        command=lambda:[Check(self.e1.get(),self.e2.get())])
        
        
        l.place(x=1,y=5)
        lbl2.place(x=1,y=90)
        lbl3.place(x=1,y=750)
        lbl4.place(x=400,y=300)
        lbl5.place(x=390,y=400)
        self.e1.place(x=570,y=300)
        self.e2.place(x=570,y=400)
        b1.place(x=700,y=550)

       
       

        w1.title('HOSPITAL BED AVAILABILITY-ADMIN')
        w1.geometry("500x500")
        
        w1.mainloop() 
          
        
      

    
                
               
        
                

               
                  

         
          


