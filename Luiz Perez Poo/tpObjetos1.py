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
  def __init__(self, largo: int, ancho: int, aberturas: int = 0) -> None:
    self.largo = largo;
    self.ancho = ancho;
    while aberturas > 4:
      aberturas = int(input("No puedes tener más de 4 aberturas, reingrese el valor: "));
    self.aberturas = aberturas;

class Pintor:
  def __init__(self, cantHab) -> None:
    self.habitaciones = [];
    for _ in range(cantHab):
      self.habitaciones.append(Habitacion());
  
  def supHabitacion() -> int:
    
    pass

room = Habitacion(21, 34, 5);
print(room.aberturas);