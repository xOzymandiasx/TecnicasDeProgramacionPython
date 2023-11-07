#  # * 1) Realizar el programa que despliegue un menú en pantalla y pida al usuario que seleccione una opción del menú. Si la opción es válida, informa la opción seleccionada, Si la opción es invalida, pide que la ingrese nuevamente. Las opciones del menú son: Nuevo, Editar, Borrar y Salir
 
# def menu():
#   print(f"""            Seleccione una opción del menú:
#        ->|Nuevo| ->|Editar| ->|Borrar| ->|Salir|""");
  
#   inputChoice = input("Ingrese el comando: ").lower().strip();
  
#   if(inputChoice == "nuevo"):
#     print(f"Seleccionaste: {inputChoice.capitalize()}.");
#     menu();
#   elif(inputChoice == "editar"):
#     print(f"Seleccionaste: {inputChoice.capitalize()}.");
#     menu();
#   elif(inputChoice == "borrar"):
#     print(f"Seleccionaste: {inputChoice.capitalize()}.");
#     menu();
#   elif(inputChoice == "salir"):
#     print("Programa finalizado.");
#     return;
#   else:
#     print(f"'{inputChoice}' no es una opción válida, vuelva a reingresarla.");
#     menu();
     
# menu();


# # * 2) Realizar una función que despliegue un menú en pantalla y pida al usuario que seleccione una opción del menú, la función debe devolver un código de la opción seleccionada (puede ser un carácter con la inicial de la opción seleccionada, o un entero de la opción seleccionada). Las opciones del menú son: Nuevo, Editar, Borrar y Salir.

# def menu():
#   print(f"""            Seleccione una opción del menú:
#        ->|Nuevo| ->|Editar| ->|Borrar| ->|Salir|""");
  
#   inputChoice = input("Ingrese el comando: ").lower().strip();
  
#   if(inputChoice == "nuevo"):
#     print(f"Seleccionaste: {inputChoice.capitalize()}.");
#     return "N";
#   elif(inputChoice == "editar"):
#     print(f"Seleccionaste: {inputChoice.capitalize()}.");
#     return "E";
#   elif(inputChoice == "borrar"):
#     print(f"Seleccionaste: {inputChoice.capitalize()}.");
#     return "B";
#   elif(inputChoice == "salir"):
#     return "S";
#   else:
#     print(f"'{inputChoice}' no es una opción válida, vuelva a reingresarla.");
#     return menu();
     
# menu();


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
    
#   while True:
#     print("Seleccione una opción del menú: ");
#     for choice in data:
#       print(f"-> {data[choice]}");
      
#     inputChoice = input("Ingrese el comando: ");
    
#     for choice in data:
#       if (data[choice] == inputChoice.capitalize()):
#         return choice;
    
#     print(f"'{inputChoice}' no es una opción válida, vuelva a reingresarla.");
    
#   # inputChoice = input("Elija una de las opciones: ");

#   # for choice in data:
#   #   if (data[choice] == inputChoice.capitalize()):
#   #     print(type(choice)) 
#   #     return choice;

#   # print(f"'{inputChoice}' no es una opción válida, vuelva a reingresarla.");
#   # menu(data);

# print(menu(menu_clientes));


# # * 4) Realizar una función que permita el ingreso de los datos de un cliente (Nombre de la empresa, Nombre del contacto y email). La función devuelve una Tupla con dichos datos en el orden indicado.

# def clientForm ():
#   companyName = input("Ingrese el nombre de la empresa: ");
#   contactName = input("Ingrese el nombre de la persona: ");
#   email = input("Ingrese el email de la persona: ");

#   return (companyName, contactName, email);

# print(clientForm());


# * 5) Realizar una función que reciba 3 parametros día, mes y año (tipo de dato int) de una fecha y devuelva la fecha en formato ISO 8601. Si la fecha es válida, la función debe devolver la fecha con el tipo de dato string en formato ISO 8601. Si la fecha es invalida, la función debe devolver un None (Null).
# ? Por ejemplo:
# ? FechaISO(20,10,2020) debe devolver: “2020-10-20”
# ? FechaISO(10,2,2020) debe devolver: “2020-02-10”
# ? FechaISO(30,2,2020) debe devolver: None

from datetime import datetime;

def formatDate(day, month, year):
  try:
    date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d");
    return date.date().strftime("%Y-%m-%d");
  except ValueError:
    return None;
    

print(formatDate(2024, 2, 29));
print(formatDate(2023, 2, 29));