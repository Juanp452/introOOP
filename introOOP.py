class Persona:
    # Método constructor (__init__) para inicializar los atributos de la persona
    def __init__(self, nombre, edad, genero, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    # Método 1: Saludar
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}.")

    # Método 2: Mostrar detalles
    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Ocupación: {self.ocupacion}")

    # Método 3: Cumplir años (aumentar la edad en 1)
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

    # Método 4: Cambiar ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ha cambiado su ocupación a {self.ocupacion}.")

    # Método 5: Despedirse
    def despedirse(self):
        print(f"Adiós, {self.nombre} se despide.")

        def saludarA(self):
            return f"Hola, {self.nombre}, te manda saludos a {nombreOtraPersona}."


# Crear una instancia de la clase Persona
persona1 = Persona("Carlos", 28, "Masculino", "Ingeniero")
persona2 = Persona("Juan", 19, "Masculino", "estudiante")
persona3 = Persona("Victor", 10, "Masculino", "Docente")
persona4 = Persona("Brenda", 21, "Femenino", "Secretaria")
# Llamar a los métodos de la instancia
persona1.saludar()
persona2.saludar()
persona3.saludar()
persona4.saludar()
persona1.mostrar_detalles()
persona1.cumplir_anios()
persona1.cambiar_ocupacion("Desarrollador de Software")
persona1.despedirse()
print(persona3.saludarA(persona4.nombre))

