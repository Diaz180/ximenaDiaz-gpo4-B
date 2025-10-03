
# Caso: Sistema de pedidos en una cafetería

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[{self.nombre}] Notificación: {mensaje}")


class Cafeteria:
    def __init__(self):
        self.observadores = []

    def agregar_cliente(self, cliente):
        self.observadores.append(cliente)

    def notificar(self, mensaje):
        for cliente in self.observadores:
            cliente.actualizar(mensaje)


class Bebida:
    def preparar(self):
        pass


class Cafe(Bebida):
    def preparar(self):
        return "Preparando un café americano"


class Te(Bebida):
    def preparar(self):
        return "Preparando un té verde"


class Chocolate(Bebida):
    def preparar(self):
        return "Preparando un chocolate caliente "


# Caso: Sistema de pedidos en una cafetería

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[{self.nombre}] Notificación: {mensaje}")


class Cafeteria:
    def __init__(self):
        self.observadores = []

    def agregar_cliente(self, cliente):
        self.observadores.append(cliente)

    def notificar(self, mensaje):
        for cliente in self.observadores:
            cliente.actualizar(mensaje)


class Bebida:
    def preparar(self):
        pass


class Cafe(Bebida):
    def preparar(self):
        return "Preparando un café americano"


class Te(Bebida):
    def preparar(self):
        return "Preparando un té verde"


class Chocolate(Bebida):
    def preparar(self):
        return "Preparando un chocolate caliente "


class BebidaFactory:
    def crear_bebida(tipo):
        if tipo == "cafe":
            return Cafe()
        elif tipo == "te":
            return Te()
        elif tipo == "chocolate":
            return Chocolate()
        else:
            raise ValueError("Bebida no disponible")


cafeteria = Cafeteria()

# Clientes que quieren recibir notificaciones
cliente1 = Cliente("Ana")
cliente2 = Cliente("Luis")
cafeteria.agregar_cliente(cliente1)
cafeteria.agregar_cliente(cliente2)

# Pedido usando Factory
pedido = BebidaFactory.crear_bebida("chocolate")
mensaje = pedido.preparar()

# Se prepara y se avisa a todos
print(mensaje)
cafeteria.notificar("Tu bebida está lista ")


cafeteria = Cafeteria()

# Clientes que quieren recibir notificaciones
cliente1 = Cliente("Ana")
cliente2 = Cliente("Luis")
cafeteria.agregar_cliente(cliente1)
cafeteria.agregar_cliente(cliente2)

# Pedido usando Factory
pedido = BebidaFactory.crear_bebida("chocolate")
mensaje = pedido.preparar()

# Se prepara y se avisa a todos
print(mensaje)
cafeteria.notificar("Tu bebida está lista ")