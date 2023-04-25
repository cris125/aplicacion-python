from tkinter import *
import os

from main import SumaVentas



from main import vistaDes

from main import vistaVentas

from main import vistaFecha
from main import ElimininarExistencias

def Cerrar():
    main.destroy()
def ventana22():
    global formulario
    global main
    main=Tk()
    main.title("Inventarios (Ventas)")
    main.geometry("780x340")
    main.resizable(0, 50)
    
    

    main.config(width=300, height=200,bg="#567599")
    
    
    carpetaP=os.path.dirname(__file__)
    carpetaimg=os.path.join(carpetaP,"Img")
    try:
        main.iconbitmap(os.path.join(carpetaimg,"logo (2).ico"))
    except:
        xd=""
    
    scroll=Scrollbar(main)
    c=Canvas(main,bg="white",yscrollcommand=scroll.set)
    scroll.config(command=c.yview)
    scroll.pack(side="right",fill="y")
    elframe=Frame(c)
    c.pack(side='top',fill="both",expand=True)
    c.create_window(0,0,window=elframe,anchor="nw")


    txt=Label(elframe,wraplength=500)
    txt.grid(column=0,row=0,columnspan=1,rowspan=2)
    txt.config(width=1,height=7,font=("Arial Bold",16),bg="white")


    txt=Label(elframe,wraplength=500,text="Fecha")
    txt.grid(column=1,row=0,columnspan=1)
    txt.config(width=10,font=("Arial Bold",16),fg="#83c240",bg="white")

    txt=Label(elframe,wraplength=500,text="Precio")
    txt.grid(column=2,row=0,columnspan=1)
    txt.config(width=10,font=("Arial Bold",16),fg="#75a147",bg="#d8f2bd")

    txt=Label(elframe,wraplength=500,text="Descripción")
    txt.grid(column=3,row=0,columnspan=1)
    txt.config(width=40,font=("Arial Bold",16),fg="#83c240",bg="white")

    txt1=Label(elframe,wraplength=500,text=vistaFecha())
    txt1.grid(column=1,row=1,columnspan=1 )
    txt1.config(width=10,font=("Arial Bold",16),fg="#75a147",bg="#d8f2bd")

    txt2=Label(elframe,wraplength=500,text=vistaVentas())
    txt2.grid(column=2,row=1,columnspan=1)
    txt2.config(width=10,font=("Arial Bold",16),fg="#83c240",bg="white")

    txt3=Label(elframe,wraplength=500,text=vistaDes())
    txt3.grid(column=3,row=1,columnspan=1)
    txt3.config(width=40,font=("Arial Bold",16),fg="#75a147",bg="#d8f2bd")

    suma=(SumaVentas())

    SumaE=Label(elframe,wraplength=500,text="$"+suma)
    SumaE.grid(column=2,row=3,columnspan=1)
    SumaE.config(width=13,font=("Arial Bold",14),fg="#75a147",bg="#d8f2bd")

    SumaV=Label(elframe,wraplength=500,text="Suma Ventas:")
    SumaV.grid(column=1,row=3,columnspan=1)
    SumaV.config(width=11,font=("Arial Bold",14),fg="#75a147",bg="#d8f2bd")


    botonVerVen=Button(elframe,text="Cerrar",command=Cerrar)
    botonVerVen.config(width=20,height=1,font=("Arial Bold",15))
    botonVerVen.config(fg="white",bg="dark green")
    botonVerVen.grid(column=3,row=3,columnspan=1 ,padx=1,pady=1)

    main.update()
    c.config(scrollregion=c.bbox("all"))

    main.mainloop()


