import datetime
from os import remove
import sys
def Fecha():
    hora_actual = str(datetime.datetime.now())
    hora=""
    Con=0
    for i in hora_actual:
        Con=Con+1  
        if(Con<11):
            hora= hora + i 
    return(hora)      
           
"""print(Fecha())"""


    

def LeerVentas(lugar):
    try:
        archivo = open(lugar,"r",encoding="utf-8")
        texto = archivo.readlines()
    except:
        archivo = open(lugar,"w",encoding="utf-8")
        archivo.write("")
        archivo.close()
        archivo = open(lugar,"r",encoding="utf-8")
        texto = archivo.readlines()
    Texto=""
    for i in texto:
        Texto=Texto+i
      
    return(Texto)

"""print(LeerVentas("Audifonos.txt"))"""

def SumaVentas():
    try:
        archivo = open("VistaVentas.txt","r",encoding="utf-8")

    except:
        archivo = open("VistaVentas.txt","w",encoding="utf-8")
        archivo.write("")
        archivo.close()
        archivo = open("VistaVentas.txt","r",encoding="utf-8")
    texto = archivo.readlines()
    Suma=0
    for i in texto:
        i=i.split()
        if len(i)>3:
            Suma=Suma+int(i[1])
    
    return(str(Suma))

print(SumaVentas())





def AgregarExistencias(Existencia,tipo):
    try:
        archivo = open("Existencias.txt","r",encoding="utf-8")
    except:
        archivo = open("Existencias.txt","w",encoding="utf-8")
        archivo.write("0 Memoria 16 Gb \n0 Memoria 32 Gb \n0 Memoria 8 Gb \n0 Cable \n0 Cargador \n0 Audifono cable \n0 Audifonos Inalambricos Diadema \n0 Audifonos Inalambricos")
        archivo = open("Existencias.txt","r",encoding="utf-8")
    texto1 = archivo.readlines()
    con=0
    texto=""
    for i in texto1:
        if tipo in (i):
            texto=texto+Existencia+" "+tipo+"\n"
        else:
            texto=texto+i+"\n"
        archivo.close()
        archivo = open("Existencias.txt","w",encoding="utf-8")
        archivo.write("")
        archivo.write(texto)
        archivo.close()    
"""AgregarExistencias("60","Cable")  """


def ElimininarExistencias(tipo):
    try:
        archivo = open("Existencias.txt","r",encoding="utf-8")
    except:
        archivo = open("Existencias.txt","a",encoding="utf-8")
        archivo.write("0 Memoria 16 Gb \n0 Memoria 32 Gb \n0 Memoria 8 Gb \n0 Cable \n0 Cargador \n0 Audifono cable \n0 Audifonos Inalambricos Diadema \n0 Audifonos Inalambricos")
        archivo = open("Existencias.txt","r",encoding="utf-8")
    texto1 = archivo.readlines()
    texto=""
    for i in texto1:
        
        if tipo in (i):
            a=i.split()
            a=int(a[0])
            texto=texto+(str(a-1))+" "+tipo+"\n"
        else:
            texto=texto+i
        archivo.close()
        archivo = open("Existencias.txt","w",encoding="utf-8")
        archivo.write(texto)
        archivo.close()    

"""ElimininarExistencias("Cable")  """
def NuevaVenta(valor,Descri):
    if Descri == "Memoria 16 Gb" or Descri == "Memoria 32 Gb" or Descri == "Memoria 8 Gb":
        lugar="Memorias.txt"
    elif Descri == "Cable":
        lugar="Cables.txt"
    elif Descri== "Cargador":
        lugar = "Cargadores.txt"
    elif Descri == "Audifonos Inalambricos Diadema" or Descri == "Audifonos Inalambricos" or Descri == "Audifono cable":
        lugar = "Audifonos.txt"
    archivo = open(lugar,"a",encoding="utf-8")
    archivo2 = open("Vistaventas.txt","a",encoding="utf-8")
    
    if lugar == "Cargadores.txt":
        archivo.write((Fecha())+" "+valor +" de Cargador \n")
        archivo2.write((Fecha())+" "+valor +" de Cargador \n")
        archivo.close()
        archivo2.close()
        ElimininarExistencias(Descri)
        return((Fecha())+" "+valor +" de Cargador "+"\n")
    elif lugar == "Cables.txt":
        archivo.write((Fecha())+" "+valor +" de Cable \n ")
        archivo2.write((Fecha())+" "+valor +" de Cable \n")
        archivo.close()
        archivo2.close()
        ElimininarExistencias(Descri)
        return((Fecha())+" "+valor +" de Cable "+"\n")
    elif lugar == "Audifonos.txt":
        archivo.write((Fecha())+" "+valor +" de Audifono "+Descri+"\n")
        archivo2.write((Fecha())+" "+valor +" de Audifono "+Descri+"\n")
        archivo.close()
        archivo2.close()
        ElimininarExistencias(Descri)
        return((Fecha())+" "+valor +" de Audifono "+Descri+"\n")
    elif lugar == "Memorias.txt":
        archivo.write((Fecha())+" "+valor +" de Memoria "+Descri+"\n")
        archivo2.write((Fecha())+" "+valor +" de Memoria "+Descri+"\n")
        archivo.close()
        archivo2.close()
        ElimininarExistencias(Descri)
        return((Fecha())+" "+valor +" de Memoria "+Descri+"\n")
    else:
        ElimininarExistencias(Descri)
        return("error")
    
