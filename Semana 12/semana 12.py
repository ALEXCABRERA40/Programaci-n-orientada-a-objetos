class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.info[0]

    @property
    def autor(self):
        return self.info[1]

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"

    def __repr__(self):
        return self.__str__()


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

    def __repr__(self):
        return self.__str__()


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros por ISBN
        self.usuarios = set()  # Conjunto de IDs de usuarios

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido correctamente.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros[isbn]
            del self.libros[isbn]
            print(f"Libro '{libro.titulo}' eliminado correctamente.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in {u.user_id for u in self.usuarios}:
            self.usuarios.add(usuario)
            print(f"Usuario {usuario.nombre} registrado correctamente.")
            return True
        print(f"El usuario con ID {usuario.user_id} ya existe.")
        return False

    def dar_baja_usuario(self, user_id):
        usuario = self.buscar_usuario(user_id)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario {usuario.nombre} dado de baja correctamente.")
            return True
        print(f"No se encontró un usuario con ID {user_id}.")
        return False

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros and usuario in self.usuarios:
            libro = self.libros[isbn]
            if libro not in usuario.libros_prestados:
                usuario.prestar_libro(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
                return True
            print(f"El libro '{libro.titulo}' ya está prestado a {usuario.nombre}.")
        else:
            print("No se pudo realizar el préstamo. Verifique el ISBN o el usuario.")
        return False

    def devolver_libro(self, usuario, isbn):
        if isbn in self.libros:
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados:
                usuario.devolver_libro(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                return True
            print(f"El libro '{libro.titulo}' no estaba prestado a {usuario.nombre}.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")
        return False

    def buscar_libros(self, termino, tipo='titulo'):
        resultados = []
        for libro in self.libros.values():
            if tipo == 'titulo' and termino.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif tipo == 'autor' and termino.lower() in libro.autor.lower():
                resultados.append(libro)
            elif tipo == 'categoria' and termino.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def buscar_usuario(self, user_id):
        for usuario in self.usuarios:
            if usuario.user_id == user_id:
                return usuario
        return None

    def listar_libros_prestados(self, usuario):
        return usuario.libros_prestados

    def mostrar_libros_disponibles(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Libros disponibles:")
            for libro in self.libros.values():
                print(libro)

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for usuario in self.usuarios:
                print(usuario)


def menu_biblioteca():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Mostrar libros disponibles")
        print("9. Mostrar usuarios")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == '2':
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '3':
            nombre = input("Ingrese el nombre del usuario: ")
            user_id = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, user_id)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':
            user_id = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)

        elif opcion == '5':
            user_id = input("Ingrese el ID del usuario: ")
            usuario = biblioteca.buscar_usuario(user_id)
            if usuario:
                isbn = input("Ingrese el ISBN del libro a prestar: ")
                biblioteca.prestar_libro(usuario, isbn)
            else:
                print("Usuario no encontrado.")

        elif opcion == '6':
            user_id = input("Ingrese el ID del usuario: ")
            usuario = biblioteca.buscar_usuario(user_id)
            if usuario:
                isbn = input("Ingrese el ISBN del libro a devolver: ")
                biblioteca.devolver_libro(usuario, isbn)
            else:
                print("Usuario no encontrado.")

        elif opcion == '7':
            tipo = input("Buscar por (titulo/autor/categoria): ")
            termino = input("Ingrese el término de búsqueda: ")
            resultados = biblioteca.buscar_libros(termino, tipo)
            if resultados:
                print("Resultados de la búsqueda:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        elif opcion == '8':
            biblioteca.mostrar_libros_disponibles()

        elif opcion == '9':
            biblioteca.mostrar_usuarios()

        elif opcion == '10':
            print("Saliendo del sistema de biblioteca...")
            break

        else:
            print("Opción inválida. Por favor, intente nuevamente.")


# Ejecutar el menú de la biblioteca
if __name__ == "__main__":
    menu_biblioteca()