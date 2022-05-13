#!/usr/bin/python3

import argparse
import gameData

parser = argparse.ArgumentParser(description='El juego de la vida')
parser.add_argument('-g', '--game',
                    type=str,
                    help='selecciona un juego en espesifico')

parser.add_argument('-l', '--list',
                    action='store_true',
                    help='Lista todos los juegos disponibles')

args = parser.parse_args()


gameList = ["quiz", "Traduccion de codones", "El camino del gen"]

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



def quiz():
   quiz = gameData.quiz
   print("QUIZ GAME")
   print("\nResponde las siguientes preguntas indicando el numero de la respuesta correcta\n")
   aciertos = 0
   for key, value in quiz.items():
      next = True
      while next:
         print(f"Pregunta numero {key}")
         print(value["pregunta"] + "\n")
         for index, option in value["opciones"].items(): #Option = [string, bool]
            print(f"{option[0]}: {index}")
         response = input("\nRespuesta: ")

         if not response.isdigit() or not int(response) in range(1, 1 + len(value["opciones"])):
            print ("\n Elija una opcion correcta \n")
         else:
            next = False
            if(value["opciones"][response][1]):
               aciertos += 1
               print("\n Correcto \n")
            else:
               print("\n Incorrecto :C \n")
   print(f"\n Fin del juego {aciertos}/{len(quiz)} aciertos")

def traduccionDeCodones():
   codones = gameData.codones
   print("\nTraduccion de codones! demuestra que sabes a que aminoacidos corresponde cada codon\n")
   print("La respuesta puede ser tanto con la forma acotada de 3 letras como con la de 1\n")
   aciertos = 0
   for value in codones.values():
      print(f"codon: {value[0]}")
      response = input("Respuesta: ")

      if response.upper() == value[2] or response.lower() == value[1]:
         aciertos += 1
         print("\n Correcto \n")
      else:
         print("\n Incorrecto :C \n")

   print(f"\n Fin del juego {aciertos}/{len(codones)} aciertos")

def elCaminoDelGen():
   camino = gameData.camino
   print("El camino del gen")
   print("\nSeleccione la opción correcta para describir el proceso de la expresión génica \n")
   aciertos = 0
   for key, value in camino.items():
      next = True
      while next:
         print(f"{key}° paso")
         print(value["pregunta"] + "\n")
         for index, option in value["opciones"].items():
            print(f"{option[0]}: {index}")
         response = input("\nRespuesta: ")

         if not response.isdigit() or not int(response) in range(1, 1 + len(value["opciones"])):
            print ("\n Elija una opcion correcta \n")
         else:
            next = False
            if(value["opciones"][response][1]):
               aciertos += 1
               print("\n Correcto \n")
            else:
               print("\n Incorrecto :C \n")
   print(f"\n Fin del juego {aciertos}/{len(camino)} aciertos")


if args.game == "quiz" or game == "1":
   quiz()
if args.game == "traduccion de codones" or game == "2":
   traduccionDeCodones()
if args.game == "el camino del gen" or game == "3":
   elCaminoDelGen()
