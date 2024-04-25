# # 1) Realizar un programa para calcular el monto total a pagar por cada mesa en un restaurante. Realizar el
# # programa usando objetos para almacenar la información de los pedidos de cada mesa y calcular el importe
# # total a pagar. ¿Qué estructura de datos necesita para almacenar la información? 

# class Mesa:
#   def __init__(self) -> None:
#     self.pedidos = [];

# # *Lista pedidos; 
#   def listaPedidos(self) -> None:
#     return self.pedidos;

# # *Pedidos;
#   def pedido(self, nPedido: str, precio: float) -> None:
#     self.pedidos.append({"pedido": nPedido, "precio": precio});

# class Restaurant:
#   def __init__(self, cantidad: int) -> None:
#     self.mesas = [];
#     for _ in range(cantidad):
#       self.mesas.append(Mesa());

# # *Agregar pedido a Mesa; 
#   def agregarPedido(self, nPedido: str, precio: float, id: int) -> None:
#     self.mesas[id].pedido(nPedido, precio);

# # *Monto a pagar de la mesa elegida;
#   def montoPagar(self, nMesa: int) -> int:
#     total = 0;
#     for pedidos in self.mesas[nMesa].listaPedidos():
#       total += pedidos["precio"];
#     return total;

# # *Tests
# resto = Restaurant(5);
# resto.agregarPedido("Mila", 100, 1);
# resto.agregarPedido("Mila", 500, 1);
# print(resto.mesas[1].listaPedidos());
# print(resto.montoPagar(1));

# # 2) Realizar un programa que ayude al pintor a realizar el presupuesto. El programa debe calcular la superficie
# # total a pintar y la cantidad de litros de pintura, de una cantidad indeterminada de habitaciones. Cada
# # pared puede tener una abertura (puertas, ventanas, etc.), o no tener ninguna abertura. Las aberturas no
# # se pintan, restar su superficie de las paredes a pintar.
# # ¿Qué estructura de datos necesita para almacenar la información?
# # Realizar el programa usando objetos para almacenar la información de las habitaciones. Está prohibido el
# # uso de las instrucciones print() e input() dentro de las clases (capricho del profesor).
  
# class Habitacion:
#   def __init__(self, largo: float, alto: float) -> None:
#     self.largo = largo;
#     self.ancho = alto;
#     self.aberturas = [];

# # *Superficie habitación;  
#   def supHabitacion(self) -> float:
#     return self.largo * self.ancho;
 
# # *Agregar aberturas; 
#   def agregarAbertura(self, abertura: {float}) -> None:
#     if len(self.aberturas) >= 4:
#       pass;
#     else:
#       self.aberturas.append(abertura);

# # *Superficie total de aberturas; 
#   def supAberturas(self) -> float:
#     total = 0;
#     for abertura in self.aberturas:
#       total += abertura["largo"] * abertura["alto"];
#     return total;

# # *Cálculo superficie total a pintar; 
#   def supTotal(self) -> float:
#     return self.supHabitacion() - self.supAberturas();

# class Pintor:
#   def __init__(self) -> None:
#     self.habitaciones = [];
    
# # *Agregar habitaciones 
#   def agregarHabitaciones(self, habitacion: Habitacion) -> None:
#     self.habitaciones.append(habitacion);
 
# # *Agregar aberturas; 
#   def agAbertura(self, ubicacion: int, largo: float, alto: float) -> None:
#     self.habitaciones[ubicacion].agregarAbertura({"largo": largo, "alto": alto});

# # *Superficie total a pintar de las habitaciones; 
#   def calSupTotal(self) -> float:
#     total = 0;
#     for habitacion in self.habitaciones:
#       total += habitacion.supTotal();
#     return total;

# # *Calculo de rendimineto de pintura; 
#   def cantValPintura(self, rendimiento: float) -> float:
#     return self.calSupTotal() / rendimiento;

