#   # * 1) Corregir el código para cumplir con la consigna.
# # * Ingresar 5 números y guardarlos en un vector. Al finalizar informar el número menor.

# vector = [];
# menor = 0;

# for n in range(5):
#   nuevo = float(input("Ingrese el siguiente número:"));
#   vector.append(nuevo);

# for elemento in vector:
#   if (menor == 0): menor = elemento;
#   if (elemento < menor): menor = elemento;
    
# print("El número menor es:", menor);


# # * 2) Dado el siguiente vector [1, 5, 3, 9, 10, 8], informar el número mayor.

# vector = [1, 5, 3, 9, 10, 8];
# mayor = 0;

# for elemento in vector:
#   if (mayor == 0): mayor = elemento;
#   if (elemento > mayor): mayor = elemento;
    
# print("El número mayor es:", mayor);


# # * 3) Dado el siguiente vector [5, 9, 15, 2, -8, 3], informar el número mayor y el número menor.

# vector = [5, 9, 15, 2, -8, 3];
# mayor = 0;
# menor = 0;

# for elemento in vector:
#   if (menor == 0): menor = elemento;
#   if (elemento < menor): menor = elemento;
    
# for elemento in vector:
#   if (mayor == 0): mayor = elemento;
#   if (elemento > mayor): mayor = elemento;
    
# print("El número mayor es:", mayor);
# print("El número menor es:", menor);


# # * 4) Dado el siguiente vector [-5, -9, -15, -2, -8, -3], informar el número mayor y el número menor.

# vector = [-5, -9, -15, -2, -8, -3];
# mayor = 0;
# menor = 0;

# for elemento in vector:
#   if (menor == 0): menor = elemento;
#   if (elemento < menor): menor = elemento;
    
# for elemento in vector:
#   if (mayor == 0): mayor = elemento;
#   if (elemento > mayor): mayor = elemento;
    
# print("El número mayor es:", mayor);
# print("El número menor es:", menor);


# # * 5) Dado el siguiente vector [8, 10, 15, 2, 8, 6, 21, 5], informar los dos números mayores.

# vector = [8, 10, 15, 2, 8, 6, 21, 5];
# mayor = 0;
# mayor2 = 0;

# for elemento in vector:
#   if (mayor == 0): mayor = elemento;
#   if (elemento > mayor): 
#     mayor2 = mayor;
#     mayor = elemento;

# if mayor2 == 0:
#   for elemento in vector:
#     if (elemento > mayor2 and elemento < mayor): 
#       mayor2 = elemento;
    
# print("El número mayor es:", mayor);
# print("El segundo número mayor es:", mayor2);


# # * 6) Dado el siguiente vector [5,-2, 8, 10, -4, 13, 21], a cada elemento, sumarle 2, y guardarlo en un nuevo vector.

# vector = [5,-2, 8, 10, -4, 13, 21];
# vectorPlus2 = [];

# for number in vector:
#   vectorPlus2.append(number + 2);
  
# print(vectorPlus2);


# # * 7) Ingresar 10 números y guardarlos en un vector nuevo. Al finalizar informar el número mayor y el número menor.

# vector = [];
# mayor = 0;
# menor = 0;

# for n in range(10):
#   nuevo = int(input("Ingrese el siguiente número:"));
#   vector.append(nuevo);
  
# for elemento in vector:
#   if (menor == 0): menor = elemento;
#   if (elemento < menor): menor = elemento;
    
# for elemento in vector:
#   if (mayor == 0): mayor = elemento;
#   if (elemento > mayor): mayor = elemento;
    
# print("El número mayor es:", mayor);
# print("El número menor es:", menor);