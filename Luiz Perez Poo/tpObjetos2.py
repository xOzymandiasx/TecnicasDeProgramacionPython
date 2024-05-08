 #* Ejercicio 1 linked list;
 
class Nodo:
  def __init__(self, value) -> None:
    self.value = value;
    self.next = None;
    
class LinkedList:
  def __init__(self) -> None:
    self.head = None;
    
#Insertamos un nodo al principio/creamos cabecera;
  def insertarAlPrincipio(self, value) -> None:
    nuevoNodo = Nodo(value);
    
    if self.head is None: #Si la cabecera no existe, se crea y con return salimos de la funcion;
      self.head = nuevoNodo;
      return;
    
    nuevoNodo.next = self.head; #Si hay algo, lo existente pasa adelante y el nuevo nodo se transforma en la cabecera;
    self.head = nuevoNodo;
    
  def insertarNodoAlFinal(self, value) -> None:
    nuevoNodo = Nodo(value);
    
    if self.head is None:
      self.head = nuevoNodo;
      return;
    
    current = self.head;
    while current.next:
      current = current.next;
      
    current.next = nuevoNodo;

  def buscarEnNodos(self, value) -> bool:
    current = self.head;
    currentNode = 1;
    
    while current:
      if current.value == value:
        return True, f"Se encuentra en el nodo {currentNode}";
      current = current.next;
      currentNode += 1;
      
    return False;
    
  def borrarDato(self, value) -> None:
    current = self.head;
    
    while current:
      if current.value == value:
        current.value = None                          #! Estoy por esta parte del código;
        return;
      current = current.next;
    
  def mostrarValores(self) -> None:
    current = self.head;
    while current:
      print(current.value, "->", end= " ");
      current = current.next;
      
listaLinkeada = LinkedList();
listaLinkeada.insertarAlPrincipio(78);
listaLinkeada.insertarNodoAlFinal(89);
listaLinkeada.insertarNodoAlFinal(89);
listaLinkeada.insertarNodoAlFinal("hola");
print(listaLinkeada.buscarEnNodos(59));
print(listaLinkeada.buscarEnNodos("hola"));
listaLinkeada.mostrarValores();