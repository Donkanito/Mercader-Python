#Lectura del input.txt
import os
from colores import Colores
from romanos import convertRoman
class libros:
  valor={}
  metales={}
# NOTA se usaron variables float, puesto que se 
# necesitaba ejecutar una division

def leer(input):
    
    peticiones=[]   #preguntas en el input, detectadas con '?'
    ecuaciones=[]   #ecuaciones para deducir valores de metales
    error=[]        #frases no aceptadas como input, 
                    #se pueden imprimir si se desea
    paint=Colores() #paleta de colores para warnings
    info= open("input.txt","r")
    info=[line for line in info if line.strip() != ''] #evitar lineas en blanco
    for lineas in info:
        lineaNoSalto=lineas.rstrip("\n")
        lineaSeparada=lineaNoSalto.split(' ')

        # evita error lanzado si hay espacios extras en las frases de inputs
        lineaSeparada=[line for line in lineaSeparada if line.strip() != '']
        #Detectar las frases que son preguntas, estas deben comenzar con 'how'
        if "?" in lineas and lineaSeparada[0]=="how":
            peticiones.append(lineaSeparada)
        #detectar las ecuaciones, las frases que son usadas para deducir
        #el precio de los metales
        elif "Credits" in lineas and "?" not in lineas and lineaSeparada[-3]=='is':
            
            try:
                costo=int(lineaSeparada[-2])
                ecuaciones.append(lineaSeparada)
            except ValueError:
                
                print(paint.Color['WARNING'] + "**WARNING: mal formato, recordar que los datos con "
                    "metales son ingresados de la forma:  \n EXAMPLE: glob Gold is 578 Credits **" 
                    + paint.Color['ENDC'])
                error.append(lineaNoSalto)
                continue
        #se detectan las frases que entregan datos directos sobre valores galacticos,
        # ejemplo: glob is V        
        elif lineas.split()[-1] in 'IVXLCDM' and len(lineaSeparada)==3 and lineaSeparada[1]=='is':
            if lineaSeparada[0] not in libros.valor:
                libros.valor.update({lineaSeparada[0]:lineaSeparada[2]})
            else:
                print(paint.Color['WARNING'] + "**WARNING: hay una moneda galactica repetida, "
                    "se considera el primer valor propuesto**"+ paint.Color['ENDC'])
                continue
        else:
            error.append(lineaNoSalto)
    return ecuaciones,peticiones
    #retorna las frases del input separadas en categorias

#funcion para obtener el precio de los metales
def precioMetales(valores,metales):
    paint=Colores()
    for lineas in metales:
        numeros=[]
        flag2=0
        for palabra in lineas[:-4]:
            if palabra in valores:
                numeros.append(valores[palabra])
            else:
                flag2=1
                print(paint.Color['WARNING'] + "**WARNING: se desconoce el valor: "+palabra+", "
                "no se puede deducir el precio del metal: " + str(lineas[-4])+
                "\n  Tampoco se podran responder preguntas que contengan: " +palabra+"*****"+ paint.Color['ENDC'])
                break
        if flag2==0:
            denominador=convertRoman("".join(numeros))
            if denominador is not None:
                numerador=float(lineas[-2])
                libros.metales.update({lineas[-4]:float(numerador/denominador)})
            else: print(paint.Color['WARNING'] + 
                    "**WARNING: Escriba numero romano correctamente para deducir precio de metales*****"+
                    paint.Color['ENDC'])
            
    return None

#funcion para realizar la conversion final 
# de numero galactico a arabe
def conversionGalactica(galaxyDolars,valores):
    numeros=[]
    for items in galaxyDolars:
        if items in valores:
            numeros.append(valores[items])
        else:
            return None
    creditos=convertRoman("".join(numeros))
    return creditos

#se arma la lista de respuestas
def respuestas(peticiones,valores,metales):
    respuestas=[]
    for preguntas in peticiones:
        if "much" in preguntas and preguntas[2]=='is':
            creditos=conversionGalactica(preguntas[3:-1],valores)
            if creditos is not None:
                respuestas.append(" ".join(preguntas[3:-1])+" is "+ str(creditos) + " Credits")
            else:
                respuestas.append("I have no idea what you are talking about")
        elif "many" in preguntas and preguntas[3]=='is' and preguntas[-2] in metales:
            creditos=conversionGalactica(preguntas[4:-2],valores)
            
            if creditos is not None:
                creditos=creditos*metales[preguntas[-2]]
                respuestas.append(" ".join(preguntas[4:-1])+" is "+ str(creditos) + " Credits")
                
            else:
                respuestas.append("I have no idea what you are talking about")
        else:
                respuestas.append("I have no idea what you are talking about")
    return respuestas       

if __name__ == "__main__":
    frasesMetal,preguntas=leer(input)
    precioMetales(libros.valor,frasesMetal)
    resultado=respuestas(preguntas,libros.valor,libros.metales)
    print(resultado)