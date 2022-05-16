#!/usr/bin/python3

import argparse
import gameData

parser = argparse.ArgumentParser(description='El juego de la vida')
parser.add_argument('-g', '--game',
                    type=str,
                    help='selecciona un juego en especifico')

parser.add_argument('-l', '--list',
                    action='store_true',
                    help='Lista todos los juegos disponibles')

args = parser.parse_args()


gameList = ["Quiz", "Traduccion de codones", "El camino del gen"]

if args.list:
   for game in gameList:
      print(game)
   exit()

game = ""
if (not args.game):
   init = True
   while init:
      for game in gameList:
         print(f" para jugar a '{game}' escribe: {gameList.index(game) + 1} ")

      game = input("\n¿A que queres jugar? ")

      if (not game.isdigit() or int(game) in range(1, 1 + len(gameList))):
         init = False
      else:
         print ("\n Elija una opcion correcta \n")


class bcolors():
   OK = '\033[92m' #GREEN
   QUESTION = '\033[93m' #YELLOW
   FAIL = '\033[91m' #RED
   CONTEXT = '\033[96m' #CYAN
   RESET = '\033[0m' #RESET COLOR


def crossOut(text):
    result = '\u0336'
    for c in text:
        result = result + '\u0336' + c
    return(result + " ")

def correctOption (options):
   resp = ""
   for option in options[0].values():
      if(option[1]):
         resp = option[0]

   return resp


def quiz():
   try:
      quiz = gameData.quiz

      validLevel = True
      print("\nElija la cantidad de niveles " + bcolors.QUESTION + '[1/' + str(len(quiz)) + ']' + bcolors.RESET)
      print("Para ganar no tenes que " + bcolors.QUESTION + "fallar mas del 30% \n" + bcolors.RESET)
      levels = ""
      while validLevel:
         levels = input("Ingrese la cantidad de niveles que desea jugar: \n")
         if  not levels.isdigit() or not int(levels) in range( 1, 1 + len(quiz) ):
            print("Ingrese un nivel valido")
         else:
            validLevel = False

      print("QUIZ GAME")
      print("\nResponde las siguientes preguntas indicando el numero de la respuesta correcta\n")

      mistakes = 0
      limit = round(int(levels) * 0.6, 0)
      hits = 0

      print(f"No puedes fallar mas de {int(limit)} veces")
      for index in range(0, int(levels)):
         if(mistakes >= limit):
            print(bcolors.FAIL + "demasiados errores... ¡¡PERDISTE!!"+ bcolors.RESET)
            exit()
         value = quiz[index + 1]

         next = True
         while next:
            print(f"Pregunta numero {index + 1}\n")
            if("contexto" in value):
               print(bcolors.CONTEXT + value["contexto"] + bcolors.RESET + "\n")
            print(bcolors.QUESTION + value["pregunta"] + bcolors.RESET + "\n")
            for indexOp, option in value["opciones"].items(): #Option = [string, bool]
               print(f"{option[0]}: {indexOp}")
            response = input("\nRespuesta: ")

            if not response.isdigit() or not int(response) in range(1, 1 + len(value["opciones"])):
               print ("\n Elija una opcion correcta \n")
            else:
               next = False
               if(value["opciones"][response][1]):
                  print(bcolors.OK + "\n Correcto \n" + bcolors.RESET)
                  hits+=1
               else:
                  print(bcolors.FAIL + "\n Incorrecto :C" + bcolors.RESET)
                  mistakes+=1
                  answer = correctOption([value["opciones"]])
                  print(f"La respuesta correcta era: {answer} \n")

      print(bcolors.QUESTION + "Juego terminado!!" + bcolors.RESET)
      print("Lograste hacer " + bcolors.OK + str(hits) + bcolors.RESET  + " puntos!!" if hits >= limit else "Lograste hacer " + bcolors.FAIL + str(hits) + bcolors.RESET + " puntos!!")
   except KeyboardInterrupt:
      exit()


def traduccionDeCodones():
   try:
      codones = gameData.codones

      validLevel = True
      print("\nElija la cantidad de niveles " + bcolors.QUESTION + '[1/' + str(len(codones)) + ']' + bcolors.RESET)
      print("Para ganar no tenes que " + bcolors.QUESTION + "fallar mas del 60% \n" + bcolors.RESET)
      levels = ""
      while validLevel:
         levels = input("Ingrese la cantidad de niveles que desea jugar: \n")
         if  not levels.isdigit() or not int(levels) in range( 1, 1 + len(codones) ):
            print("Ingrese un nivel valido")
         else:
            validLevel = False

      print("\nTraduccion de codones! demuestra que sabes a que aminoacidos corresponde cada codon\n")
      print("La respuesta puede ser tanto con la forma acotada de 3 letras como con la de 1\n")

      mistakes = 0
      limit = round(int(levels) * 0.6, 0)
      hits = 0
      print(f"No puedes fallar mas de {int(limit)} veces")
      for index in range(0, int(levels)):
         if(mistakes >= limit):
            print(bcolors.FAIL + "demasiados errores... ¡¡PERDISTE!!"+ bcolors.RESET)
            exit()
         value = codones[index + 1]
         print( bcolors.QUESTION + f"codon: {value[0]}" + bcolors.RESET)
         response = input("Respuesta: ")

         if response.upper() == value[2] or response.lower() == value[1]:
            print(bcolors.OK + "\n Correcto \n" + bcolors.RESET)
            hits+=1
         else:
            mistakes+=1
            print(bcolors.FAIL + "\n Incorrecto :C" + bcolors.RESET)
            print(f"La respuesta correcta era: {value[1]}({value[2]}) \n")
      print(bcolors.QUESTION + "Juego terminado!!" + bcolors.RESET)
      print("Lograste hacer " + bcolors.OK + str(hits) + bcolors.RESET  + " puntos!!" if hits >= limit else "Lograste hacer " + bcolors.FAIL + str(hits) + bcolors.RESET + " puntos!!")

   except KeyboardInterrupt:
      exit()


def elCaminoDelGen():
   try:
      camino = gameData.camino
      print("El camino del gen")
      print("\nSeleccione la opción correcta para describir el proceso de la expresión génica \n")
      history = ""
      for key, value in camino.items():
         next = True
         while next:
            print(f"{key}° paso")
            print(bcolors.QUESTION + value["pregunta"] + bcolors.RESET + "\n")
            for index, option in value["opciones"].items():
               print(f"{option[0]}: {index}")
            response = input("\nRespuesta: ")

            if not response.isdigit() or not int(response) in range(1, 1 + len(value["opciones"])):
               print ("\n Elija una opcion correcta \n")
            else:
               history += value["pregunta"] + ' '
               next = False
               userAnswer = value["opciones"][response][0]
               if(value["opciones"][response][1]):
                  history = history.replace("____", bcolors.OK + userAnswer + bcolors.RESET)
                  print(bcolors.OK + "\n Correcto \n" + bcolors.RESET)
               else:
                  print(bcolors.FAIL + "\n Incorrecto :C" + bcolors.RESET)
                  answer = correctOption([value["opciones"]])
                  history = history.replace("____", bcolors.FAIL + crossOut(userAnswer) + bcolors.OK + answer + bcolors.RESET)
                  print(f"La respuesta correcta era: {answer} \n")
      print (bcolors.QUESTION + "Historia completa: " + bcolors.RESET)
      print(history)
   except KeyboardInterrupt:
      exit()



if args.game == "Quiz" or game == "1":
    quiz()
if args.game == "Traduccion de codones" or game == "2":
   traduccionDeCodones()
if args.game == "El camino del gen" or game == "3":
   elCaminoDelGen()
