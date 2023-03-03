"""
El código implementa el patrón de diseño Abstract Factory, que proporciona una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas. En este caso, las clases abstractas Caracterizacion y Personaje actúan como productos abstractos, mientras que las clases concretas que heredan de ellas actúan como productos concretos. La clase IFicha actúa como la fábrica abstracta que define los métodos para crear productos abstractos, mientras que la clase Ficha actúa como la fábrica concreta que implementa los métodos de creación de productos concretos.

En cuanto a los principios SOLID, el código cumple con varios de ellos:

- Principio de responsabilidad única: cada clase tiene una única responsabilidad y un único motivo para cambiar.
- Principio abierto-cerrado: las clases abstractas Caracterizacion y Personaje están abiertas a la extensión (es decir, se pueden agregar nuevas subclases), pero cerradas a la modificación.
- Principio de sustitución de Liskov: las subclases pueden ser utilizadas en lugar de sus clases base sin afectar el comportamiento del programa.
- Principio de inversión de dependencia: las clases dependen de abstracciones (clases abstractas e interfaces) en lugar de depender de clases concretas.

"""


from abc import ABC, abstractmethod

# Creamos la clase abstracta Caracterizacion, que servirá como base para todas las subclases
class Caracterizacion(ABC):

    def __init__(self, describ="ninguna"):
        self.describ = describ

    @abstractmethod
    def descripcion(self):
        pass

# Creamos las subclases de Caracterizacion
class Poder(Caracterizacion):
    def descripcion(self):
        return "Poderes:",self.describ

class Habilidad(Caracterizacion):
    def descripcion(self):
        return "habilidades excepcionales :",self.describ

class Debilidad(Caracterizacion):
    def descripcion(self):
        return "Debilidades:",self.describ

class Arma(Caracterizacion):
    def descripcion(self):
        return "Armas:",self.describ

class Personalidad(Caracterizacion):
    def descripcion(self):
        return "Personalidad:",self.describ

# Creamos la clase abstracta Personajes, que también servirá como base para todas las subclases
class Personaje(ABC):
    def __init__(self, nombre, liga="ninguna", enemigo="ninguno"):
        self.nombre = nombre
        self.liga = liga
        self.enemigo = enemigo
        self.caracteristicas = []

    def add_caracteristica(self, caracteristica):
        self.caracteristicas.append(caracteristica)

    def descripcion(self):
        return f"Soy {self.nombre}, un {self.__class__.__name__}"

    @abstractmethod
    def habilidad_especial(self):
        pass

# Creamos las subclases de Personajes
class Humano(Personaje):
    def __init__(self, nombre, edad, altura, peso, ocupacion, genero):
        super().__init__(nombre)
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.ocupacion = ocupacion
        self.genero = genero

    def habilidad_especial(self):
        return "Habilidad especial: Ninguna"

class SuperHumano(Personaje):
    def __init__(self, nombre, edad, altura, peso, superpoder, identidad_secreta):
        super().__init__(nombre)
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.superpoder = superpoder
        self.identidad_secreta = identidad_secreta

    def habilidad_especial(self):
        return "Habilidad especial: Superfuerza"

class Artificial(Personaje):
    def __init__(self, nombre, edad, altura, peso, nivel_inteligencia, capacidad_procesamiento):
        super().__init__(nombre)
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.nivel_inteligencia = nivel_inteligencia
        self.capacidad_procesamiento = capacidad_procesamiento

    def habilidad_especial(self):
        return "Habilidad especial: Inteligencia artificial avanzada"

class Alien(Personaje):
    def __init__(self, nombre, edad, altura, peso, planeta_origen, habilidad_especial):
        super().__init__(nombre)
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.planeta_origen = planeta_origen
        self.habilidad_especial = habilidad_especial

    def habilidad_especial(self):
        return f"Habilidad especial: {self.habilidad_especial}"


# Creamos la clase IFicha, que será la interfaz que usaremos para crear personajes
class IFicha(ABC):
    @abstractmethod
    def add(self, caracterizacion):
        pass

    @abstractmethod
    def liga(self, nombre_liga):
        pass

    @abstractmethod
    def enemigo(self, nombre_enemigo):
        pass

# Creamos la clase Ficha, que implementa la interfaz IFicha y nos permite crear personajes
class Ficha(IFicha):
    def __init__(self, personaje):
        self.personaje = personaje

    def add(self, caracterizacion):
        self.personaje.add_caracteristica(caracterizacion)

    def liga(self, nombre_liga):
        self.personaje.liga = nombre_liga

    def enemigo(self, nombre_enemigo):
        self.personaje.enemigo = nombre_enemigo

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos un personaje usando la Ficha y la clase Aliens
    alien_ficha = Ficha(Alien(nombre="E.T.", edad=99, altura=1.2, peso=30, planeta_origen="Xenón", habilidad_especial="Teletransportación"))
    alien_ficha.add(Poder("telequinesis"))
    alien_ficha.add(Personalidad("enojon"))
    alien_ficha.liga("Alianza Intergaláctica")
    alien_ficha.enemigo("Fuerzas de la Oscuridad")
    alien = alien_ficha.personaje

    # Imprimimos la descripción del personaje
    print(alien.nombre)
    print(alien.__class__.__name__)
    cart = [c.descripcion() for c in alien.caracteristicas]
    for des in cart:
        print(des)
    print(alien.__class__.habilidad_especial(alien))
    print(alien.liga)
    print(alien.enemigo)

     # Creamos un personaje usando la Ficha y la clase humano
    human_ficha = Ficha(Humano(nombre="Carlos", edad=30, altura=1.8, peso=70, ocupacion="Programador", genero="Masculino"))
    human_ficha.add(Poder("inteligencia"))
    human_ficha.add(Personalidad("timido"))
    human_ficha.liga("Avengers ")
    human_ficha.enemigo("raser")
    human = human_ficha.personaje

    print()
    print(human.nombre)
    print(human.__class__.__name__)
    cart = [c.descripcion() for c in human.caracteristicas]
    for des in cart:
        print(des)
    print(human.__class__.habilidad_especial(human))
    print(human.liga)
    print(human.enemigo)