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
    
#   def supHabitacion(self) -> float:
#     return self.largo * self.ancho;
  
#   def agregarAbertura(self, abertura: {float}) -> None:
#     if len(self.aberturas) >= 4:
#       pass;
#     else:
#       self.aberturas.append(abertura);
    
#   def supAberturas(self) -> float:
#     total = 0;
#     for abertura in self.aberturas:
#       total += abertura["largo"] * abertura["alto"];
#     return total;
  
#   def supTotal(self) -> float:
#     return self.supHabitacion() - self.supAberturas();

# class Pintor:
#   def __init__(self) -> None:
#     self.habitaciones = [];
    
#   def agregarHabitaciones(self, habitacion: Habitacion) -> None:
#     self.habitaciones.append(habitacion);
    
#   def agAbertura(self, ubicacion: int, largo: float, alto: float) -> None:
#     self.habitaciones[ubicacion].agregarAbertura({"largo": largo, "alto": alto});
    
#   def calSupTotal(self) -> float:
#     total = 0;
#     for habitacion in self.habitaciones:
#       total += habitacion.supTotal();
#     return total;
  
#   def cantValPintura(self, rendimiento: float) -> float:
#     return self.calSupTotal() / rendimiento;
    
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

  
# def agAberturas(cantidad: int) -> None: #Funcion para agregar aaberturas a la clase habitacion
#   for value in range(cantidad):
#     largo = float(input(f"ingrese el largo de la abertura {value + 1}: "));
#     alto = float(input(f"ingrese el alto de la abertura {value + 1}: "));
#     abertura = Abertura(largo, alto);
#     room.agregarAbertura(abertura);

# pintoPintor = Pintor();
# pintoPintor.agregarHabitaciones(Habitacion(5, 6));
# print(pintoPintor.habitaciones);
# pintoPintor.habitaciones[0].agregarAbertura(Abertura(5, 3));
# print(pintoPintor.habitaciones[0].aberturas.supAbertura[0]());
# room = Habitacion(3, 3);
# agAberturas(2);
# print(room.aberturas);
# print(room.supHabitacion())


# 3) Realizar el programa usando objetos. Está prohibido el uso de las instrucciones print() e input() dentro de
# las clases (capricho del profesor).
# El programa debe permitir:
# A) Cargar países, almacenando el nombre, el nombre de su capital y su población.
# B) Cargar los países limítrofes a un país ya cargado. Los países limítrofes deben ser objetos ya creados en el
# punto A. Cuando al país A, se le carga el país limítrofe B, automáticamente se cargue en el país B, el país
# limítrofe A. Es decir, si a Argentina le cargamos el país limítrofe Uruguay, automáticamente se debe cargar
# a Uruguay el país limítrofe Argentina.
# D) El usuario selecciona un país, y el programa muestra todos sus países limítrofes.
# ¿Qué estructura de datos necesita para almacenar la información? ¿Cuántas clases son necesarias? ¿Cómo
# codificar la información?

class Pais:
  def __init__(self, nombre: str, capital: str, poblacion: int) -> None:
    self.nombre = nombre;
    self.capital = capital;
    self.poblacion = poblacion;
    self.limitrofes = [];

class Mapa:
  def __init__(self) -> None:
    self.paises = [];
    
  def cargarPais(self, pais: Pais) -> None:
    self.paises.append(pais);
    
  def limitrofes(self, pais: str, limitrofe: str) -> None:
    existe = False;
    limit = False;
    for values in self.paises:
      if pais in values.nombre:
        existe = True;
        break;
    for values in self.paises:
      if limitrofe in values.nombre:
        limit = True;
        break;
      
    if existe and limit:
      for values in self.paises:
        if pais == values.nombre and limitrofe not in values.limitrofes:
          values.limitrofes.append(limitrofe);
        elif limitrofe == values.nombre and pais not in values.limitrofes:
          values.limitrofes.append(pais);
  
argentina = Pais("Argentina", "Buenos Aires", 46000000);
uruguay = Pais("Uruguay", "Montevideo", 4500000);
mundi = Mapa();
mundi.cargarPais(argentina);
mundi.cargarPais(uruguay);
mundi.limitrofes("Argentina", "Uruguay");
mundi.limitrofes("Argentina", "Uruguay");
print(mundi.paises[0].limitrofes)
print(mundi.paises[1].limitrofes)
  
