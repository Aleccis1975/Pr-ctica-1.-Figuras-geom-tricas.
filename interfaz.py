import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importar PIL para cargar imágenes
from figuras import Rectangulo, Circulo, Cuadrado, Triangulo  # Importar las clases de figuras

# Función para validar la entrada numérica y asegurarse de que no sea cero
def validar_entrada(valor):
    try:
        valor = float(valor)
        if valor <= 0:
            messagebox.showerror("Error", "Las medidas deben ser mayores que cero.")
            return None
        return valor
    except ValueError:
        messagebox.showerror("Error", "Introducir solo valores numéricos.")
        return None

# Función para mostrar los campos y la imagen correspondiente a la figura seleccionada
def mostrar_campos_figura(*args):
    figura = seleccion_figura.get()

    # Ocultar todos los campos primero
    frame_rectangulo.pack_forget()
    frame_circulo.pack_forget()
    frame_cuadrado.pack_forget()
    frame_triangulo.pack_forget()

    # Mostrar la imagen correspondiente a la figura
    if figura == "Rectángulo":
        frame_rectangulo.pack(pady=10)
        mostrar_imagen("rectangulo.png")
    elif figura == "Círculo":
        frame_circulo.pack(pady=10)
        mostrar_imagen("circulo.png")
    elif figura == "Cuadrado":
        frame_cuadrado.pack(pady=10)
        mostrar_imagen("cuadrado.png")
    elif figura == "Triángulo":
        frame_triangulo.pack(pady=10)
        mostrar_imagen("triangulo.png")

# Función para mostrar una imagen en la interfaz
def mostrar_imagen(ruta_imagen):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen)
    
    # Redimensionar la imagen usando LANCZOS (el nuevo nombre de ANTIALIAS)
    imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)
    
    # Convertir la imagen a un formato compatible con Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    # Mostrar la imagen en el label
    label_imagen.config(image=imagen_tk)
    label_imagen.image = imagen_tk  # Guardar una referencia a la imagen

# Función para calcular y mostrar el área y perímetro
def calcular():
    figura = seleccion_figura.get()

    if figura == "Rectángulo":
        ancho = validar_entrada(entry_ancho.get())
        alto = validar_entrada(entry_alto.get())
        if ancho is not None and alto is not None:
            if ancho == alto:
                messagebox.showinfo("Información", "Este es un cuadrado, no un rectángulo. Usa la opción Cuadrado.")
            else:
                rectangulo = Rectangulo(ancho, alto)
                area = rectangulo.calcular_area()
                perimetro = rectangulo.calcular_perimetro()
                messagebox.showinfo("Resultados", f"Área: {area}\nPerímetro: {perimetro}")

    elif figura == "Círculo":
        radio = validar_entrada(entry_radio.get())
        if radio is not None:
            circulo = Circulo(radio)
            area = circulo.calcular_area()
            perimetro = circulo.calcular_perimetro()
            messagebox.showinfo("Resultados", f"Área: {area}\nPerímetro: {perimetro}")

    elif figura == "Cuadrado":
        lado = validar_entrada(entry_lado.get())
        if lado is not None:
            cuadrado = Cuadrado(lado)
            area = cuadrado.calcular_area()
            perimetro = cuadrado.calcular_perimetro()
            messagebox.showinfo("Resultados", f"Área: {area}\nPerímetro: {perimetro}")

    elif figura == "Triángulo":
        lado1 = validar_entrada(entry_lado1.get())
        lado2 = validar_entrada(entry_lado2.get())
        lado3 = validar_entrada(entry_lado3.get())
        if lado1 is not None and lado2 is not None and lado3 is not None:
            if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
                triangulo = Triangulo(lado1, lado2, lado3)
                area = triangulo.calcular_area()
                perimetro = triangulo.calcular_perimetro()
                tipo = triangulo.tipo_triangulo()
                messagebox.showinfo("Resultados", f"Área: {area}\nPerímetro: {perimetro}\nTipo: {tipo}")
            else:
                messagebox.showerror("Error", "Las medidas no corresponden a un triángulo válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Figuras Geométricas")
ventana.geometry("1280x1080")

# Etiqueta para seleccionar la figura
label_figura = tk.Label(ventana, text="Seleccione una figura:")
label_figura.pack(pady=10)

# Variable para almacenar la selección de la figura
seleccion_figura = tk.StringVar()
seleccion_figura.set("Rectángulo")

# Menú desplegable para seleccionar la figura geométrica
figuras = ["Rectángulo", "Círculo", "Cuadrado", "Triángulo"]
menu_figuras = tk.OptionMenu(ventana, seleccion_figura, *figuras)
menu_figuras.pack(pady=10)

# Label para mostrar la imagen
label_imagen = tk.Label(ventana)
label_imagen.pack()

# Crear frames para cada conjunto de entradas
frame_rectangulo = tk.Frame(ventana)
label_ancho = tk.Label(frame_rectangulo, text="Ancho:")
label_ancho.pack()
entry_ancho = tk.Entry(frame_rectangulo)
entry_ancho.pack()
label_alto = tk.Label(frame_rectangulo, text="Alto:")
label_alto.pack()
entry_alto = tk.Entry(frame_rectangulo)
entry_alto.pack()

frame_circulo = tk.Frame(ventana)
label_radio = tk.Label(frame_circulo, text="Radio:")
label_radio.pack()
entry_radio = tk.Entry(frame_circulo)
entry_radio.pack()

frame_cuadrado = tk.Frame(ventana)
label_lado = tk.Label(frame_cuadrado, text="Lado:")
label_lado.pack()
entry_lado = tk.Entry(frame_cuadrado)
entry_lado.pack()

frame_triangulo = tk.Frame(ventana)
label_lado1 = tk.Label(frame_triangulo, text="Lado 1:")
label_lado1.pack()
entry_lado1 = tk.Entry(frame_triangulo)
entry_lado1.pack()
label_lado2 = tk.Label(frame_triangulo, text="Lado 2:")
label_lado2.pack()
entry_lado2 = tk.Entry(frame_triangulo)
entry_lado2.pack()
label_lado3 = tk.Label(frame_triangulo, text="Lado 3:")
label_lado3.pack()
entry_lado3 = tk.Entry(frame_triangulo)
entry_lado3.pack()

# Botón para calcular y mostrar los resultados
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.pack(pady=20)

# Asociar la función mostrar_campos_figura a los cambios en la selección del menú
seleccion_figura.trace("w", mostrar_campos_figura)

# Mostrar inicialmente los campos del rectángulo
mostrar_campos_figura()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
