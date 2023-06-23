# Codificamos el famoso juego del ahorcado
#importamos la clase choice para elegir un número al azar
from random import randint, choice

#defino la lista de palabras con las que se jugará y que seleccionará al azar el programa
lista_palabras = ['arbol','bicicleta','reloj','bizcocho','ordenador','boton']
letras_introducidas=[]

#la siguiente variable almacena el número de palabras de la lista
numPalabras = len(lista_palabras)


#defino la funcion seleccionar la palabra al azar que se deberá adivinar
def palabra_azar(lista_palabras):
    #palabra = lista_palabras[randint(0,numPalabras-1)]
    palabra = choice(lista_palabras)
    return palabra



#funcion que muestra el panel oculto palabra
def muestra_panel(palabra):
    guion =""
    for n in palabra:
        guion += guion.join('-')
    print(guion)



#defino la función explica el juego

def informador():
    print('Hola concursante. El juego consiste en acertar una palabra\nen un máximo de 6 intentos')
    print('para ello, debes introducir letras y el programa te dirá si están o no,')
    print('y la posición que ocupa')
    #print('¿te atreves?')

# defino la función que solicita letras al usuario y comprueba si ha introducido una letra del abecedario
def solicitar_letra(letras_introducidas):
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
   
    letra= input('introduce un caracter a buscar: ')
    while not letra in abecedario or len(letra) != 1:
        print ('Introduce una letra del abecedario: ')
        letra = input('introduce un caracter a buscar: ')
    else:
        letras_introducidas.append(letra)
        pass
    print(letras_introducidas)
    return letra, letras_introducidas

def formar_palabra(palabra,letras_validas):
    lista_oculta = []
    #print(f'la palabra es {palabra}')
    #print(f'las letras validas son {letras_validas}')
    for l in palabra:
        if l in letras_validas:
            lista_oculta.append(l)
        else:
             lista_oculta.append('-')
    print(''.join(lista_oculta))
    return lista_oculta

def comprobar_siesta(letra,palabra, esta):
    
    if letra in palabra:
       esta = True
       
    else:
        esta = False
               
    return esta

# def aparece_letra(letra, palabra):
#     lista_oculta = []
#     lista_indices = list(enumerate(palabra))
#     print(lista_indices)
#     for indice, caracter in lista_indices:
#         if caracter == letra:
#            #print(f'el caracter {caracter} aparece en la posición {indice +1}')
#            lista_oculta.insert(indice,letra)
#         else:
#             lista_oculta.insert(indice,'-')
    
#     print(''.join(lista_oculta)) 
  

def jugar():
    informador()
    respuesta = str(input('¿te atreves jugar? s/n '))
    while respuesta.lower() != 's':
        print('en otra ocasión será')
        break
    else:
        juego()
        
        

def juego():
    letras_introducidas = []
    palabra= palabra_azar(lista_palabras)
    print(f'la palabra oculta tiene {len(palabra)} caracteres')
    muestra_panel(palabra)
    acertadas = 0
    contador = 6
    esta = False
    while contador >=0 or acertadas <= len(palabra):
        letra= solicitar_letra(letras_introducidas)

        if not comprobar_siesta(letra[0],palabra,esta):
            contador -=1
            print(f'lo siento esa letra no está. te quedan {contador} vidas')
           
        else:
           
            formar_palabra(palabra,letra[1])
            panel = formar_palabra(palabra, letra[1])
            if '-' not in panel:
                print(f'Felicidades has acertado la palabra oculta: {palabra} \n')
                jugar()
            else:
                pass
            
            
    else:
        print ('lo siento has agotado todos los intentos')
        print(f'la palabra era {palabra}')
        


jugar()
