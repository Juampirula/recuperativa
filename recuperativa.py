productos = []

def mostrar_menu():
    print("👻👻👻 MENÚ 👻👻👻")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir")
    print("4. Salir")

def grabar_producto():
    print("👻👻👻 GRABAR PRODUCTO 👻👻👻")
    numero_parte = input("Ingrese el número de parte: ")

    for producto in productos:
        if producto[0] == numero_parte:
            print("El número de parte ya existe. Intente nuevamente.")
            return

    nombre_producto = input("Ingrese el nombre del producto (mínimo 6 caracteres): ")
    if len(nombre_producto) < 6:
        print("El nombre del producto debe tener al menos 6 caracteres. Intente nuevamente.")
        return

    precio_producto = float(input("Ingrese el precio del producto (mayor a 0): "))
    if precio_producto <= 0:
        print("El precio del producto debe ser mayor a 0. Intente nuevamente.")
        return

    producto = (numero_parte, nombre_producto, precio_producto)
    productos.append(producto)
    print("Producto grabado exitosamente.")

def buscar_producto():
    print("👻👻👻 BUSCAR PRODUCTO 👻👻👻")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    print("Productos registrados:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. Número de parte: {producto[0]}")

    numero_seleccionado = int(input("Ingrese el número del producto a buscar: "))

    if 1 <= numero_seleccionado <= len(productos):
        producto_seleccionado = productos[numero_seleccionado - 1]

        if producto_seleccionado[2] >= 500:
            print("Información del producto:")
            print("Número de parte:", producto_seleccionado[0])
            print("Nombre:", producto_seleccionado[1])
            print("Precio:", producto_seleccionado[2])
        else:
            print("Producto sin stock.")
    else:
        print("Número de producto inválido.")

def imprimir_productos():
    print("👻👻👻 IMPRIMIR PRODUCTOS 👻👻👻")

    if len(productos) == 0:
        print("No hay productos para imprimir.")
        return

    print("Reporte de productos:")
    for i, producto in enumerate(productos, start=1):
        print(f"👻👻👻 Producto {i} 👻👻👻")
        print("Número de parte:", producto[0])
        print("Nombre:", producto[1])
        print("Precio:", producto[2])

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        grabar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        imprimir_productos()
    elif opcion == "4":
        print("¡Hasta luego!, amigo insano 👻👻👻")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
