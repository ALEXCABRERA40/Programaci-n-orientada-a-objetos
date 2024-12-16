def ingresar_temperaturas():
    """Función para ingresar las temperaturas diarias."""
    temperaturas = []
    for dia in range(7):
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio de las temperaturas."""
    if len(temperaturas) == 0:
        return 0
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

def mostrar_resultados(promedio):
    """Función para mostrar el resultado del promedio."""
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} °C")

def main():
    """Función principal que organiza el flujo del programa."""
    print("Bienvenido al programa de registro de temperaturas.")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultados(promedio)

# Ejecutar el programa
if __name__ == "__main__":
    main()