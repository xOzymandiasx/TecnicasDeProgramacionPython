# #  # * 1) Realizar el programa que despliegue un menú en pantalla y pida al usuario que seleccione una opción del menú. Si la opción es válida, informa la opción seleccionada, Si la opción es invalida, pide que la ingrese nuevamente. Las opciones del menú son: Nuevo, Editar, Borrar y Salir
 
# def menu(a = ""):
#   print(f"""Seleccione una opción del menú:
# A) {"->" if a=="a" else ""} Nuevo 
# B) {"->" if a=="b" else ""} Editar 
# C) {"->" if a=="c" else ""} Borrar 
# D) {"->" if a=="d" else ""} Salir""");
  
#   inputChoice = input("Ingrese el comando (A, B...): ").lower().strip();

#   while True:
#     if (inputChoice == "a" or inputChoice == "b" or inputChoice == "d" or inputChoice == "c"): break;
#     inputChoice = input(f"'{inputChoice}' no es una opción válida, vuelva a ingresarla: ").lower().strip();
  
#   if(inputChoice == "a"):
#     print(f"Seleccionaste: Nuevo.");
#     menu(inputChoice);
#   elif(inputChoice == "b"):
#     print(f"Seleccionaste: Editar.");
#     menu(inputChoice);
#   elif(inputChoice == "c"):
#     print(f"Seleccionaste: Borrar.");
#     menu(inputChoice);
#   elif(inputChoice == "d"):
#     print(f"Seleccionaste: Salir.");
#     menu(inputChoice);

# menu();


# # * 2) Realizar una función que despliegue un menú en pantalla y pida al usuario que seleccione una opción del menú, la función debe devolver un código de la opción seleccionada (puede ser un carácter con la inicial de la opción seleccionada, o un entero de la opción seleccionada). Las opciones del menú son: Nuevo, Editar, Borrar y Salir.

# def menu():
#   print(f"""Seleccione una opción del menú:
# A) Nuevo 
# B) Editar 
# C) Borrar 
# D) Salir""");
  
#   inputChoice = input("Ingrese el comando (A, B...): ").lower().strip();
  
#   if(inputChoice == "a"):
#     print(f"Seleccionaste: Nuevo.");
#     return "N";
#   elif(inputChoice == "b"):
#     print(f"Seleccionaste: Editar.");
#     return "E";
#   elif(inputChoice == "c"):
#     print(f"Seleccionaste: Borrar.");
#     return "B";
#   elif(inputChoice == "d"):
#     print(f"Seleccionaste: Salir.");
#     return "S";
#   else:
#     print(f"'{inputChoice}' no es una opción válida, vuelva a reingresarla.");
#     return menu();
     
# print(menu());


# # * 3) Realizar una función que despliegue un menú en pantalla y pida al usuario que seleccione una opción del menú. A la función se le pasa (como parámetro de la función) un diccionario donde la clave es el valor que debe devolver si se selecciona esa opción y el dato es el texto que debe mostrar el menú. La función debe devolver la clave de la opción seleccionada por el usuario. Ejemplo de implementación (falta completar la función):
# #? def menu(diccionario):
# #?  ….. #Completar el código de la función
# #?  return key
# #? Programa principal
# #? menu_principal={‘N’:’Nuevo’, ‘E’:’Editar’, ‘B’:’Borrar’, ‘S’:’Salir’}
# #? opción=menu(menú_principal)
# #? print(“Opción seleccionada:”,opción)
# #? Debe funcionar para los siguientes ejemplos:
# #? menu_principal={‘N’:’Nuevo’, ‘E’:’Editar’, ‘B’:’Borrar’, ‘I’:’Imprimir’, ‘S’:’Salir’}
# #? menú_clientes={‘N’:’Nuevo Cliente’,’B’:’Buscar Cliente’, ’A’:’Actualizar datos del cliente’, ’X’:’Borrar cliente’}

# menu_principal = {"N":"Nuevo", "E":"Editar", "B":"Borrar", "I":"Imprimir", "S":"Salir"};
# menu_clientes = {"N":"Nuevo Cliente","B":"Buscar Cliente", "A":"Actualizar datos del cliente", "X":"Borrar cliente"}

# def menu (data):
#   for choice in data:
#     print(f"{choice}) {data[choice]}");
  
#   inputChoice = input("Elija una de las opciones (N, B...): ");

