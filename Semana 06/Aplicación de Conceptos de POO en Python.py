#Conceptos de POO
class Animal:
    """Clase base que representa a un animal"""

    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulación: atributo privado

    def hacer_sonido(self):
        print("El animal hace un sonido")

    def get_nombre(self):
        return self.__nombre

class Perro(Animal):
    """Clase derivada que representa a un perro"""

    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    """Clase derivada que representa a un gato"""

    def hacer_sonido(self):
        print("Miau!")

# Creación de objetos
mi_perro = Perro("Lucas")
mi_gato = Gato("Luna")

# Demostrando polimorfismo
def hacer_sonar_animal(animal):
    animal.hacer_sonido()

# Llamadas a los métodos
hacer_sonar_animal(mi_perro)  # Imprime: Guau!
hacer_sonar_animal(mi_gato)  # Imprime: Miau!