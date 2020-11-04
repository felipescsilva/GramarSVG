# // The Nature of Code
# // L-System
from turtle import *
import canvasvg

length = 0
angle = 0
regra = {}
key = []


def main():
  print("FELIPE SOARES = 081180008 - COMPILADORES - EC6")
  print("DESAFIO N1.2 - L-SYSTEM")
  
  current, count, trans = trataInfoFile()
  
  getRegra(trans)
  print("TRANS: ",trans)
  print("COUNT: ",count)
  print("CURRENT: ",current)

  for i in range(0, count):
  
    for p in range(len(key)):
      current = current.replace(key[p], regra[key[p]])
      print(current)
    
  
  speed(0)
  pensize(2)
  screensize(10000,10000)
  draw(current)
  dwg = getscreen().getcanvas()
  canvasvg.saveall("image.svg", dwg)
  exitonclick()


def trataInfoFile():
  arquivo = open('regra.txt', 'r')
  dados   = []
  count, current = "", ""

  for line in arquivo:
    line = line.split(":")
    dados.append(line[1].rstrip('\n'))
  
  trans   = str(dados[1])
  current = str(dados[2])
  count   = int(dados[3])

  global length, angle
  length   = int(dados[4])
  angle   = int(dados[5])
  arquivo.close()

  return current, count, trans


def getRegra(trans):
  x = trans.split(",")

  for i in range (len(x)):
      y = x[i].split("->")
      regra.update({y[0]: y[1]}) #Realizar dicionario de dados
      key.append(y[0])


def draw(path):
  
  for symbol in path:
    if symbol == 'F':
      forward(length)
    elif symbol == '-':
      left(angle)
    elif symbol == '+':
      right(angle)

#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()