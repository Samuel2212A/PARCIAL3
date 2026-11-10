productos = {
    1: (" Cafe " , 3000 , 20) ,
    2: (" Jugo natural " , 5000 , 15) ,
    3: (" Sandwich " , 8000 , 10) ,
    4: (" Empanada " , 2500 , 25) ,
    5: (" Hamburguesa " , 12000 , 8)
}
pedido = []
def mostrar_productos(productos):
    print("Productos disponibles: ")
    for codigo, (nombre, precio, cantidad) in productos.items():
        print(f"{codigo}. {nombre} - Precio: {precio} - Cantidad disponible: {cantidad}")

def registrar_producto(productos, pedido, codigo, cantidad):
    if codigo in productos:
        nombre, precio, stock = productos[codigo]
        if stock >= cantidad:
            productos[codigo] = (nombre, precio, stock - cantidad)
            pedido.append((nombre, precio, cantidad))
        else:
            print("No hay suficiente stock para registrar el producto.")
    else:
        print("El código del producto no es válido.")

def agregar_producto(productos, pedido):
    mostrar_productos(productos)
    codigo = int(input("Ingrese el código del producto que desea agregar al pedido: "))
    cantidad = int(input("Ingrese la cantidad que desea agregar: "))
    registrar_producto(productos, pedido, codigo, cantidad)

while True:
        print("\n==========")
        print("CAFETERIA")
        print("==========")
        print("1. Mostrar productos")
        print("2. Agregar producto al pedido")
        print("3. Finalizar pedido")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
             mostrar_productos(productos)
        elif opcion == "2":
             agregar_producto(productos, pedido)
        elif opcion == "3":
             print("Pedido finalizado. Detalles del pedido:")
             break
        elif opcion != "1" and opcion != "2" and opcion != "3":
             print("Opción inválida. Por favor, seleccione una opción válida.")

mostrar_productos(productos)
registrar_producto(productos, pedido, 1, 5)
agregar_producto(productos, pedido)
