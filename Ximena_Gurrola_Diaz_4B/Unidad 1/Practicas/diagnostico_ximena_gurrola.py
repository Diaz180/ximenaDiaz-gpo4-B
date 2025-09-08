# Archivo: Diagnostico_nombre.py
# Simulador de pedidos en una frutería

# Elegir una temática de tienda y escribir 3 productos
productos = ["Fresas", "Mangos", "Cerezas"]
precios = [30, 40, 50]

# Función para calcular el total
def calcular_total(cantidad, precios):
    total = 0
    for i in range(len(cantidad)):
        total += cantidad[i] * precios[i] 
    return total

# Menú para usuario (Outputs)
print("Menú de frutería ¡Bienvenido!")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}, estos son los productos disponibles:")

for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    
cantidad = []

# Pedir cantidades al usuario
for i in range(len(productos)):
    cant = int(input(f"¿Cuántos {productos[i]} desea?: "))
    cantidad.append(cant)

# Calcular total
total = calcular_total(cantidad, precios)


print("Recibo de pago: ")
for i in range(len(productos)):
    if cantidad[i] > 0:
        print(f"{cantidad[i]} {productos[i]} (${precios[i]}")

print(f"Total a pagar: ${total}")
