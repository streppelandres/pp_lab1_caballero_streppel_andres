Desafio Stark 


Industrias Stark es principalmente una empresa de defensa que desarrolla y fabrica armas avanzadas y tecnologías militares.
  

Recientemente ha decidido ampliar su departamento de IT y para acceder a las entrevistas es necesario completar el siguiente desafío, el cual estará dividido en etapas. Cada semana recibiremos un nuevo pedido de parte de la empresa.


  



La empresa compartió con todos los participantes cierta información confidencial de un grupo de superhéroes.  Y semana a semana enviará una lista con los nuevos requerimientos. Quien supere todas las etapas accedera a una entrevista con el director para  de la compañía.


Set de datos


La información a ser analizada se encuentra en el archivo data_stark.py,  por tratarse de una lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera:


from data_stark import lista_personajes


Formato de los datos recibidos


lista_heroes =
[
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
 {
   "nombre": "Rocket Raccoon",
   "identidad": "Rocket Raccoon",
   "empresa": "Marvel Comics",
   "altura": "122.77",
   "peso": "25.73",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Brown",
   "fuerza": "5",
   "inteligencia": "average"
 }
]




________________


Desafío #01:
Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
4. Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
5. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
6. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
7. Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
8. Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
9. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
10. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
11. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
12. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
13. Listar todos los superhéroes agrupados por color de ojos.
14. Listar todos los superhéroes agrupados por color de pelo.
15. Listar todos los superhéroes agrupados por tipo de inteligencia