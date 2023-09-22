                                          #! Estructuras de control
                             
# *1
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

#* 2
# dominoStart = 0;

# while dominoStart < 7:
#   for numbers in range(dominoStart, 7):
#     print(f"{dominoStart}|{numbers}");
#   dominoStart += 1;

#* 3
#Datos para trabajar;
totalSeconds = int(input("Ingrese el tiempo en segundos:"));
totalMinutes = totalSeconds // 60;

#Lógica para convertir segundos a horas minutos y segundos;
hours = totalMinutes // 60;
minutes = totalMinutes - hours * 60;
seconds = totalSeconds - totalMinutes * 60;

#Lógica para convertir el horario al tipo de horario pedido;
if (len(str(hours)) == 1) : hours = f"0{hours}";
if (len(str(minutes)) == 1) : minutes = f"0{minutes}";
if (len(str(seconds)) == 1) : seconds = f"0{seconds}";
  
print(f"{hours}:{minutes}:{seconds}");










# for numbers in range(seconds):
#   print(numbers)
#   minutesCount += 1
#   if (minutesCount == 60):
#     minutes += 1;
  
#   if (minutes == 60):
#     minutes = 0;

# print(minutes)