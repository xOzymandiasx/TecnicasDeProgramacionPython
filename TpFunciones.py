# # * 1) Construir una función calcule la distancia entre 2 puntos en el plano. La función tiene 4 argumentos (x1,
# # * y1, x2, y2) que son las coordenadas de los puntos. Los tipos de datos de entrada y salida son punto
# # * flotante (float). Opcional, la función recibe 2 vectores (de 2 elementos) en lugar de 4 valores.

# from math import sqrt;
# from math import pow;

# def splitWords(word):
#     return word.replace(" ", "").split(",");


# vector1 = input("Ingrese el primer vector separando los número con una coma(,): ");
# vector2 = input("Ingrese el segundo vector separando los número con una coma(,): ");

# vectors = [
#     {"vector1": {
#         "x1": float(splitWords(vector1)[0]),
#         "y1": float(splitWords(vector1)[1])
#     }},
#     {"vector2": {
#       "x2": float(splitWords(vector2)[0]),
#       "y2": float(splitWords(vector2)[1])
#     }}
# ];

# def pitagoras (aov):
#   return sqrt(pow(aov[1]["vector2"]["x2"] - aov[0]["vector1"]["x1"], 2) + pow(aov[1]["vector2"]["y2"] - aov[0]["vector1"]["y1"], 2));

# print(pitagoras(vectors));


# # * 2) Realizar una función que, dadas las 3 dimensiones en centímetros de una caja, devuelva el volumen total
# # * en litros. Realizar otra función que, dadas las 3 dimensiones en centímetros de una caja, devuelva la
# # * superficie total de la caja en cm². Entrada: las 3 dimensiones en centímetros. Salida: el volumen (en litros)
# # * y la superficie total (en cm²). Opcional, Realizar una sola función que reciba las dimensiones de la caja y
# # * devuelva tanto el volumen, como la superficie de la caja, simultáneamente.

# boxLen = int(input("Ingrese el largo de la caja en cm: "));
# boxHigh = int(input("Ingrese el alto de la caja en cm: "));
# boxWidth = int(input("Ingrese el ancho de la caja en cm: "));

# def totalVolumeInLiters(len, high, width):
#   return len * high * width / 1000;

# def surfaceArea(len, high, width):
#   return 2 * len * width + 2 * high * width + 2 * high * len;

# def volumeAndSurface(len, high, width):
#   return totalVolumeInLiters(len, high, width), surfaceArea(len, high, width);

# print(f"El volumen total en litros de la caja es de: {volumeAndSurface(boxLen, boxHigh, boxWidth)[0]}");
# print(f"La superficie total en cm² de la caja es de: {volumeAndSurface(boxLen, boxHigh, boxWidth)[1]}");

# # * 3) El método más fácil para encriptar un mensaje consiste en el de desplazamiento, cada carácter se desplaza
# # * una cantidad fija llamada clave. Por ejemplo si la clave es 1, la palabra HOLA sería IPMB. Realizar 2
# # * funciones, una para encriptar y otra para desencriptar. A la función se le pasa el texto y la clave (un
# # * entero), y debe devolver un texto. Una pista, la función ord() convierte un carácter en un su código ASCII y
# # * la función chr() convierte el código ASCII en carácter. Tener en cuenta que el texto resultante debe estar
# # * compuesto por las letras del abecedario. Pueden ignorar las diferencias entre mayúsculas y minúsculas, y
# # * pueden ignorar de convertir los signos de puntuación. Opcional, pueden hacer el encriptado más
# # * complejo. Opcional, pueden hacer una sola función que encripte y desencripte, a la misma se le pasa el
# # * texto, la clave (igual que entes) y la operación que se desea realizar (encriptar o desencriptar).

# word = input("Ingrese palabra a encriptar o desencriptar: ");
# value = int(input("ingrese la clave: "));

# def encriptedWord(word, key):
#   encriptedArray = []; 
  
#   for letter in range(len(word)):
#     encriptedArray.append(chr(ord(word[letter]) + key));  
     
#   return "".join(encriptedArray);
  
