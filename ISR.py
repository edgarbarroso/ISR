import numpy as np
import pandas as pd

def BrutoANeto(fltSueldo= 28529.65, Tipo = "Mensual", DesplegaInfo="No"):
    boolT = True
    intPos = 0
    if (Tipo == "Quincenal"):
        df1 = pd.read_csv("2018Tablas\\ISRQuincenal.csv")
    else:
        if (Tipo == "Mensual"):
            df1 = pd.read_csv("2018Tablas\\ISRMensual.csv")
        else:
            if (Tipo == "Semanal"):
                df1 = pd.read_csv("2018Tablas\\ISRSemanal.csv")
            else:
                df1 = pd.read_csv("2018Tablas\\ISRCantidad.csv")
    df1 = df1.infer_objects()
    while (boolT):
        if(fltSueldo<df1.Superior[intPos]):
            boolT=False
        else:
            intPos+=1
    fltExcedente = fltSueldo - float ("%.2f" %df1.Inferior[intPos])
    fltImpMarg = fltExcedente*float ("%.2f" % df1.Porciento[intPos])/100
    fltImpTotal = float ("%.2f" %fltImpMarg) + float ("%.2f" %df1.Cuota[intPos])
    
    if(DesplegaInfo == "Si"):
        print ("Limite Inferior ", df1.Inferior[intPos])
        print ("Excedente" + str(fltExcedente))
        print ("Impuesto marginal" + fltImpMarg)
        print ("Cuota Fija" + df1.Cuota[intPos])
        print ("Total ISR" + fltImpTotal)
        print ("Total Neto" + fltSueldo - fltImpTotal)
    
    return fltSueldo - fltImpTotal

def NetoaBruto(fltSueldo= 23636.12,Tipo = "Mensual", DesplegaInfo="No"):
    boolT = True
    intPos = 0
    if (Tipo == "Quincenal"):
        df1 = pd.read_csv("2018Tablas\\ISRQuincenal.csv")
    else:
        if (Tipo == "Mensual"):
            df1 = pd.read_csv("2018Tablas\\ISRMensual.csv")
        else:
            if (Tipo == "Semanal"):
                df1 = pd.read_csv("2018Tablas\\ISRSemanal.csv")
            else:
                df1 = pd.read_csv("2018Tablas\\ISRCantidad.csv")
    df1 = df1.infer_objects()
    
    while (boolT):
        if(fltSueldo<BrutoANeto(df1.Superior[intPos])):
            boolT=False
        else:
            intPos+=1
    sueldoBruto =(fltSueldo + df1.Cuota[intPos] -df1.Inferior[intPos]*df1.Porciento[intPos]/100)/(1-df1.Porciento[intPos]/100)
    sueldoBruto = float ("%.2f" % sueldoBruto)
    if(DesplegaInfo == "Si"):
        return BrutoANeto(sueldoBruto, Tipo, DesplegaInfo)
    else:
        return sueldoBruto
