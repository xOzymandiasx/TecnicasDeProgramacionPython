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
  

# * 4) Realizar una función para buscar si hay ganador en un juego de ta-te-ti. La función recibe una matriz de 3x3 con la situación actual del juego. Cada elemento de la matriz contiene “x”, “o” o “ ”(espacio), igual que en el ejercicio 3. La función debe devolver un None si no hay ganador, o devolver “x” o “o” según si el ganador es la “x” o la “o”.

tablero3 = [[" "," ","o"],["o","o","o"],["x"," ","x"]];  

def checkForWinner(board):
  # Horizontal
  if (board[0][0] == board[0][1] == board[0][2]): return board[0][0];
  elif (board[1][0] == board[1][1] == board[1][2]): return board[1][0];
  elif (board[2][0] == board[2][1] == board[2][2]): return board[2][0];
  # Vertical
  elif (board[0][0] == board[1][0] == board[2][0]): return board[0][0];
  elif (board[0][1] == board[1][1] == board[2][1]): return board[0][1];
  elif (board[0][2] == board[1][2] == board[2][2]): return board[0][2];
  # Diagonal
  elif (board[0][0] == board[1][1] == board[2][2]) \
    or (board[0][2] == board[1][1] == board[2][0]): return 2;
  
  
print(f"el ganador es {checkForWinner(tablero3)}");