# def desencriptWord(word, key=0):
#   desencriptedArray = [];
  
#   for letter in range(len(word)):
#     desencriptedArray.append(chr(ord(word[letter]) - key));
    
#   return "".join(desencriptedArray);
  
# def encriptOrDesencriptWord(word, key):
#   condition = input("Ingrese '1' para encriptar, '2' para desencriptar: ");
  
#   if (condition == "1"): return encriptedWord(word, key);
#   if (condition == "2"): return desencriptWord(word, key);
#   else: 
#     print(f"ingreso de datos incorrecto: '{condition}'");
#     encriptOrDesencriptWord(word, key);

# encriptOrDesencriptWord(word, value);
  

# # * 4) Construir una función que reciba el primer nombre, el segundo nombre y apellido de una persona y
# # * devuelva un string con Apellido, Primer nombre inicial del segundo nombre punto. Tener en cuenta que el
# # * segundo nombre es opcional en ese caso no devuelve la inicial del segundo nombre. Opcional, convertir a
# # * mayúscula la inicial de cada nombre y apellido.

# name1 = input("ingrese su nombre: ").capitalize();
# name2 = input("ingrese, si posee, su segundo nombre, de lo contrario pulse enter: ").capitalize();
# surname = input("ingrese su apellido: ").capitalize();

# def completeStringName(name, name2 ="", surname=""):
#   if (len(name2) == 0): return f"{surname} {name}";
#   if (len(name2) >= 1): return f"{surname} {name} {name2[0]}.";
  

# print(completeStringName(name1, name2, surname));


# # * 5) Realizar una función para calcular la cantidad de rollos de empapelado que se necesita para empapelar
# # * una habitación. La función recibe las dimensiones de la habitación en metros (largo, ancho y alto), el ancho
# # * del rollo en cm y el largo del rollo en metros, debe devolver un entero con la cantidad de rollos requerida.
# # * Tengan en cuenta que, la habitación es rectangular y la altura es pareja en toda ella. Al empapelar las tiras
# # * se colocan verticalmente, cada tira debe entrar entera en toda la altura de la pared (si lo que sobra en el
# # * rollo es menos que la altura de la habitación, se debe desechar), se puede hacer que una tira cubra una
# # * esquina (la tira se comparte por 2 paredes). Nota: no tener en cuenta las aberturas como ventanas o
# # * puertas. Opcional, si no se especifican las dimensiones el rollo se debe calcular con rollos de 52cm de
# # * ancho y 10 m de largo.

# large = float(input("Ingrese el largo de la habitación en metros: "));
# width = float(input("Ingrese el ancho de la habitación en metros: "));
# high = float(input("Ingrese el alto de la habitación en metros: "));

# reelWidth = input("Ingrese el ancho del rollo en centimetros o presione 'enter' para su valor por defecto: ");
# reelLarge = input("Ingrese el largo del rollo en metros o presione 'enter' para su valor por defecto: ");

# if (reelWidth != ""):
#   reelWidth = float(reelWidth);
#   reelLarge = float(reelLarge);
# else:
#   reelWidth = 52.00;
#   reelLarge = 10.00;


# def reelsForRoom(roomLarge, roomWidth, roomHigh, reelWidt, reelLarge):
#   roomDimensions = 2 * roomLarge + 2 * roomWidth;
#   roomDimensionCount = 0;
  
#   reelHighCount= 0;
#   reelsCount = 0;
  
#   while roomDimensionCount <= roomDimensions:
#     if (reelLarge == reelHighCount):
#       reelsCount += 1;
#       reelHighCount = 0;
#     elif (reelLarge - reelHighCount < roomHigh):
#       reelsCount += 1;
#       reelHighCount = 0;
#     else:
#       roomDimensionCount += reelWidt / 100;
#       reelHighCount += roomHigh;
#       if (roomDimensionCount >= roomDimensions):
#         reelsCount += 1;
#         break; 
           
#   return int(reelsCount);
  
  
# print(reelsForRoom(large, width, high, reelWidth, reelLarge));