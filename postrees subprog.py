class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def agregar_ingrediente(self, nombre):
        nuevo = NodoIngrediente(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar_ingrediente(self, nombre):
        actual = self.cabeza
        previo = None
        while actual and actual.nombre != nombre:
            previo = actual
            actual = actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente

    def mostrar_ingredientes(self):
        ingredientes = []
        actual = self.cabeza
        while actual:
            ingredientes.append(actual.nombre)
            actual = actual.siguiente
        return ingredientes

    def eliminar_duplicados(self):
        """Elimina ingredientes duplicados de la lista enlazada."""
        ingredientes_vistos = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.nombre in ingredientes_vistos:
                previo.siguiente = actual.siguiente
            else:
                ingredientes_vistos.add(actual.nombre)
                previo = actual
            actual = actual.siguiente

class Postres:
    def __init__(self):
        self.postres = {}

    def agregar_postre(self, nombre, ingredientes):
        if nombre in self.postres:
            print("El postre ya existe.")
        else:
            lista = ListaIngredientes()
            for ing in ingredientes:
                lista.agregar_ingrediente(ing)
            self.postres[nombre] = lista
            print(f"Postre '{nombre}' agregado correctamente.")

    def eliminar_postre(self, nombre):
        if nombre in self.postres:
            del self.postres[nombre]
            print(f"Postre '{nombre}' eliminado correctamente.")
        else:
            print("El postre no existe.")

    def mostrar_ingredientes(self, nombre):
        if nombre in self.postres:
            print(f"Ingredientes de '{nombre}': {', '.join(self.postres[nombre].mostrar_ingredientes())}")
        else:
            print("El postre no existe.")

    def agregar_ingrediente(self, nombre, ingrediente):
        if nombre in self.postres:
            self.postres[nombre].agregar_ingrediente(ingrediente)
            print(f"Ingrediente '{ingrediente}' agregado a '{nombre}'.")
        else:
            print("El postre no existe.")

    def eliminar_ingrediente(self, nombre, ingrediente):
        if nombre in self.postres:
            self.postres[nombre].eliminar_ingrediente(ingrediente)
            print(f"Ingrediente '{ingrediente}' eliminado de '{nombre}'.")
        else:
            print("El postre no existe.")
    
    def eliminar_duplicados_postres(self):
        """Elimina ingredientes duplicados de todos los postres."""
        for nombre in self.postres:
            self.postres[nombre].eliminar_duplicados()
        print("Se han eliminado los ingredientes duplicados de todos los postres.")


def menu():
    tiendita = Postres()
    while True:
        print("\nMenú:")
        print("1. Agregar un postre")
        print("2. Eliminar un postre")
        print("3. Mostrar ingredientes de un postre")
        print("4. Agregar ingrediente a un postre")
        print("5. Eliminar ingrediente de un postre")
        print("6. Eliminar ingredientes duplicados de todos los postres")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del postre: ")
            ingredientes = input("Ingrese los ingredientes separados por comas: ").split(",")
            tiendita.agregar_postre(nombre.strip(), [i.strip() for i in ingredientes])
        
        elif opcion == "2":
            nombre = input("Ingrese el nombre del postre a eliminar: ")
            tiendita.eliminar_postre(nombre.strip())
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del postre: ")
            tiendita.mostrar_ingredientes(nombre.strip())
        
        elif opcion == "4":
            nombre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a agregar: ")
            tiendita.agregar_ingrediente(nombre.strip(), ingrediente.strip())
        
        elif opcion == "5":
            nombre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a eliminar: ")
            tiendita.eliminar_ingrediente(nombre.strip(), ingrediente.strip())
        
        elif opcion == "6":
            tiendita.eliminar_duplicados_postres()
        
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()