                                      #! Variables, tipos de datos atómicos y operaciones

#* 1
a = int(input("Ingrese el primer número: "));
b = int(input("Ingrese el segundo número: "));
c = int(input("Ingrese el tercer número: "));
total = a + b + c;
print("Suma:", total);

#* 2
dividendo = float(input("Ingrese el Dividendo: "));
divisor = float(input("Ingrese el divisor: "));
resultado = dividendo / divisor;
print("División: ", resultado);

#* 3
num1 = int(input("Ingrese el primer número: "));
num2 = int(input("Ingrese el segundo número: "));
total = num1 + num2;
print("Resultado de la suma: ", total);

#* 4
num1 = float(input("Ingrese el primer número: "));
num2 = float(input("Ingrese el segundo número: "));
total = num1 * num2;
print("Resultado de la multiplicación: ", total);

#* 5
num1 = int(input("Ingrese el primer número: "));
num2 = float(input("Ingrese el segundo número: "));
total = num2 / num1;
print("Resultado de la división: ", total);

#* 6
text1 = input("Ingrese el primer texto: ");
text2 = input("Ingrese el segundo texto: ");
textAdd = text1 + " " + text2;
print(textAdd);

#* 7
age = int(input("Ingrese su edad: "));
livedDecades = list(str(age))[0];
if(age < 10):
  print("Usted todavía no llegó a vivivir una década");
else:
  print("Usted vivió", livedDecades, "década/s.");

#* 8
age = int(input("Ingrese su edad: "));
livedDays = age * 365;
print("Usted vivió", livedDays, "días.");

#* 9
livedDays = int(input("Ingrese su edad en días: "));
livedAges = int(livedDays / 365);
print("Usted vivió", livedAges, "año/s.");