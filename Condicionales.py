                                            #! Condicionales
                                                  
#* 1
edad = int(input("Ingrese su edad: "));
if (edad >= 16):
 print("La edad es:",edad);

#* 2
dado1 = int(input("Ingrese el valor del 1er dado: "));
dado2 = int(input("Ingrese el valor del 2do dado: "));
suma = dado2 + dado1;
if (suma >= 7):
  print("La suma es mayor a 7");
else:
  print("La suma es menor a 7");

#* 3
age = int(input("Ingrese su edad: "));
if (age < 18):
  print("Debe ser mayor de 18 años");

#* 4
age = int(input("Ingrese su edad: "));
if (age < 18):
  print("Debe ser mayor de 18 años.");
else:
  name = input("Ingrese nombre y apellido: ");

#* 5
age = int(input("Ingrese su edad: "));
if (age < 16):
  print("Debe ser mayor de 16 años.");
elif (age >= 16 and age < 18):
  minorName = input ("Ingrese nombre del menor: ");
  adultName = input("Ingrese nombre del adulto responsable: ");
else:
  youngName = input ("Ingrese su nombre: ");


#* 6
name = input("Ingrese su nombre: ");
age = int(input("Ingrese su edad: "));
if (age >= 16):
  print("Bienvenido", name);
else:
  print("Debe ser mayor de 16 años.");

#* 7
num1 = float(input("Ingrese el 1er número: "));
num2 = float(input("Ingrese el 2do número: "));
num3 = float(input("Ingrese el 3er número: "));
average = (num1 + num2 + num3) / 3;
if (average < 4):
  print("Estás desaprobado.");
elif (average >= 4 and average < 7):
  print("Deberás rendir el final.");
else:
  print("Promocionaste con", average);
