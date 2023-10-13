#  # * 1) Realizar una función para normalizar un vector. La función recibe un vector de longitud indeterminada de float, y debe devolver un nuevo vector normalizado, es decir el módulo del vector debe ser 1. 

# from math import sqrt;

# vector1 = [1, 1, 1];
# vector2 = [1, 3, 7, 9];

# def normalizeVector(array):
#   unitVector = 0;
#   result = [];
  
#   for number in array:
#     unitVector += number ** 2;
   
#   unitVector = sqrt(unitVector);
#   if (unitVector == 0): return f"Imposible dividir por 0";
    
#   for number in array:
#     result.append(number / unitVector);
    
#   return result;
  
# print(normalizeVector(vector2));


#  # * 2) Construir una función que elimine los elementos duplicados en una lista. La función recibe una lista, y debe devolver una lista que contenga una sola copia de cada elemento de la lista suministrada.
 
# lista1 = [1, 4, 1, 5, 4, 1];
# lista2 = ["Juan","Luis","Juan","Ana","Luis"]

# def eliminateDuplicates(array):
#   newArray = [];
  
#   for element in array:
#     if element not in newArray:
#       newArray.append(element);
  
#   return newArray;

# print(eliminateDuplicates(lista1));
# print(eliminateDuplicates(lista2));


# # * 3) Realizar una función para mostrar por consola un tablero de ta-te-ti. La función recibe una matriz de 3x3 con la situación actual del juego. Cada elemento de la matriz contiene “x”, “o”, o “ ”(espacio). Nota: normalmente evitamos que una función imprima directamente, pero en ocasiones es conveniente.

# tablero = [["x","o"," "],["o"," ","x"],["x"," ","o"]];

# def displayTaTeTi(board):
#   for element in board:
#     print(f" {element[0]} | {element[1]} | {element[2]}");
#     print(f"---+---+---");
    
# displayTaTeTi(tablero);
  

# # * 4) Realizar una función para buscar si hay ganador en un juego de ta-te-ti. La función recibe una matriz de 3x3 con la situación actual del juego. Cada elemento de la matriz contiene “x”, “o” o “ ”(espacio), igual que en el ejercicio 3. La función debe devolver un None si no hay ganador, o devolver “x” o “o” según si el ganador es la “x” o la “o”.

# tablero1 = [["x","o"," "],["o"," ","x"],["x"," ","o"]];
# tablero2 = [["x","o"," "],["x","o","x"],["x"," ","o"]];
# tablero3 = [[" "," "," "],["o","x","o"],["x"," ","x"]];

# def checkForWinner(board):
#   # Horizontal
#   if (board[0][0] == board[0][1] == board[0][2] and board[0][0] != " "): return board[0][0];
#   elif (board[1][0] == board[1][1] == board[1][2] and board[1][0] != " "): return board[1][0];
#   elif (board[2][0] == board[2][1] == board[2][2] and board[2][0] != " "): return board[2][0];
#   # Vertical
#   elif (board[0][0] == board[1][0] == board[2][0] and board[0][0] != " "): return board[0][0];
#   elif (board[0][1] == board[1][1] == board[2][1] and board[0][1] != " "): return board[0][1];
#   elif (board[0][2] == board[1][2] == board[2][2] and board[0][2] != " "): return board[0][2];
#   # Diagonal
#   elif (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " "): return board[0][0];
#   elif (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " "): return board[0][2];
#   # Si no hay ganador
#   return None;
  
  
# print(f"el ganador es {checkForWinner(tablero1)}");


# * 5) Construir una función para calcular la superficie de un polígono cualquiera, dados sus vértices utilizando la fórmula del área de Gauss. La función recibe una lista de vértices, la cantidad de vértices es indeterminada. Cada vértice es un vector de dos elementos con la posición (x, y). La función debe devolver un float con la superficie del polígono.

prueba = [[4], [5], [6]];
p2 = [[1,1], [1,4], [5,1]];

def poligonSurface(array):
  result = 0
  
  for number in range(len(array)):
    if (array[number] == array[-1]): result += array[number][0] * array[0][1];
    else: result += array[number][0] * array[number + 1][1];
    
  return result;

print(poligonSurface(p2));