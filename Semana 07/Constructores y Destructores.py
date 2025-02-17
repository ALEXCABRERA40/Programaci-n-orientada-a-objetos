class Caja:
    def __init__(self, ancho, alto, profundidad):
        """Inicializa los atributos de la caja."""
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def volumen(self):
        """Calcula y devuelve el volumen de la caja."""
        return self.ancho * self.alto * self.profundidad

    def area_superficial(self):
        """Calcula y devuelve el área superficial de la caja."""
        return 2 * (self.ancho * self.alto + self.ancho * self.profundidad + self.alto * self.profundidad)

    def __del__(self):
        """Destructor de la caja."""
        print("La caja ha sido destruida.")


# Crear una instancia de la clase Caja
caja = Caja(5, 3, 2)

# Calcular el volumen y el área superficial de la caja
volumen = caja.volumen()
area_superficial = caja.area_superficial()

# Imprimir los resultados
print(f"Volumen de la caja: {volumen}")
print(f"Área superficial de la caja: {area_superficial}")

