#  #* 1) Corregir el código para cumplir con la consigna.
# #* Crear una función que dados 2 números, devolver el promedio.

# number1 = float(input("Ingrese el valor 1: "));
# number2 = float(input("Ingrese el valor 2 :"));

# def promedio(valor1, valor2):
#   promedio = (valor1 + valor2) / 2.0;
#   print(f"Promedio: {promedio}");

# promedio(number1, number2);

# # * 2) Corregir el código para cumplir con la consigna.
# # * Crear una función que dados las medidas de 3 segmentos, devuelva True si se puede formar un
# # * triángulo y False si no se puede formar un triángulo con ellos.

# side1 = float(input("Ingrese el lado 1: "));
# side2 = float(input("Ingrese el lado 2: "));
# side3 = float(input("Ingrese el lado 3: "));

# def esTriangulo (ladoA, ladoB, ladoC):
# #   Si la suma de 2 lados en menor que el tercero, no se puede
# #  hacer un triángulo
#   if (ladoA + ladoB) > ladoC:
#     return True;
#   elif (ladoA + ladoC) > ladoB:
#     return True;
#   elif (ladoB + ladoC) > ladoA:
#     return True;
#   else:
#     return False;
  
# if (esTriangulo(side1, side2, side3)):
#   print("Se puede formar un triángulo");
# else:
#   print("No se puede formar un triángulo");

# # * 3) Dado un número, devolver True si es par, False si es impar

# number = int(input("Ingrese un número para saber si es par o impar: "));

# def parImpar (number):
#   if (number % 2 == 0):
#     print(f"El número {number} es par.");
#   else:
#     print(f"El número {number} es impar.");
    
# parImpar(number);

# #* 4) Dado dos números, devolver el mayor.

# number1 = int(input("Ingrese el 1er número: "));
# number2 = int(input("Ingrese el 2do número: "));

# def highestNumber (firstNumber, secondNumber):
#   print(f"El número de mayor denominación ingresado es: {max(firstNumber, secondNumber)}.");
  
# highestNumber(number1, number2);

# # 5) Dado 3 números, devolver el menor.

# number1 = int(input("Ingrese el 1er número: "));
# number2 = int(input("Ingrese el 2do número: "));
# number3 = int(input("Ingrese el 3er número: "));

# def lessNumber (firstNumber, secondNumber, thirdNumber):
#   print(f"El número de menor denominación ingresado es: {min(firstNumber, secondNumber, thirdNumber)}.");
  
# lessNumber(number1, number2, number3);

# #* 6) Dado 3 números, devolver el promedio.

# total = 0;

# for numbers in range(3):
#   numberToAdd = int(input(f"Ingrese el {int(numbers) + 1} número: "));
#   total += numberToAdd;

# def average (totalSum):
#   print(f"El promedio de los números ingresados es de: {totalSum / 3}.");
  
# average(total);

# #* 7) Dado un número, devolver True si es primo y False si no es primo.
 
# number = int(input("Ingrese un número para saber si es primo o no: "));

# def primoONo (number):
#   totalOfDivisors = 0;
  
#   for divisor in range(1, number + 1):
#     if (number % divisor == 0):
#       totalOfDivisors += 1;
  
#   if (totalOfDivisors == 2):
#     print(f"El número {number} es un número primo.");
#     return True;
#   else:
#     print(f"el número {number} no es un número primo.");
#     return False;
  
# primoONo(number);