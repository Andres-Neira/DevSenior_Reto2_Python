from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre, edad, contacto, direccion,):
        self.nombre = nombre
        self.edad = edad
        self.contacto=contacto
        self.direccion=direccion

    @abstractmethod
    def mostrardatos(self):
        pass

class Cliente(Persona):
    def __init__(self, nombre, edad,contacto,direccion):
        super().__init__(nombre, edad,contacto,direccion)
        self.mascota=[]

    def agregarMascota(self,mascota):
        self.mascota.append(mascota)

    def mostrardatos(self):
        return f'El cliente se registro con exito !'


class Veterinario(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        veterinarios = []
class Mascota:
    def __init__(self, nombre, especie, edad, raza, historial_citas):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.raza = raza
        self.historial_citas =[]


class Cita:
    def __init__(self, fecha , hora, servicio,veterinario,cliente,mascota ):
        self.name = fecha
        self.hora = hora
        self.servicio= servicio
        self.veterinario = veterinario
        self.cliente = cliente
        self.mascota = mascota

class sistema:
    def __init__(self):
        self.clientes=[]
    def agregarCliente(self):
        try:
            nombre=input('Digite el nombre del cliente').strip()
            edad=input('Digite el nombre del cliente').strip()
            contacto=input('Digite el numero de contacto del cliente').strip()
            direccion=input('Digite la dirección de domicilio del cliente').strip()
            if not nombre or not edad or not contacto or not direccion:
                raise ValueError('Todos los datos se debe de registrar')

            cliente=Cliente(nombre,edad,contacto,direccion)
            self.clientes.append(cliente)
            return f'Cliente registrado con exito'
        except ValueError as e:
            print(f'error : {e}')
    def agregarMascota(self):
        try:
            nombre_cliente=input('Digite el nombre del cliete').strip()
            cliente=next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            if not cliente:
                raise ValueError('Cliente no encontrado')
            nombre=input('Digite el nombre de la mascota')
            especie=input('Digite la especie de la mascota')
            edad=input('Digite la edad de la mascota')
            raza=input('Digite la raza de la mascota')
            if not nombre or not especie or not edad or not raza:
                raise ValueError('Todos los datos se deben de registrar')
            mascota=Mascota(nombre,especie,edad,raza)
            cliente.agregarMascota(mascota)
        except ValueError as e:
            print(f'Error : {e}')

sistema()


'''
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
menu()'''
'''

cliente1=Cliente("Andres","14","3144572234","cr 13 #18-90","Chocolight")
print(cliente1.nombre)
print(cliente1.edad)
print(cliente1.contacto)
print(cliente1.direccion)
print(cliente1.mascota)
veterinario1=Veterinario("Juan","12")
print(veterinario1.nombre)
print(veterinario1.edad)'''