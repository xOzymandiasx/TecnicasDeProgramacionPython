# # 1) Realizar un programa para calcular el monto total a pagar por cada mesa en un restaurante. Realizar el
# # programa usando objetos para almacenar la información de los pedidos de cada mesa y calcular el importe
# # total a pagar. ¿Qué estructura de datos necesita para almacenar la información? 

# class Mesa:
#   def __init__(self) -> None:
#     self.pedidos = [];
  
#   def listaPedidos(self) -> None:
#     return self.pedidos;

#   def pedido(self, nPedido: str, precio: float) -> None:
#     self.pedidos.append({"pedido": nPedido, "precio": precio});

# class Restaurant:
#   def __init__(self, cantidad: int) -> None:
#     self.mesas = [];
#     for _ in range(cantidad):
#       self.mesas.append(Mesa());
  
#   def agregarPedido(self, nPedido: str, precio: float, numero: int) -> None:
#     self.mesas[numero].pedido(nPedido, precio)
#     pass

#   def montoPagar(self, nMesa: int) -> int:
#     total = 0;
#     for pedidos in self.mesas[nMesa].listaPedidos():
#       total += pedidos["precio"];
#     return total;

# resto = Restaurant(5);
# resto.agregarPedido("Mila", 100, 1);
# resto.agregarPedido("Mila", 500, 1);
# print(resto.mesas[1].listaPedidos());
# print(resto.montoPagar(1));

# 2) Realizar un programa que ayude al pintor a realizar el presupuesto. El programa debe calcular la superficie
# total a pintar y la cantidad de litros de pintura, de una cantidad indeterminada de habitaciones. Cada
# pared puede tener una abertura (puertas, ventanas, etc.), o no tener ninguna abertura. Las aberturas no
# se pintan, restar su superficie de las paredes a pintar.
# ¿Qué estructura de datos necesita para almacenar la información?
# Realizar el programa usando objetos para almacenar la información de las habitaciones. Está prohibido el
# uso de las instrucciones print() e input() dentro de las clases (capricho del profesor).

class Habitacion:
  def __init__(self, largo: int, alto: int, aberturas: int = 0) -> None:
    self.largo = largo;
    self.ancho = alto;
    while aberturas > 4:
      aberturas = int(input("No puedes tener más de 4 aberturas, reingrese el valor: "));
    self.aberturas = aberturas;
    
  def supHabitacion(self) -> int:
    return self.largo * self.ancho;
  
  def supAberturas(self) -> int:
    totalAberturas = 0
    for nAbertura in range(self.aberturas):
      largo = int(input(f"ingrese el largo de la abertura {nAbertura + 1}: "));
      alto = int(input(f"Ingrese el alto de la abertura {nAbertura + 1}: "));
      totalAberturas += largo * alto;
      
    return totalAberturas;

class Pintor:
  def __init__(self) -> None:
    self.habitaciones = [];
    
  def agregarHabitaciones(self, cantidad: int) -> None:
    for habitacion in range(cantidad):
      pass
  

room = Habitacion(3, 3, 2);
print(room.supHabitacion())
print(room.aberturas);
print(room.supAberturas())

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
#     self.limitrifes = [];

# class Mapa:
#   def __init__(self) -> None:
#     self.paises = [];
    
#   def cargarPais(self, pais: Pais) -> None:
#     self.paises.append(pais);
    
#   def limitrofes(self, limitrofe: str, pais: Pais) -> None:
#     for paises in self.paises:
#       return paises
    
# argentina = Pais("Argentina", "Buenos Aires", 46000000);
# uruguay = Pais("Uruguay", "Montevideo", 4500000);
# mundi = Mapa();
# mundi.cargarPais(argentina);
# mundi.cargarPais(uruguay);
# print(mundi.paises.nombre)
# # print(mundi.limitrofes())
  
