
from tkinter import *
import os

from main import resetear

from ventanaVentas import ventana22
from main import ElimininarExistencias

from main import AgregarExistencias
from main import LeerEx
from main import LeerEx2
from main import LeerVentas
from main import NuevaVenta


import sys

def ventana1():
    global TxtExiss
    global varAu
    global varMemo
    global ventana
    global varMemoex
    global varAuex
    global Cable
    global Cargador
    global TxtExiss1
    global imagen
    global carpetaP
    global carpetaimg
     
    Cable="Cable"
    Cargador="Cargador"

    ventana=Tk()
    ventana.title("Inventarios")
    ventana.geometry("840x450")
    ventana.resizable(0,0)


    carpetaP=os.path.dirname(__file__)
    carpetaimg=os.path.join(carpetaP,"Img")
    
    ventana.config(width=300, height=200,bg="#567599")

   
    try:
        ventana.iconbitmap(os.path.join(carpetaimg,"logo (2).ico"))
        imagen=PhotoImage(file=(os.path.join(carpetaimg,"fondo.png")))  
        Ibl_img=Label(ventana,image=imagen)
        Ibl_img.grid(column=0,row=0,columnspan=11,rowspan=13)


        Ibl11=Label(ventana)
        Ibl11.grid(column=0,row=10)
        Ibl3=Label(ventana)
        Ibl3.grid(column=9,row=11)
    except:
        Ibl_img=Label(ventana)
        Ibl_img.grid(column=0,row=0,columnspan=11,rowspan=13)
        Ibl11=Label(ventana)
        Ibl11.grid(column=0,row=10)
        Ibl3=Label(ventana)
        Ibl3.grid(column=9,row=11)
    TxtVenta = Label(ventana,text= "Vender ",width=15,height=1,font=("Arial Bold",20))
    TxtVenta.config(fg="white",bg="#83c240")
    TxtVenta.grid(column=1,row=0,columnspan=2 ,padx=10,pady=10)

    TxtExis = Label(ventana,text= "Existencias",width=10,height=1,font=("Arial Bold",24))
    TxtExis.grid(column=3,row=0,columnspan=2 ,padx=10,pady=10)
    TxtExis.config(fg="white",bg="#83c240")

    TxtExis = Label(ventana,text= "Modificar Existencias",width=18,height=1,font=("Arial Bold",20))
    TxtExis.grid(column=1,row=5,columnspan=2 ,padx=10,pady=10)
    TxtExis.config(fg="white",bg="#83c240")

    ExisternciaNum=LeerEx()
    Existerncia=LeerEx2()
    TxtExi = Label(ventana,text= "Cantidad" ,width=7,height=1,font=("Arial Bold",17),anchor="e")
    TxtExi.grid(column=3,row=2,columnspan=1,rowspan=1 ,padx=0,pady=0)
    TxtExi.config(fg="white",bg="#83c240")

    TxtExi = Label(ventana,text= "Descripción" ,width=20,height=1,font=("Arial Bold",17),anchor="center")
    TxtExi.grid(column=4,row=2,columnspan=1,rowspan=1,padx=0,pady=0 )
    TxtExi.config(fg="white",bg="#83c240")

    TxtExiss = Label(ventana,text= ExisternciaNum ,width=7,height=9,font=("Arial Bold",17),anchor="e")
    TxtExiss.grid(column=3,row=2,columnspan=1,rowspan=8 ,padx=0,pady=0)
    TxtExiss.config(fg="#6a9140",bg="#e9f0e9")

    TxtExiss1 = Label(ventana,text= Existerncia ,width=26,height=9,font=("Arial Bold",17),anchor="w")
    TxtExiss1.grid(column=4,row=2,columnspan=1,rowspan=8 ,padx=0,pady=0)
    TxtExiss1.config(fg="#6a9140",bg="#e9f0e9")

    

    varAu=StringVar(ventana)
    varAu.set("Audifonos")
    obcionesAu=["Audifono cable ","Audifonos Inalambricos Diadema","Audifonos Inalambricos"]
    
    varAuex=StringVar(ventana)
    varAuex.set("Audifonos")
    obcionesAuex=["Audifono cable ","Audifonos Inalambricos Diadema","Audifonos Inalambricos"]
    
    varMemo=StringVar(ventana)
    varMemo.set("Memorias")
    obcionesMemo=["Memoria 8 Gb","Memoria 32 Gb","Memoria 16 Gb "]

    varMemoex=StringVar(ventana)
    varMemoex.set("Memorias")
    obcionesMemoex=["Memoria 8 Gb","Memoria 32 Gb","Memoria 16 Gb "]

    opcionAudi=OptionMenu(ventana,varAu,*obcionesAu)
    opcionAudi.config(width=12,font=("Arial Bold",14))
    opcionAudi.config(fg="#83c240",bg="white")
    opcionAudi.grid(column=1,row=2,columnspan=1 ,padx=5,pady=5)

    opcionMemo=OptionMenu(ventana,varMemo,*obcionesMemo)
    opcionMemo.config(width=12,font=("Arial Bold",14))
    opcionMemo.config(fg="#83c240",bg="white")
    opcionMemo.grid(column=2,row=2,columnspan=1 ,padx=5,pady=5)

    botonCargador=Button(ventana,text="Cargador",command=EliExCar)
    botonCargador.config(width=15,font=("Arial Bold",14))
    botonCargador.config(fg="#83c240",bg="white")
    botonCargador.grid(column=1,row=3,columnspan=1 ,padx=5,pady=5)

    botonCable=Button(ventana,text="Cable",command=EliExCab)
    botonCable.config(width=15,font=("Arial Bold",14))
    botonCable.config(fg="#83c240",bg="white")
    botonCable.grid(column=2,row=3,columnspan=1 ,padx=5,pady=5)

    botonAceptarV=Button(ventana,text="Aceptar Venta",command=VenderEx)
    botonAceptarV.config(width=20,height=1,font=("Arial Bold",18))
    botonAceptarV.config(fg="white",bg="#ccc056")
    botonAceptarV.grid(column=1,row=4,columnspan=2 ,padx=5,pady=5)

    
    opcionAudiex=OptionMenu(ventana,varAuex,*obcionesAuex)
    opcionAudiex.config(width=12,font=("Arial Bold",14))
    opcionAudiex.config(fg="#83c240",bg="white")
    opcionAudiex.grid(column=1,row=6,columnspan=1 ,padx=5,pady=5)

    opcionMemoex=OptionMenu(ventana,varMemoex,*obcionesMemoex)
    opcionMemoex.config(width=12,font=("Arial Bold",14))
    opcionMemoex.config(fg="#83c240",bg="white")
    opcionMemoex.grid(column=2,row=6,columnspan=1 ,padx=5,pady=5)

    botonCargadorex=Button(ventana,text="Cargador",command=agregarExCar)
    botonCargadorex.config(width=15,font=("Arial Bold",14))
    botonCargadorex.config(fg="#83c240",bg="white")
    botonCargadorex.grid(column=1,row=7,columnspan=1 ,padx=5,pady=5)

    botonCableex=Button(ventana,text="Cable",command=agregarExCab)
    botonCableex.config(width=15,font=("Arial Bold",14))
    botonCableex.config(fg="#83c240",bg="white")
    botonCableex.grid(column=2,row=7,columnspan=1 ,padx=5,pady=5)
    
    botonAceptarex=Button(ventana,text="Aceptar Existencia",command=Agregarex)
    botonAceptarex.config(width=20,height=1,font=("Arial Bold",17))
    botonAceptarex.config(fg="white",bg="#ccc056")
    botonAceptarex.grid(column=1,row=8,columnspan=2 ,padx=5,pady=5)
    
    botonVerVen=Button(ventana,text="Ver ventas",command=ventana22)
    botonVerVen.config(width=20,height=1,font=("Arial Bold",15))
    botonVerVen.config(fg="white",bg="#ccc056")
    botonVerVen.grid(column=4,row=8,columnspan=1 ,padx=5,pady=5)

    boton=Button(ventana,text="Resetear",command=resetear)
    boton.config(width=8,height=1,font=("Arial Bold",15))
    boton.config(fg="white",bg="#ccc056")
    boton.grid(column=3,row=8,columnspan=1 ,padx=5,pady=5)

    
    ventana.mainloop()
