from tkinter import *
import mysql.connector
from tkinter import ttk
from Hos_Admin import *
from Bed_Notify import *


class Bed:
    def __init__(self):
        window2=Tk()

        l=Label(window2, text="HOSPITAL BED AVAILABILITY", fg='white',
          bg='royal blue',height=3,width=138,font='Arial,50')
        lbl2=Label(window2, text="One stop for all Covid Emergency Services", fg='black',
          bg='light blue',height=2,width=138,font='Arial,50')
        lbl3=Label(window2, text="Please Wear Mask Properly And Help Fight COVID-19", fg='white',
          bg='royal blue',width=138,font='Arial,50')

        btn=Button(window2,text="Admin Login",width=10,font='Calibri,7',bg='grey',command=Admin)
        btn.place(x=20,y=150)
        btn2=Button(window2,text="NOTIFY ME",width=10,font='Calibri,7',bg='grey',command=Bed_Notify)
        btn2.place(x=1390,y=150)
          
        l.place(x=1,y=5)
        lbl2.place(x=1,y=90)
        lbl3.place(x=1,y=750)
        

        conn=mysql.connector.connect(host='localhost',username='root',
                         password='',database='covid info management')

        c=conn.cursor()

        c.execute("""SELECT * FROM Hos_bed""")
        
        tree=ttk.Treeview(window2)
        tree["show"]="headings"

        s=ttk.Style(window2)
        s.theme_use("alt")
        s.configure(".",font=("Helvetica",12))
        s.configure("Treeview.Heading",foreground="red",font=("Helvetica",12,"bold"))

        hsb=ttk.Scrollbar(window2,orient='horizontal')
        hsb.configure(command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side=BOTTOM)

        tree["columns"]=("Name","Total Beds","Vacant Beds","Phone No","Address")

        tree.column("Name",anchor=CENTER)
        tree.column("Total Beds",anchor=CENTER)
        tree.column("Vacant Beds",anchor=CENTER)
        tree.column("Phone No",anchor=CENTER)
        tree.column("Address",anchor=CENTER)

        tree.heading("Name",text="Name",anchor=CENTER,)
        tree.heading("Total Beds",text="Total Beds",anchor=CENTER)
        tree.heading("Vacant Beds",text="Vacant Beds",anchor=CENTER)
        tree.heading("Phone No",text="Phone No",anchor=CENTER)
        tree.heading("Address",text="Address",anchor=CENTER)

        i=0
        for ro in c:
          tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
          i=i+1

        tree.place(x=300,y=300)





        window2.geometry("500x500")
        window2.title('HOSPITAL BED AVAILABILITY')
        window2.mainloop()








