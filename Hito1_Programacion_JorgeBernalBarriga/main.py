import re
from tabulate import tabulate
from colorama import init, Fore, Style

init(autoreset=True)
class Cliente:
    def __init__(self, nombreCompleto, nombreUsuario, correoElectronico, telefono, contraseña, confirmarContraseña,
                 direccionFacturacion):
        self.nombreCompleto = nombreCompleto
        self.nombreUsuario = nombreUsuario
        self.correoElectronico = correoElectronico
        self.telefono = telefono
        self.contraseña = contraseña
        self.confirmarContraseña = confirmarContraseña
        self.direccionFacturacion = direccionFacturacion
        self.total_compra = 0

    def validar_informacion(self):
        if (
                not self.nombreCompleto
                or not self.nombreUsuario
                or not self.correoElectronico
                or not self.contraseña
                or not self.confirmarContraseña

        ):
            return False
        return True

    def registro_cliente(self):
        print(Fore.GREEN + Style.BRIGHT + "\n ---------TIENDA DE ROPA---------")
        print(Fore.GREEN + "\n Bienvenido a nuestra tienda online a continuación le mostraremos nuestra página")
        print("\nPor favor regístrese para continuar y que le podamos mostrar los productos que tenemos disponibles")

        while True:
            self.nombreCompleto = input("Por favor, ingrese su nombre y apellidos: ")
            if self.nombreCompleto:
                break
            else:
                print("Error: El campo de nombre y apellidos no puede estar vacío.")
        while True:
            self.nombreUsuario = input("Por favor, ingrese el nombre de usuario que querrá utilizar: ")
            if self.nombreUsuario:
                break
            else:
                print("Error: El campo de nombre de usuario no puede estar vacío.")


        while True:
            self.correoElectronico = input("Por favor, ingrese su correo electrónico: ")
            if not self.correoElectronico:
                print("Error: El campo de correo electrónico no puede estar vacío.")
                continue

            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correoElectronico):
                print("Error: El formato del correo electrónico no es válido.")
                continue

            break

        while True:
            self.contraseña = input("Por favor, ingrese una contraseña: ")
            self.confirmarContraseña = input("Por favor, confirme su contraseña: ")

            if self.contraseña ==self.confirmarContraseña:
                break
            else:
                print('La confirmación de contraseña no es correcta, por favor rellene correctame estos campos para poder continuar.')



        if not self.validar_informacion():
            print("\nError, por favor rellene todos los campos para poder continuar")
        else:
            print(f"\n Se ha registrado correctamente. Hola {self.nombreCompleto}, bienvenido/a  a nuestra tienda online")

    def seleccionar_productos(self):
        print("\nBienvenido a la sección de productos. Aquí están los productos disponibles:")

        productos_disponibles = {
            1: {"nombre": "Zapatillas deportivas ", "precio": 39.9,"stock": 15},
            2: {"nombre": "Zapatos de vestir ", "precio": 59.0,"stock": 17},
            3: {"nombre": "Camisa ", "precio": 22.0,"stock": 9},
            4: {"nombre": "Americana ", "precio": 59.0,"stock": 23},
            5: {"nombre": "Pantalon vaquero ", "precio": 39.0,"stock": 14},
            6: {"nombre": "Corbata", "precio": 15.0,"stock": 10},
            7: {"nombre": "Calcetines ", "precio": 9.0,"stock": 9},
            8: {"nombre": "Abrigo ", "precio": 95.0,"stock": 12},
            9: {"nombre": "Bufanda", "precio": 19.0,"stock": 14},
            10: {"nombre": "Gorro", "precio": 18.0,"stock": 12}
        } #Utilizamos un diccionario para mostrar los productos disponibles.

        tabla_productos = []
        for key, value in productos_disponibles.items():
            tabla_productos.append([
                f"{Fore.BLUE}{key}{Style.RESET_ALL}",
                f"{Fore.GREEN}{value['nombre']}{Style.RESET_ALL}",
                f"{Fore.YELLOW}{value['precio']}{Style.RESET_ALL}",
                f"{Fore.RED}{value['stock']}{Style.RESET_ALL}"
            ])

        # Definir encabezados para la tabla
        headers = [
            f"{Fore.CYAN}ID{Style.RESET_ALL}",
            f"{Fore.CYAN}Nombre{Style.RESET_ALL}",
            f"{Fore.CYAN}Precio{Style.RESET_ALL}",
            f"{Fore.CYAN}Stock{Style.RESET_ALL}"
        ]

        # Imprimir la tabla utilizando tabulate
        print(tabulate(tabla_productos, headers=headers, tablefmt="grid"))

        # Selección de productos por parte del cliente
        productos_seleccionados = [] #Guardamos los productos en una lista
        self.total_compra = 0 #Variable para almacenar la suma total de la compra

        while True:
            seleccion = input(
                "Por favor, seleccione un producto por su número y se guardarán en su cesta(o escriba 'fin' para terminar): ")
            if seleccion.lower() == 'fin':
                break
            elif seleccion.isdigit():
                id_producto = int(seleccion)
                if id_producto in productos_disponibles:
                    producto = productos_disponibles[id_producto]
                    if producto['stock'] > 0:  # Verificar si hay stock disponible
                        productos_seleccionados.append(producto)
                        producto['stock'] -= 1  # Restar uno al stock
                        self.total_compra += producto['precio']  # Actualizar la suma total
                        print(
                            f"Producto {producto['nombre']} agregado al carrito. Total hasta ahora: {self.total_compra}€")
                    else:
                        print("Producto agotado. Seleccione otro producto.")
                else:
                    print("Número de producto no válido. Intente de nuevo.")
            else:
                print("Entrada no válida. Intente de nuevo.")

        print("\nProductos seleccionados:")
        for producto in productos_seleccionados:
            print(f"{producto['nombre']} -  Precio {producto['precio']}€ - Stock actual  {producto['stock']}")

        print(f"\nEl total de su compra actual con IVA es: {self.total_compra}€")

    def aplicar_descuento(self, descuento):
        self.total_compra *= (1 - descuento)

    def proceso_pago(self):

        aplicar_descuento = input("\nVamos a realizar el proceso de pago. Si usted reside fuera de España pulse 1 y se le descotará el IVA, en caso contrario pulse 2: ")
        while aplicar_descuento not in ['1', '2']:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
            aplicar_descuento = input(
                "\nSi usted reside fuera de España pulse 1 y se le descotará el IVA, en caso contrario pulse 2: ")

        if aplicar_descuento == '1':
            descuento = 0.21
            self.aplicar_descuento(descuento)
            print(f"El total de su compra tras descontar el IVA es: {self.total_compra:.2f}€")
        elif aplicar_descuento == '2':
            print(f"El total de su compra con el IVA incluido es: {self.total_compra}€")

        print('\nPor último rellene los siguientes datos para terminar con el pago de su pedido y le enviaremos el codigo de seguimiento y su factura')

        while True:
            self.telefono = input("Por favor, ingrese un teléfono de contacto (9 dígitos) para que podamos enviarle su numero de seguimiento del pedido: ")
            if not self.telefono:
                print("Error: El campo de teléfono no puede estar vacío.")
                continue

            if not re.match(r"\d{9}$", self.telefono):
                print("Error: El número de teléfono debe contener exactamente 9 dígitos.")
                continue

            break


        while True:
            tarjeta_credito = input("Ingrese el número de tarjeta de crédito: ")
            if tarjeta_credito:
                break
            else:
                print("Error: El campo de número de tarjeta de crédito no puede estar vacío.")

        while True:
            fecha_vencimiento = input("Ingrese la fecha de caducidad de su tarjeta (MM/YY): ")
            if fecha_vencimiento:
                break
            else:
                print("Error: El campo de fecha de vencimiento no puede estar vacío.")

        while True:
            codigo_seguridad = input("Ingrese el código de seguridad: ")
            if codigo_seguridad:
                break
            else:
                print("Error: El campo de código de seguridad no puede estar vacío.")

        print("¡Pago realizado con éxito!")
        print('Hemos enviado a su correo electrónico su factura y recibirá en su teléfono y correo el codigo de seguimiento de su pedido.')

# Crear una instancia de la clase Cliente
cliente_nuevo = Cliente("", "", "", "", "", "", "")

# Llamar al método registro_cliente en la instancia creada
cliente_nuevo.registro_cliente()

# Llamar al método seleccionar_productos en la instancia creada
cliente_nuevo.seleccionar_productos()

# Llamar al método proceso_pago en la instancia creada
cliente_nuevo.proceso_pago()

