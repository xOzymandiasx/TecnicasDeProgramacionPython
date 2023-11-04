 # * 1) Realizar el programa que despliegue un menú en pantalla y pida al usuario que seleccione una opción del menú. Si la opción es válida, informa la opción seleccionada, Si la opción es invalida, pide que la ingrese nuevamente. Las opciones del menú son: Nuevo, Editar, Borrar y Salir
 
def menu():
  print(f"""            Seleccione una opción del menú:
       ->|Nuevo| ->|Editar| ->|Borrar| ->|Salir|""");
  
  choice = input("Ingrese el comando: ");
  
  if(choice.lower == "nuevo"):
    print(f"seleccionaste: {choice}")
    
  
menu();