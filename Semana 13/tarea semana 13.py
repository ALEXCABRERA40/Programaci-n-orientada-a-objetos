#Tipos de Muestreo Estadístico
import tkinter as tk
from tkinter import ttk

class AplicacionGUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Datos")

        # Componentes GUI
        self.etiqueta_entrada = tk.Label(ventana, text="Ingrese Datos:")
        self.etiqueta_entrada.pack(pady=10)

        self.campo_entrada = tk.Entry(ventana, width=40)
        self.campo_entrada.pack(pady=5)

        self.boton_agregar = tk.Button(ventana, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack(pady=5)

        self.boton_limpiar = tk.Button(ventana, text="Limpiar", command=self.limpiar_datos)
        self.boton_limpiar.pack(pady=5)

        self.tabla_datos = ttk.Treeview(ventana, columns=("Datos",), show="headings")
        self.tabla_datos.heading("Datos", text="Datos Ingresados")
        self.tabla_datos.pack(pady=10)

        self.datos = []  # Lista para almacenar los datos

    def agregar_dato(self):
        dato = self.campo_entrada.get()
        if dato:
            self.datos.append(dato)
            self.tabla_datos.insert("", tk.END, values=(dato,))
            self.campo_entrada.delete(0, tk.END)  # Limpiar el campo de entrada

    def limpiar_datos(self):
        self.campo_entrada.delete(0, tk.END)  # Limpiar el campo de entrada
        for item in self.tabla_datos.get_children(): # Limpiar la tabla
            self.tabla_datos.delete(item)
        self.datos.clear() #Limpiar la lista de datos

# Crear la ventana principal
ventana_principal = tk.Tk()
app = AplicacionGUI(ventana_principal)

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()