"""print(NuevaVenta("5000","Memoria 32 Gb")) """
def LeerEx():
    try:
        archivo = open("Existencias.txt","r",encoding="utf-8")
    except:
        archivo = open("Existencias.txt","a",encoding="utf-8")
        archivo.write("0 Memoria 16 Gb \n0 Memoria 32 Gb \n0 Memoria 8 Gb \n0 Cable \n0 Cargador \n0 Audifono cable \n0 Audifonos Inalambricos Diadema \n0 Audifonos Inalambricos")
        archivo = open("Existencias.txt","r",encoding="utf-8")
    texto1 = archivo.readlines()
    texto=""
    for i in texto1:
        xd=i.split()
        if len(xd)>1:
            texto=texto+xd[0]+"\n"
    return(texto)
def LeerEx2():
    try:
        archivo = open("Existencias.txt","r",encoding="utf-8")
    except:
        archivo = open("Existencias.txt","a",encoding="utf-8")
        archivo.write("0 Memoria 16 Gb \n0 Memoria 32 Gb \n0 Memoria 8 Gb \n0 Cable \n0 Cargador \n0 Audifono cable \n0 Audifonos Inalambricos Diadema \n0 Audifonos Inalambricos")
        archivo = open("Existencias.txt","r",encoding="utf-8")
    texto1 = archivo.readlines()
    texto2=""
    for i in texto1:
        xd=i.split()
        if len(xd)==2:
            texto2=texto2+xd[1]+"\n"
        elif len(xd)==3:
            texto2=texto2+xd[1]+" "+xd[2]+"\n"
        elif len(xd)==4:
            texto2=texto2+xd[1]+" "+xd[2]+" "+xd[3]+"\n"    
    return(texto2)
"""print(LeerEx2())  """     


def vista():
    global t1
    global t2
    global t3 
    try:
        archivo=open("Vistaventas.txt","r",encoding="utf-8")
    except:
        archivo=open("Vistaventas.txt","w",encoding="utf-8")
        archivo.write("")
        archivo.close()
        archivo=open("Vistaventas.txt","r",encoding="utf-8")
    texto1 = archivo.readlines()
    t1=""
    t2=""
    t3=""
    for i in texto1:
        a=i.split()
        if len(a)>2:
            t1=t1+str(a[0])+"\n"
            t2=t2+str(a[1])+"\n"
            a.pop(0)
            a.pop(0)
            s = ' '.join(str(x) for x in a)
            t3=t3+s+"\n"
    archivo.close()
    
    
    archivo.close()
def vistaBi(t):
    textob=""
    i=t.split()
    for e in i:
        if e!="\n":
            textob=textob+e+"\n"
    return(textob)
def vistaFecha():
    vista()
    return(t1)


def vistaVentas():
    vista()
    return(t2)


def vistaDes():
    vista()
    return(t3)

def resetear():
    try:
        remove('Audifonos.txt') 
    except:
        xd=""
    try:
        remove('Cargadores.txt')
    except:
        xd=""
    try:
        remove('Memorias.txt')
    except:
        xd=""
    try:
        remove('Cables.txt')
    except:
        xd=""
    try:
        remove('Existencias.txt')
    except:
        xd=""
    try:
        remove('Vistaventas.txt')
    except:
        xd=""
    sys. exit()


    

    