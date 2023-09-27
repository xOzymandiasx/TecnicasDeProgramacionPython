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