#   for choice in data:
#     if (choice.lower() == inputChoice.lower().strip()):
#       print(f"Opción seleccionada: {data[choice]}");
#       return choice;

#   print(f"'{inputChoice}' no es una opción válida, vuelva a reingresarla.");
#   return menu(data);

# print(menu(menu_clientes));


# # * 4) Realizar una función que permita el ingreso de los datos de un cliente (Nombre de la empresa, Nombre del contacto y email). La función devuelve una Tupla con dichos datos en el orden indicado.

# def clientForm ():
#   companyName = input("Ingrese el nombre de la empresa: ");
#   contactName = input("Ingrese el nombre de la persona: ");
#   email = input("Ingrese el email de la persona: ");

#   return (companyName, contactName, email);

# print(clientForm());


# # * 5) Realizar una función que reciba 3 parametros día, mes y año (tipo de dato int) de una fecha y devuelva la fecha en formato ISO 8601. Si la fecha es válida, la función debe devolver la fecha con el tipo de dato string en formato ISO 8601. Si la fecha es invalida, la función debe devolver un None (Null).
# # ? Por ejemplo:
# # ? FechaISO(20,10,2020) debe devolver: “2020-10-20”
# # ? FechaISO(10,2,2020) debe devolver: “2020-02-10”
# # ? FechaISO(30,2,2020) debe devolver: None

# from datetime import datetime;

# def formatDate(day, month, year):
#   try:
#     date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d");
#     return date.date().strftime("%Y-%m-%d");
#   except ValueError:
#     return None;

# print(formatDate(20,10,2020));
# print(formatDate(10,2,2020));
# print(formatDate(30,2,2020));


# # * 6) Realizar una función para imprimir los datos de un producto. La función recibe una lista con los datos, y debe imprimirlos en pantalla. Los datos son Marca, Modelo, Precio y Stock disponible. Debe funcionar para los siguientes ejemplos:

# # ? Producto1=[“Samsung”, “LA5890”,12345,128]
# # ? Producto2=[“Samsung”, “LB001”,2550,205]
# # ? Producto3=[“Sony”, “A-1205N”,2550,0]
# Producto1 = ["Samsung", "LA5890",12345,128];
# Producto2 = ["Samsung", "LB001", 2550, 205];
# Producto3 = ["Sony", "A-1205N", 2550, 0];

# def printProductData (array):
#   print(f"""
#   Marca: {array[0]}
#   ------
#   Modelo: {array[1]}
#   ------
#   Precio: {array[2]}
#   ------
#   Stock: {array[3]}
#   """);

# printProductData(Producto1);
# printProductData(Producto2);
# printProductData(Producto3);


# # * 7) Realizar una función para imprimir un listado de productos. La función recibe una lista de tuplas conteniendo los datos de los productos a mostrar. Los datos son Marca, Modelo, Precio y Stock disponible.
# # * Debe funcionar para los siguientes ejemplos:
# # ? Lista1=[(“Samsung”, “LA5890”,12345,28),
# #  ? (“Samsung”, “LB001”,2550,205),
# #  ? (“LG”, “GL-2552”,25400,18)]

# # ? Lista2=[(“Sony”, “A-1205N”,2550,0)]

# # ? Lista3=[(“Samsung”, “LA5890”,12345,28),
# #  ? (“Samsung”, “LB001”,2550,205),
# #  ? (“LG”, “GL-2552”,25400,18),
# #  ? (“LG”, “GL-3250”,35200,28),
# #  ? (“LG”, “GL-5240S”,105800,0)]

# Lista1=[
#   ("Samsung", "LA5890",12345,28),
#   ("Samsung", "LB001",2550,205),
#   ("LG", "GL-2552",25400,18)
#    ];
# Lista2=[("Sony", "A-1205N",2550,0)];

# Lista3=[
#   ("Samsung", "LA5890",12345,28),
#  ("Samsung", "LB001",2550,205),
#  ("LG", "GL-2552",25400,18),
#  ("LG", "GL-3250",35200,28),
#  ("LG", "GL-5240S",105800,0)
#   ];

# Lista4=[];

# def printProductData (array):
#   for data in array:
#     print(f"""
#   Marca: {data[0]}
#   ------
#   Modelo: {data[1]}
#   ------
#   Precio: {data[2]}
#   ------
#   Stock: {data[3]}
#   """);

# printProductData(Lista1);
# printProductData(Lista2);
# printProductData(Lista3);
# printProductData(Lista4);