def ventana2ex():
    global formulario
    global main
    global xdd
    
    
    main=Tk()
    main.title("Inventarios")
    main.geometry("350x340")
    main.resizable(0,0) 

    main.config(width=300, height=200,bg="white")
    if xdd=="Audifonos Inalambricos Diadema":
        tex="Audifonos \n Inalambricos Diadema"
    else:
        tex=xdd

    try:
        main.iconbitmap(os.path.join(carpetaimg,"logo (2).ico"))
    except:
        none=none    
    label3 = Label(main,text= "Cantidad de \n"+tex,width=18,height=3,font=("Arial Bold",18))
    label3.grid(column=0,row=0,columnspan=2,rowspan=1 ,padx=10,pady=10)
    label3.config(fg="white",bg="#83c240")

    label3 = Label(main,text= "Cantidad de \n "+tex,width=18,height=3,font=("Arial Bold",13))
    label3.grid(column=0,row=1,columnspan=1,rowspan=1 ,padx=10,pady=10)
    label3.config(fg="white",bg="#83c240")

    formulario= Entry(main,width=8,font=("Arial Bold",25))
    formulario.grid(column=1,row=1,columnspan=1, padx=5,pady=5,)
    formulario.config(bg="white",border=2,fg="dark green")

    boton2 = Button(main,text="Aceptar ",width=25,height=1,command=agregarEx,font=("Arial Bold",15))
    boton2.grid(column=0,row=2,columnspan=3, padx=5,pady=5)
    boton2.config(bg="#ccc056",border=2,fg="white")
    main.mainloop()
