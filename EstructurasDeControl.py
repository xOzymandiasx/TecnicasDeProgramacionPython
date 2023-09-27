                                         # #! Estructuras de control
                             
# # *1
# day = int(input("Ingrese el día: "));
# month = int(input("Ingrese el mes: "));
# year = int(input("Ingrese el año: "));

# pairMonths = [4, 6, 9, 11];
# oddMonths = [1, 3, 5, 7, 8, 10, 12];
# februaryMotnh = month == 2;

# def findOddMonths (month):
#   for months in oddMonths:
#    if (months == month):
#      return True;
   
#   return False;

# def findPairMotnhs (month):
#   for months in pairMonths:
#    if (months == month):
#      return True;
   
#   return False;

# def leapYear (year):
#   if (year % 4 == 0):
#     return True;
#   else:
#     return False;

# februaryDays = day >= 1 and day <= 28 or (day == 29 and leapYear(year));
# daysInOddMonths = day >= 1 and day <= 31;
# daysInPairMoths = day >= 1 and day <= 30;


# if ( daysInOddMonths and findOddMonths(month)):
#   print("Fecha válida");
# elif (daysInPairMoths and findPairMotnhs(month)):
#   print("Fecha válida");
# elif (februaryDays and februaryMotnh):
#   print("Fecha válida");
# else:
#   print("Fecha no válida");

# #* 2
# dominoStart = 0;

# while dominoStart < 7:
#   for numbers in range(dominoStart, 7):
#     print(f"{dominoStart}|{numbers}");
#   dominoStart += 1;

# #* 3
# #Datos para trabajar;
# totalSeconds = int(input("Ingrese el tiempo en segundos:"));
# totalMinutes = totalSeconds // 60;

# #Lógica para convertir segundos a horas minutos y segundos;
# hours = totalMinutes // 60;
# minutes = totalMinutes - hours * 60;
# seconds = totalSeconds - totalMinutes * 60;

# #Lógica para convertir el horario al tipo de horario pedido;
# if (len(str(hours)) == 1) : hours = f"0{hours}";
# if (len(str(minutes)) == 1) : minutes = f"0{minutes}";
# if (len(str(seconds)) == 1) : seconds = f"0{seconds}";
  
# print(f"{hours}:{minutes}:{seconds}");

# #* 4
# # Datos para trabajar;
# packageWeight = int(input("Ingrese peso del paquete a llenar: "));
# cokiesCount = 0;
# programStatus = True;

# while programStatus != False:       #Ingreso de datos y consiguiente suma;
#   cokies = int(input("Ingrese peso de galletitas a agregar al paquete: "));
#   changePackage = None;
  
#   cokiesCount += cokies;
#                                     #Comprobaciones cuando el paquete se llena;
#   if (packageWeight <= cokiesCount):
#     while True:
#       if (changePackage == None):
#         changePackage = input("Paquete lleno, introduszca 'next' para poner el proximo o 'exit' para salir: ");
#       else:
#         changePackage = input(f"{changePackage} es una palabra errónea, por favor vuelva a ingresarla: ");
#                                         #Reinicio o salida del programa;
#       if (changePackage.lower() == "next"):
#         cokiesCount = 0;
#         break;
#       elif (changePackage.lower() == "exit"):
#         print("Programa terminado.");
#         programStatus = False;
#         break;
    
# #* 5
# silo = int(input("Ingrese la capacidad del silo: "));
# flour = 0;

# while flour < silo:
#   flour = int(input("Ingrese cantidad de harina requerida para la preparación: "));

#   if (silo - flour >= 0):
#     print("Hay suficiente harina para realiazr la preparación.");
#     silo -= flour;
#     flour = 0;
#   else:
#     print(f"Cantidad insuficiente. Quedan en el silo: {silo} de harina");
#     flour = 0;

# print("Harina del silo terminada");