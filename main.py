import tkinter as tk

# Crear una nueva ventana
root = tk.Tk()

# Agregar un label con el mensaje "Hola"
label = tk.Label(root, text="¡Hola!")
label.pack()

# Iniciar el bucle de eventos de la ventana
root.mainloop()
