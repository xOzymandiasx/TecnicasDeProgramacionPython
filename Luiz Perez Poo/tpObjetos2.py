#  #* Ejercicio 1 linked list;
 
# class Nodo:
#   def __init__(self, value) -> None:
#     self.value = value;
#     self.next = None;
    
# class LinkedList:
#   def __init__(self) -> None:
#     self.head = None;
    
# #Insertamos un nodo al principio/creamos cabecera;
#   def insertarAlPrincipio(self, value) -> None:
#     nuevoNodo = Nodo(value);
    
#     if self.head is None: #Si la cabecera no existe, se crea y con return salimos de la funcion;
#       self.head = nuevoNodo;
#       return;
    
#     nuevoNodo.next = self.head; #Si hay algo, lo existente pasa adelante y el nuevo nodo se transforma en la cabecera;
#     self.head = nuevoNodo;
    
#   def insertarNodoAlFinal(self, value) -> None:
#     nuevoNodo = Nodo(value);
    
#     if self.head is None:
#       self.head = nuevoNodo;
#       return;
    
#     current = self.head;
#     while current.next:
#       current = current.next;
      
#     current.next = nuevoNodo;

#   def buscarEnNodos(self, value) -> bool:
#     current = self.head;
#     currentNode = 1;
    
#     while current:
#       if current.value == value:
#         return True, f"Se encuentra en el nodo {currentNode}";
#       current = current.next;
#       currentNode += 1;
      
#     return False;
    
#   def borrarDato(self, value) -> None:
#     current = self.head;
    
#     if current.value == value:
#       self.head = current.next;
#       return;
    
#     while current:
#       if current.next.value == value and current.next.next is None:
#         current.next = None;
#         return;
#       if current.next.value == value and current.next.next is not None:
#         current.next = current.next.next;
#         return;
#       current = current.next;       
 
#   def listarLinkedList(self) -> list:
#     lista = [];
#     current = self.head;
    
#     while current:
#       lista.append(current.value);
#       current = current.next;
      
#     return lista;
    
#   def mostrarValores(self) -> None:
#     current = self.head;
#     while current:
#       print(current.value, "->", end= " ");
#       current = current.next;

#* Ejercicio 2 binary tree;

class TreeNode:
  def __init__(self, value:int) -> None:
    self.value = value;
    self.left = None;
    self.right = None;
    
class BinaryTree:
  def __init__(self, value:int) -> None:
    self.head = TreeNode(value);
    
  def agregarNodo(self, nodoActual, nodo: TreeNode) -> None: 
    if nodo.value < nodoActual.value:
      if nodoActual.left is None:
        nodoActual.left = nodo;
      else:
        self.agregarNodo(nodoActual.left, nodo);       
    else:
      if nodoActual.right is None:
        nodoActual.right = nodo;
      else:
        self.agregarNodo(nodoActual.right, nodo);
  
  def buscar(self, nodoActual, value: int) -> bool:
    if nodoActual is None:
        return False;
    if nodoActual.value == value:
        return True;
    elif value < nodoActual.value:
        return self.buscar(nodoActual.left, value);
    else:
        return self.buscar(nodoActual.right, value);

  def listar(self) -> list:
    lista = [];
    self.ordenar(self.head, lista);
    return lista;
    
  def ordenar(self, nodoActual, valores:list)-> None:
    if nodoActual is not None:
      self.ordenar(nodoActual.left, valores);
      valores.append(nodoActual.value);
      self.ordenar(nodoActual.right, valores);
      

  def borrar(self,nodoActual, value) -> TreeNode:
    if nodoActual is None:
      return nodoActual;
    
    if value < nodoActual.value:
      nodoActual.left = self.borrar(nodoActual.left, value);
    elif nodoActual.value > value:
      nodoActual.right = self.borrar(nodoActual.right, value);
    else:
      if nodoActual.left is None and nodoActual.right is None:
        return None;
      elif nodoActual.left is None:
        return nodoActual.right;
      elif nodoActual.right is None:
        return nodoActual.left;
      
    return nodoActual;

bt = BinaryTree(20);
nodo1 = TreeNode(15);
nodo2 = TreeNode(10);
nodo3 = TreeNode(5);
nodo4 = TreeNode(22);
bt.agregarNodo(bt.head, nodo1);
bt.agregarNodo(bt.head, nodo2);
bt.agregarNodo(bt.head, nodo3);
bt.agregarNodo(bt.head, nodo4);
print(bt.listar());