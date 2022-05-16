## El juego de la vida - Estacion de juegos

#### lista de juegos
En la version actual hay 3 juegos disponibles:
* Quiz
* Traduccion de codones 
* El camino del gen

***********

#### Dependencias
Para poder jugar alguno de esos juegos en tu computadora tenes que tener instalado Git y Python
#### Pasos:
1. clonar el repositorio con `git clone git@github.com:CardozoCasariegoLuciano/El_juego_de_la_vida.git`
2. darle permisos de ejecucion al archivo main.py con `sudo chmod +x main.py`
3. Jugar usando `./main.py`

************

#### Agregar tus preguntas
Las preguntas estan almacenadas en el archivo gameData.py en un diccionario por cada juego

##### Quiz
El diccionario del juego de preguntas tiene las siguientes claves-valor:

* "pregunta" : string ==> aqui escribe tu pregunta indicando el lugar de la respusta con ____ (cuatro guiones bajos)
* "contexto" : string ==> (opcional) informacion para dar contexto a la pregunta
* "opciones" : dict([string, bool]) ==> es otro diccionario cuyos valores son arrays de dos posiciones donde la primera es una posible opcion para responder la pregunta y la segunda posicion es un bool que indica si es la opcion correcta o no


##### Traduccion de codones
Para el juego de traduccion de codones a aminoacidos hay un diccionario simple cuyos calores son arrays de 3 posiciones:

[`<codon>`, `<respuesta acotada de 3 letras>`, `<respuesta acotada de 1 letra>`]


##### El camino del gen
El diccionario del juego del camino del gen tiene las siguientes claves-valor:

* "pregunta" : string ==> aqui escribe tu pregunta indicando el lugar de la respusta con ____ (cuatro guiones bajos)
* "opciones" : dict([string, bool]) ==> es otro diccionario cuyos valores son arrays de dos posiciones donde la primera es una posible opcion para responder la pregunta y la segunda posicion es un bool que indica si es la opcion correcta o no
