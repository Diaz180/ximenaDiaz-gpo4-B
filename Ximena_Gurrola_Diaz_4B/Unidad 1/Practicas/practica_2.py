# PRACTICA 2. ATRIBUTOS PUBLICOS Y PRIVADOS

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.__cuenta = None  # atributo privado

    def estudiar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Esta persona cumplió: {self.edad} años")

    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta bancaria (nº {cuenta.num_cuenta})")

    def consultar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de {self.nombre} es de ${self.__cuenta.mostrar_saldo()}")
        else:
            print(f"{self.nombre} aún no es cliente bancario")


class CuentaBancaria:
    def __init__(self, num_cuenta, saldo):  
        self.num_cuenta = num_cuenta
        self.__saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se depositó ${cantidad}. Nuevo saldo: ${self.__saldo}")
        else:
            print("Ingresa una cantidad válida mayor a $0")

    def retiro(self, cantidad):
        if cantidad <= 0:
            print("Ingresa una cantidad válida mayor a $0")
        elif cantidad > self.__saldo:
            print(f"La cantidad que desea retirar es mayor a la disponible. Saldo disponible: ${self.__saldo}")
        else:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad}. Nuevo saldo: ${self.__saldo}")


# Ejemplo de uso
persona1 = Persona("Ximena", 19)
cuenta1 = CuentaBancaria("818", 700)

persona1.asignar_cuenta(cuenta1)
persona1.consultar_saldo()   

cuenta1.depositar(7000)     
persona1.consultar_saldo()  

cuenta1.retiro(300)         
cuenta1.retiro(5000)

        
        
        
        