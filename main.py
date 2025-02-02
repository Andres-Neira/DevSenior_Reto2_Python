class Cliente:
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

class Mascota:
    def __init__(self, nombre, especie, edad, raza, historial_citas):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.raza = raza
        self.historial_citas = historial_citas

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
