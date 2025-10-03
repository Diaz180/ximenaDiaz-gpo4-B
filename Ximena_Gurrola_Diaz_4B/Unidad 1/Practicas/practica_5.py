# practica 5 patrones de diseño

class Logger:
    # creamos un atributo de clase donde se guardará la instancia
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Creamos una única instancia de Logger
            cls._instance = super().__new__(cls)
            # Abrimos el archivo solo una vez
            cls._instance.archivo = open("app.log", "a")
        return cls._instance

    def log(self, mensaje):
        self.archivo.write(mensaje)
        self.archivo.flush()  # para que se guarde inmediatamente en el archivo


logger1 = Logger()
logger2 = Logger()

logger1.log("inicio de sesión en la aplicación\n")
logger2.log("El usuario se autenticó correctamente\n")
print(logger1 is logger2)  # True, ambas variables apuntan a la misma instancia


class Presidente:
    _instance = None

    def __new__(cls, nombre):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nombre = nombre
            cls._instance.historial = []
        return cls._instance

    def accion(self, evento):
        evento = f"{self.nombre} {evento}"
        self.historial.append(evento)
        print(evento)


p1 = Presidente("AMLO")
p2 = Presidente("EPN")
p3 = Presidente("Fox")

p1.accion("ganó las elecciones")
p2.accion("firmó un acuerdo")
p3.accion("declaró la guerra")

print("Historial del presidente:")
print(p1.historial)

print(p1 is p2 is p3)  # True, todas las variables apuntan a la misma instancia

# Cerramos el archivo de log para liberar el recurso
logger1.archivo.close()


#1 Que pasaria si eliminamos la verificacion if cls._instance is None: en el metodo new

#2 Que significa el true en p1 is p2 is p3 en el contexto del patron singleton

#3 Es buena idea usar el metodo singelton para todo lo que sea global? menciona ejemplos donde sea recomendable y donde no










