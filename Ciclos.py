                                      #! Ciclos
                        
#* 1
for i in range (11):
 mutiplicacion = i * 4;
 print(i, "* 4 =", mutiplicacion);

#* 2
suma = 0;
while suma < 10:
 nuevo = int(input ("Ingrese un nuevo número: "));
 suma += nuevo;
 if (suma > 10):
  print ("La suma es: ", suma);

#* 3
for number in range(1, 12, 2):
  print(number, number + 1);

#* 4
for number in range(1, 7):
  print(number, number + 6);

#* 5
initialCount = None;
additionCount = 0;
while initialCount != 0:
  initialCount = int(input("Ingrese un numero a sumar: "));
  additionCount += initialCount;
  if (initialCount == 0):
    print("La suma de los valores ingresados es:", additionCount);

#* 6
def arrayCount(array):
  sum = 0;
  for numbers in array:
    sum += numbers;
  return sum;

arrayOfNumbers = [];

while arrayCount(arrayOfNumbers) < 20:
  numberToAdd = int(input("Ingrese un número: "));
  arrayOfNumbers.append(numberToAdd);

sumAverage = int(arrayCount(arrayOfNumbers) / len(arrayOfNumbers));

print("El promedio de los número ingresados es: ", sumAverage);