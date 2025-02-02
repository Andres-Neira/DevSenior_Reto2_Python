class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Cliente(Persona):
    def __init__(self, nombre, edad, contacto, direccion):
        super().__init__(nombre, edad)
        self.contacto = contacto
        self.direccion= direccion
        clientes = []
class Veterinario(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        Veterinarios=[]

class Mascota:
    def __init__(self, nombre, especie, edad, raza, historial_citas,cliente):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.raza = raza
        self.historial_citas = historial_citas
        self.cliente = cliente



def menu():
    while True:
        print('SISTEMA DE GESTION ADMINISTRATIVA VETERINARIA DEVSENIOR\n'
                '---------------------------------------------------------\n'
                '1.Registrar cliente\n'
                '2.Registrar mascota\n'
                '3 Registrar Veterinario'
                '4.Registra Cita\n'
                '5 Modificar cita\n'
                '6 Cancelar cita\n'
                '7 Consultar historial\n'
                '8 Consultar citas\n'
                '9 Salir')
        opcion=input('Elija una opción (Ejemplo : 1) : ')
        if opcion == "1":
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            pass
        elif opcion == '7':
            pass
        elif opcion == '8':
            pass
        elif opcion == '9':
            print('Gracias por utilizar nuestro programa de gestión veterinaria')
            break
        else:
            print(' Opcion invalida Elija alguna de las opciones anteriores')
menu()