def Agregarex():
    global xdd
    if varAuex.get() != "Audifonos": 
        xdd=str(varAuex.get())
        ventana2ex()
    elif varMemoex.get() != "Memorias":
        xdd=str(varMemoex.get())
        ventana2ex()
    elif Cargador != "Cargador":
        xdd="Cargador"
        ventana2ex()
    elif Cable != "Cable":
        xdd="Cable"
        ventana2ex()

def agregarEx():
    global Cable
    global Cargador
    nu=0
    tex=""
    tex=(str(formulario.get())).replace(" ","")
    try:
        nu=int(tex)
    except:
        tex="0"
    AgregarExistencias(tex,xdd) 
    TxtExiss.config(text=LeerEx())
    TxtExiss1.config(text=LeerEx2())
    varMemoex.set("Memorias")
    varAuex.set("Audifonos")
    Cable="Cable"
    Cargador="Cargador"
    main.destroy()

def agregarExCab():
    global Cable
    Cable=""
    Agregarex()
def agregarExCar():
    global Cargador
    Cargador=""
    Agregarex()


def EliExCab():
    global Cable
    Cable=""
    VenderEx()   
def EliExCar():
    global Cargador
    Cargador=""
    VenderEx()

def ventana2():
    global formulario
    global main
    global xdd
    main=Tk()
    main.title("Inventarios")
    main.geometry("350x340")
    main.resizable(0,0) 
    
    tex=""
    if xdd=="Audifonos Inalambricos Diadema":
        tex="Audifonos \n Inalambricos Diadema"
    else:
        tex=xdd

    main.config(width=300, height=200,bg="#567599")

    try:
        main.iconbitmap(os.path.join(carpetaimg,"logo (2).ico"))
    except:
        none=none

    label3 = Label(main,text= "Cantidad de \n "+tex,width=18,height=3,font=("Arial Bold",18))
    label3.grid(column=0,row=0,columnspan=2,rowspan=1 ,padx=10,pady=10)
    label3.config(fg="white",bg="#83c240")

    label3 = Label(main,text= "Valor venta \n "+tex,width=18,height=3,font=("Arial Bold",13))
    label3.grid(column=0,row=1,columnspan=1,rowspan=1 ,padx=10,pady=10)
    label3.config(fg="white",bg="#83c240")

    formulario= Entry(main,width=8,font=("Arial Bold",25))
    formulario.grid(column=1,row=1,columnspan=1, padx=5,pady=5,)
    formulario.config(bg="white",border=2,fg="dark green")

    boton2 = Button(main,text="Aceptar ",width=25,height=1,command=eliminarex,font=("Arial Bold",15))
    boton2.grid(column=0,row=2,columnspan=2, padx=5,pady=5)
    boton2.config(bg="#ccc056",border=2,fg="white")
    
def VenderEx():
    
    global formulario
    global main
    global xdd
    if varAu.get() != "Audifonos": 
        xdd=str(varAu.get())
        ventana2()
    elif varMemo.get() != "Memorias":
        xdd=str(varMemo.get())
        ventana2()
    elif Cargador != "Cargador":
        xdd="Cargador"
        ventana2()
    elif Cable != "Cable":
        xdd="Cable"
        ventana2()
   

def eliminarex():
    global Cable
    global Cargador
    nu=0
    tex=""
    tex=(str(formulario.get())).replace(" ","")
    try:
        nu=int(tex)
    except:
        tex="0"
    NuevaVenta(tex,xdd)
    TxtExiss.config(text=LeerEx())
    TxtExiss1.config(text=LeerEx2())
    varMemoex.set("Memorias")
    varAuex.set("Audifonos")
    varMemo.set("Memorias")
    varAu.set("Audifonos")
    Cable="Cable"
    Cargador="Cargador"
    main.destroy()


ventana1()