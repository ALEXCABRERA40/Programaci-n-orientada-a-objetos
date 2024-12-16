class ClimaDiario:
    """Clase que representa la información diaria del clima."""

    def __init__(self):
        """Inicializa una lista para almacenar las temperaturas diarias."""
        self.__temperaturas = []  # Encapsulamiento: atributo privado

    def ingresar_temperatura(self, temperatura):
        """Método para agregar una temperatura a la lista."""
        if isinstance(temperatura, (int, float)):
            self.__temperaturas.append(temperatura)
        else:
            raise ValueError("La temperatura debe ser un número.")

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas."""
        if not self.__temperaturas:
            return 0
        suma = sum(self.__temperaturas)
        promedio = suma / len(self.__temperaturas)
        return promedio

    def mostrar_temperaturas(self):
        """Método para mostrar las temperaturas ingresadas."""
        return self.__temperaturas

    def __str__(self):
        """Devuelve una representación en cadena de las temperaturas ingresadas."""
        return f'Temperaturas: {self.__temperaturas}'

class Clima:
    def __init__(self, temperatura=0, humedad=0, lluvia=0, fecha=""):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__lluvia = lluvia
        self.__fecha = fecha

    def ingresar_datos(self, temperatura, humedad, lluvia, fecha):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__lluvia = lluvia
        self.__fecha = fecha

    def calcular_promedio_semanal(self, climas):
        total_temperatura = 0
        total_humedad = 0
        total_lluvia = 0
        for clima in climas:
            total_temperatura += clima.__temperatura
            total_humedad += clima.__humedad
            total_lluvia += clima.__lluvia
        promedio_temperatura = total_temperatura / len(climas)
        promedio_humedad = total_humedad / len(climas)
        promedio_lluvia = total_lluvia / len(climas)
        return promedio_temperatura, promedio_humedad, promedio_lluvia

    def imprimir_informacion(self):
        print(f"Fecha: {self.__fecha}")
        print(f"Temperatura: {self.__temperatura}°C")
        print(f"Humedad: {self.__humedad}%")
        print(f"Lluvia: {self.__lluvia} mm")

# Ejemplo de uso
clima1 = Clima(25, 60, 10, "Lunes")
clima2 = Clima(26, 65, 12, "Martes")
clima3 = Clima(27, 70, 15, "Miércoles")
clima4 = Clima(28, 75, 18, "Jueves")
clima5 = Clima(29, 80, 20, "Viernes")
clima6 = Clima(30, 85, 22, "Sábado")
clima7 = Clima(31, 90, 25, "Domingo")

climas = [clima1, clima2, clima3, clima4, clima5, clima6, clima7]

promedio_temperatura, promedio_humedad, promedio_lluvia = Clima().calcular_promedio_semanal(climas)

print(f"Promedio semanal de temperatura: {promedio_temperatura}°C")
print(f"Promedio semanal de humedad: {promedio_humedad}%")
print(f"Promedio semanal de lluvia: {promedio_lluvia} mm")

for clima in climas:
    clima.imprimir_informacion()
    print("--------------------")
