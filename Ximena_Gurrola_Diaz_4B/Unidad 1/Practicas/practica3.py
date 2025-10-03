# Práctica 3: Introducción de Polimorfismo

class PagoTarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} con tarjeta"

class Transferencia: 
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} por medio de transferencia"

class Paypal:
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} por medio de PayPal"

class Deposito:
    def procesar_pago(self, cantidad):
        return f"Procesado pago de ${cantidad} por medio de depósito en ventanilla"


#actividad 
#PRECESAR PAGO CO DIFERENTES CANTIDADES EN CADA UNO DE LAS FORMAS DE PAGO EJEMPLO: 100 CON TARJETA ,  
# #500 CON TRANSFERENCIA, 20000 CON PAYPAL, 400 CON DEPOSITO 
# Instancias con diferentes métodos de pago
metodos_pago = [
    PagoTarjeta(),
    Transferencia(),
    Paypal(),
    Deposito()
]

# Ejemplo de cantidades diferentes
cantidades = [100, 500, 20000, 400]

# Polimorfismo en acción
for metodo, cantidad in zip(metodos_pago, cantidades):
    print(metodo.procesar_pago(cantidad))

