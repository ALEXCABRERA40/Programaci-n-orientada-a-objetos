class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                break

    def buscar_productos(self, nombre):
        return [p for p in self.productos if nombre in p.get_nombre()]

    def mostrar_productos(self):
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
def main():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar productos")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto (dejar en blanco para no cambiar): "))
            nuevo_precio = float(input("Ingrese el nuevo precio del producto (dejar en blanco para no cambiar): "))
            inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_productos(nombre)
            for p in productos:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
