from tkinter import *
import mysql.connector
from tkinter import ttk
from Oxy_Admin import *
from Oxy_Notify import *

class Oxygen:
    def __init__(self):
            
        window3=Tk()

        l=Label(window3, text="OXYGEN SUPPLIERS", fg='white',
          bg='royal blue',height=3,width=138,font='Arial,50')
        lbl2=Label(window3, text="One stop for all Covid Emergency Services", fg='black',
          bg='light blue',height=2,width=138,font='Arial,50')
        lbl3=Label(window3, text="Please Wear Mask Properly And Help Fight COVID-19", fg='white',
          bg='royal blue',width=138,font='Arial,50')

        btn=Button(window3,text="Admin Login",width=10,font='Calibri,7',bg='grey',command=Oxy_Ad)
        btn.place(x=20,y=150)
        btn2=Button(window3,text="NOTIFY ME",width=10,font='Calibri,7',bg='grey',command=Oxy_Notify)
        btn2.place(x=1390,y=150)

        l.place(x=1,y=5)
        lbl2.place(x=1,y=90)
        lbl3.place(x=1,y=750)

        conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

        c=conn.cursor()

        c.execute("""SELECT * FROM oxy_suppliers""")
        
        tree=ttk.Treeview(window3)
        tree["show"]="headings"

        s=ttk.Style(window3)
        s.theme_use("alt")
        s.configure(".",font=("Helvetica",12))
        s.configure("Treeview.Heading",foreground="red",font=("Helvetica",12,"bold"))

        hsb=ttk.Scrollbar(window3,orient='horizontal')
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side=BOTTOM)

        tree["columns"]=("Name","Cylinders Available","Phone No","Address")

        tree.column("Name",anchor=CENTER)
        tree.column("Cylinders Available",anchor=CENTER)
        tree.column("Phone No",anchor=CENTER)
        tree.column("Address",anchor=CENTER)

        tree.heading("Name",text="Name",anchor=CENTER,)
        tree.heading("Cylinders Available",text="Cylinders Available",anchor=CENTER)
        tree.heading("Phone No",text="Phone No",anchor=CENTER)
        tree.heading("Address",text="Address",anchor=CENTER)

        i=0
        for ro in c:
          tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
          i=i+1

        tree.place(x=300,y=300)





        
        window3.geometry("500x500")
        window3.title('OXYGEN SUPPLIERS')
        window3.mainloop()
        