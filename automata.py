import re
import tkinter as tk
from tkinter import messagebox

def validar_cadena(cadena):
    # Patrón de expresión regular para el rango modificado
    patron = r'^((A[G-Z][A-Z])|(B[A-Z]+[A-Z])|(C[A-Y][A-Z]))-[0-9]{3}-[A-Z]$'
    
    if re.match(patron, cadena):
        return True
    else:
        return False
    
def validar_cadena_y_mostrar_resultado():
    cadena = cadena_entry.get()
    
    if cadena.lower() == 'salir':
        root.quit()
    elif validar_cadena(cadena):
        messagebox.showinfo("Resultado", "Cadena válida")
    else:
        messagebox.showerror("Resultado", "Cadena no válida")

root = tk.Tk()
root.title("Validación de Cadenas")

etiqueta = tk.Label(root, text="Ingrese una cadena:")
etiqueta.pack()

cadena_entry = tk.Entry(root)
cadena_entry.pack()

validar_button = tk.Button(root, text="Validar", command=validar_cadena_y_mostrar_resultado)
validar_button.pack()

root.mainloop()