# # *Tests  
# pintor = Pintor();
# pintor.agregarHabitaciones(Habitacion(3, 3));
# pintor.agregarHabitaciones(Habitacion(3, 3));
# pintor.agAbertura(0, 2, 2);
# pintor.agAbertura(0, 2, 2);
# pintor.agAbertura(0, 2, 2);
# pintor.agAbertura(0, 2, 2);
# pintor.agAbertura(0, 2, 2);
# print(pintor.habitaciones[0].aberturas);
# print(pintor.habitaciones[0].supAberturas());
# print(pintor.habitaciones[0].supTotal());
# print(pintor.calSupTotal());
# print(pintor.cantValPintura(2));

# # 3) Realizar el programa usando objetos. Está prohibido el uso de las instrucciones print() e input() dentro de
# # las clases (capricho del profesor).
# # El programa debe permitir:
# # A) Cargar países, almacenando el nombre, el nombre de su capital y su población.
# # B) Cargar los países limítrofes a un país ya cargado. Los países limítrofes deben ser objetos ya creados en el
# # punto A. Cuando al país A, se le carga el país limítrofe B, automáticamente se cargue en el país B, el país
# # limítrofe A. Es decir, si a Argentina le cargamos el país limítrofe Uruguay, automáticamente se debe cargar
# # a Uruguay el país limítrofe Argentina.
# # D) El usuario selecciona un país, y el programa muestra todos sus países limítrofes.
# # ¿Qué estructura de datos necesita para almacenar la información? ¿Cuántas clases son necesarias? ¿Cómo
# # codificar la información?

# class Pais:
#   def __init__(self, nombre: str, capital: str, poblacion: int) -> None:
#     self.nombre = nombre;
#     self.capital = capital;
#     self.poblacion = poblacion;
#     self.limitrofes = [];

# class Mapa:
#   def __init__(self) -> None:
#     self.paises = [];

# # *Funcion para cargar paises(objetos); 
#   def cargarPais(self, pais: Pais) -> None:
#     for value in self.paises:
#       if value.nombre == pais.nombre.capitalize(): return "El país ya existe";
      
#     self.paises.append(pais);
    
# # *Funcion para agregar limítrofes;
#   def limitrofes(self, pais: str, limitrofe: str) -> None:
#     existe = False;
#     limit = False;
#     for values in self.paises:
#       if pais.capitalize() in values.nombre:
#         existe = True;
#         break;
#     for values in self.paises:
#       if limitrofe.capitalize() in values.nombre:
#         limit = True;
#         break;
      
#     if existe and limit:
#       for values in self.paises:
#         if pais == values.nombre and limitrofe not in values.limitrofes:
#           values.limitrofes.append(limitrofe.capitalize());
#         elif limitrofe == values.nombre and pais not in values.limitrofes:
#           values.limitrofes.append(pais.capitalize());
          
# # *Funcion para seleccionar paises limítrofes;
#   def selectLimitrofes(self, nombre: str) -> object:
#     for value in self.paises:
#       if value.nombre == nombre.capitalize(): return value.limitrofes;

# #* Tests  
# nPais = input("Ingrese el nombre del pais: ");
# cPais = input("Ingrese la capital del pais: ");
# pPais = input("Ingrese la poblacion del pais: ");
# argentina = Pais("Argentina", "Buenos Aires", 46000000);
# uruguay = Pais("Uruguay", "Montevideo", 4500000);
# chile = Pais("Chile", "Santiago", 2500000);
# mundi = Mapa();
# mundi.cargarPais(argentina);
# mundi.cargarPais(uruguay);
# mundi.cargarPais(uruguay);
# mundi.cargarPais(chile);
# mundi.cargarPais(Pais(nPais, cPais, pPais));
# print(mundi.paises);
# mundi.limitrofes("Argentina", "Uruguay");
# mundi.limitrofes("Argentina", "Uruguay");
# mundi.limitrofes("Argentina", "Chile");
# paisesLimitrofes = input("Elija el pais del cual quiera ver sus paises limitrofes: ");
# print(mundi.selectLimitrofes(paisesLimitrofes));
# print(mundi.selectLimitrofes("Argentina"));
# print(mundi.paises[0].limitrofes);
# print(mundi.paises[1].limitrofes);