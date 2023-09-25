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
  