class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido, cuenta, saldo):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.saldo = saldo
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} tiene {self.saldo}€ en su {self.cuenta}'
    
    def imprimir(self):
        print (f'el saldo acumulado es {self.saldo}')

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo 
    
    def retirar(self, cantidad):
         if cantidad <=self.saldo:
            self.saldo -= cantidad
         else:
            print ('has solicitado más dinero del que tienes')
         return self.saldo

def crear_cliente(): 
    nombre = input('introduce el nombre del cliente: ')
    apellido = input('introduce el nombre del apellido: ')
    cuenta = input('Número de cuenta: ')
    saldo = int(input(f'Introduce el saldo incial de la cuenta {cuenta}: '))

    nuevoCliente = Cliente(nombre, apellido, cuenta, saldo)
    #nuevoCliente.nombre = nombre
    #nuevoCliente.apellido = apellido
    return nuevoCliente

def inicio():
    nuevoCliente= crear_cliente()
    menu= """              1- depositar dinero 
              2- retirar dinero
              3- ver el saldo
              4- salir"""
    print (menu)
    opcion = input('¿qué operación desea realizar? ')
    opciones_permitidas =['1','2','3','4']
    while opcion in opciones_permitidas:
       if opcion == '1':
            ingreso= int(input('introduce la cantidad que deseas ingresar: '))
            nuevoCliente.depositar(ingreso)
       else:
             if opcion == '2':
                reintegro = int(input('introduce la cantidad que deseas retirar: '))
                nuevoCliente.retirar(reintegro)
             else:
                  if opcion == '3':
                      nuevoCliente.imprimir()
                  else:
                      print('que tenga un buen dia')
                      break
            
       opcion = input('¿qué operación desea realizar? ')
     
    else:
        opcion= input ('vuelve a introducir una opción válida (1,2,3 4)')
            
inicio()

