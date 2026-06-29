import json

ARCHIVO = "productos.json"

def cargar_productos():
    with open(ARCHIVO, "r") as archivo:
        return json.load(archivo)
    
def guardar_productos(productos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)

    print("Cambios guardados correctamente")

def listar_productos(productos):
    if len(productos) == 0:
        print("No hay productos cargados")
    else:
        for producto in productos:
            print(f"Id: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
            print("=====================================")

def agregar_productos(productos):
    nuevo_id = int(input("Ingrese el id del nuevo producto que desea ingresar: "))
    for producto in productos:
        if producto["id"] == nuevo_id:
            print("Id de producto ya existente")
            return
    nombre = input("Ingrese el nombre del producto que desea agregar: ")
    while nombre == "":
        nombre = input("Error, reingrese el nombre del producto que desea agregar: ")

    categoria = input("Ingrese la categoria del producto: ")
    while categoria == "":
        categoria = input("Error, reingrese la categoria del producto: ")
    
    precio = float(input("Ingrese el precio del producto: "))
    while precio <= 0:
        precio = float(input("Error, reingrese el precio del producto: "))

    stock = int(input("Ingrese el stock del producto: "))
    while stock < 0:
        stock = int(input("Error, reingrese el stock del producto: "))

    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }

    productos.append(nuevo_producto)
    print("Producto agregado correctamente")

def buscar_producto_nombre(productos):
    nombre_buscado = input("Ingrese el nombre del prodcuto que desea buscar: ")
    encontrado = False

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            encontrado = True
            print(f"Nombre: {producto['nombre']}")
            print(f"Id: {producto['id']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
            print("=====================================")
    
    if encontrado == False:
        print("Nombre del producto no encontrado")

def modificar_stock(productos):
    id_buscado = int(input("Ingrese el id del producto que desea modificar el stock: "))
    
    for producto in productos:
        if producto["id"] == id_buscado:
            nuevo_stock = int(input("Ingrese la cantidad de stock que quiere modificar: "))
            while nuevo_stock < 0:
              nuevo_stock = int(input("Error, reingrese la cantidad de stock que quiere modificar: "))  
            producto["stock"] = nuevo_stock
            print("Cantidad de stock modificado correctamente")
            return
    print("No se encontro el producto")

def eliminar_producto(productos):
    id_buscado = int(input("Ingrese el ID del producto que desea eliminar: "))
    while id_buscado < 0:
        id_buscado = int(input("Error, reingrese el ID del producto que desea eliminar: "))

    for producto in productos:
        if producto["id"] == id_buscado:
            productos.remove(producto)
            print("Producto eliminado correctamente")
            return
    print("No se encontro el producto")

def mostrar_producto_categoria(productos):
    categoria_buscada = input("Ingrese la categoria que desea buscar: ")
    encontrado = False

    while categoria_buscada == "":
        categoria_buscada = input("Error, reingrese la categoria que desea buscar: ")

    for producto in productos:
        if producto["categoria"] == categoria_buscada:
            encontrado = True
            print("Categoria encontrada")
            print(f"La categoria es: {producto['categoria']}")
            print(f"Id: {producto['id']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print(f"Stock: {producto['stock']}")
            print("=====================================")

    if encontrado == False:
        print("No hay productos en esa Categoria")


def mostrar_estadisticas(productos):
    if len(productos) == 0:
        print("No hay productos cargados")
        return
    
    cantidad_productos = len(productos)

    total = 0
    for producto in productos:
        total += producto["stock"]

    min_precio = productos[0]["precio"]
    pos_anterior = 0

    for i in range(len(productos)):
        if productos[i]["precio"] < min_precio:
            min_precio = productos[i]["precio"]
            pos_anterior = i
    
    max_precio = productos[0]["precio"]
    pos_nuevo = 0

    for i in range(len(productos)):
        if productos[i]["precio"] > max_precio:
            max_precio = productos[i]["precio"]
            pos_nuevo = i

    categorias = {}

    for i in range(len(productos)):
        categoria = productos[i]["categoria"]

        if categoria in categorias:
            categorias[categoria] += 1
        else:
            categorias[categoria] = 1

    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Total stock: {total}")
    print(f"Producto con menor precio: {productos[pos_anterior]['nombre']} ({productos[pos_anterior]['precio']})")
    print(f"Producto con mayor precio: {productos[pos_nuevo]['nombre']} ({productos[pos_nuevo]['precio']})")

    print("Productos por categoria: ")
    for clave in categorias:
        print(f"{clave}: {categorias[clave]}")

def exportar_reporte_csv(productos, nombre_archivo):
    archivo = open(nombre_archivo, "w", encoding="utf-8")

    archivo.write("nombre,categoria,precio,stock\n")

    for producto in productos:
        linea = f"{producto['id']},{producto['nombre']},{producto['categoria']},{producto['precio']},{producto['stock']}"
        archivo.write(linea)
    archivo.close()
    print("Archivo exportado correctamente")


def mostrar_menu():
    print("\n=======Sistema de gestion de Supermercado=======")
    print("1. Listar Productos")
    print("2. Agregar Producto")
    print("3. Buscar producto por nombre")
    print("4. Modificar stock")
    print("5. Eliminar producto")
    print("6. Mostrar productos por categoria")
    print("7. Mostrar Estadisticas")
    print("8. Exportar reporte CSV")
    print("9. Guardar y salir")

def main():
    productos = cargar_productos()

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))

        while opcion < 1 or opcion > 9:
            opcion = int(input("Error, reingrese una opcion valida: "))

        match opcion:
            case 1:
                listar_productos(productos)
            case 2:
                agregar_productos(productos)
            case 3:
                buscar_producto_nombre(productos)
            case 4:
                modificar_stock(productos)
            case 5:
                eliminar_producto(productos)
            case 6:
                mostrar_producto_categoria(productos)
            case 7:
                mostrar_estadisticas(productos)
            case 8:
                exportar_reporte_csv(productos, "reporte.csv")
            case 9:
                guardar_productos(productos)
                break

main()