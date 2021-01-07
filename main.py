import sys
import os
from lectura import leer,precioMetales, respuestas, libros

def saberValores(input):
  frasesMetal,preguntas=leer(input)
  precioMetales(libros.valor,frasesMetal)
  resultado=respuestas(preguntas,libros.valor,libros.metales)
  for lineas in resultado:
    print(lineas)

if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    if not os.path.isfile(input_file):
        print("Can't find the input file: " + input_file)
        exit(1)
    saberValores(input)