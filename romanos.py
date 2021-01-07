import os
from colores import Colores

class Romano:
  VALOR = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

def romanoCheck(RN): #RN : Roman Number
  global flag,resta
  flag=0
  resta=9000
  RN_largo=len(RN)

  #-----------------------------------------
  #Checkeo de las repeticiones de las letras
  if RN.count('I')>3 or RN.count('X')>4 or RN.count('C')>4 or RN.count('M')>4: 
    return False
  if (RN.count('X')==4 and 'XXXIX' not in RN)\
    or(RN.count('C')==4 and 'CCCXC'not in RN)\
    or(RN.count('M')==4 and 'MMMCM' not in RN): 
    return False

  #-----------------------------------------------
  #Checkeo que los caracteres sean los indicados
  llaves=Romano.VALOR.keys()
  if not RN or not all(c in llaves for c in RN):
    return False

  #--------------------------------------------
  #Checkeo de las reglas de restas dentro de RN
  for i in range(RN_largo-1):

    #Detecta restas comparando con el numero sucesor
    if Romano.VALOR[RN[i]]<Romano.VALOR[RN[i+1]]:
      #se considera el caracter actual y su sucesor
      arab = int(Romano.VALOR[RN[i]])
      arabNext=int(Romano.VALOR[RN[i+1]])
      #Reglas de resta:
      if flag==1:
        return False
      elif (len(str(arabNext-arab)))>=len(str(resta)):
        return False 
      elif arab is 1 and arabNext>10:
        return False
      elif arab is 5:
        return False
      elif arab is 10 and arabNext>100:
        return False
      elif arab is 50:
        return False
      resta= arabNext-arab
      flag=1
      
    else:
      arab = int(Romano.VALOR[RN[i]])
      arabNext=int(Romano.VALOR[RN[i+1]])
      if flag==1 and len(str(resta))<=len(str(arabNext)):
        print("no resta mayor")
        return False 
      elif flag==0:
        resta=arab
      flag=0
      
  return True  
#funcion para convertir numero romano a arabe, si el numero
# esta mal escrito, entonces retorna valor Nulo    
def convertRoman(RN):
  paint=Colores()
  if not romanoCheck(RN):
    print(paint.Color['WARNING'] + "**WARNING: el numero: "+RN+", "
                "no es correcto con la sintaxis romana**" + paint.Color['ENDC'])
    return None
  numeros=[]
  for i in range(len(RN)-1):
    if Romano.VALOR[RN[i]]<Romano.VALOR[RN[i+1]]:
      numeros.append(-Romano.VALOR[RN[i]])
    else:
      numeros.append(Romano.VALOR[RN[i]]) 
  numeros.append(Romano.VALOR[RN[len(RN)-1]])
  return sum(numeros)
  

if __name__ == "__main__":
   
  test=convertRoman('CMXCVIII')
  print(test)
  
    