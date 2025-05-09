import random  # Importo para resolver el ejercicio 6
import statistics # Importo  para resolver el ejercicio 6

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
def verificar_edad():
    edad = int(input("Ingrese su edad: "))  
    if edad >= 18: 
        print("Es mayor de edad")  
    else:
        print("Es menor de edad") 
verificar_edad()

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

def verificar_nota():
    nota = float(input("Ingrese su nota: "))  
    if nota >= 6: 
        print("Aprobado")  
    else:
        print("Desaprobado") 

verificar_nota()

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
  
def solicitar_par():
    numero = int(input("Ingrese un número: "))  
    if numero % 2 == 0:  
        print("Ha ingresado un número par") 
    else:
        print("Por favor, ingrese un número par")  
solicitar_par()

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece..

def clasificar_edad():
    edad = int(input("Ingrese su edad: "))  
    if edad < 12:  
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

clasificar_edad()

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). 

def verificar_contrasena():
    contrasena = input("Ingrese una contraseña: ")  
    if 8 <= len(contrasena) <= 14:  
        print("Ha ingresado una contraseña correcta")  
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")  

verificar_contrasena()

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. 

def determinar_sesgo():

    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    moda_num = statistics.mode(numeros_aleatorios) 
    mediana_num = statistics.median(numeros_aleatorios)
    media_num = statistics.mean(numeros_aleatorios)

    print(f"Moda: {moda_num}, Mediana: {mediana_num}, Media: {media_num}")

    if media_num > mediana_num > moda_num:
        print("Sesgo positivo o a la derecha")
    elif media_num < mediana_num < moda_num:
        print("Sesgo negativo o a la izquierda")
    else:
        print("Sin sesgo")
        
determinar_sesgo()

#7) Escribir un programa que solicite una frase o palabra al usuario
def agregar_exclamacion():
    frase = input("Ingrese una frase o palabra: ")  
    ultima_letra = frase[-1].lower()  
    if ultima_letra in "aeiou":  
        print(frase + "!")  
    else:
        print(frase)  
        
agregar_exclamacion()

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:

def transformar_nombre():
    nombre = input("Ingrese su nombre: ")  
    opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: "))  

    if opcion == 1:  
        print(nombre.upper())  
    elif opcion == 2:
        print(nombre.lower())  
    elif opcion == 3:
        print(nombre.title())  
    else:
        print("Opción inválida")
      
transformar_nombre()


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
def clasificar_terremoto():
    magnitud = float(input("Ingrese la magnitud del terremoto: ")) 
    if magnitud < 3:  
        print("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")
clasificar_terremoto()

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

def determinar_estacion():
    hemisferio = input("Ingrese el hemisferio (N/S): ").upper()  
    mes = input("Ingrese el mes del año: ").lower() 
    dia = int(input("Ingrese el día: "))  

    if hemisferio == "N":  
        if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
            print("Invierno")
        elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
            print("Primavera")
        elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
            print("Verano")
        else:
            print("Otoño")
    elif hemisferio == "S":
        if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
            print("Verano")
        elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
            print("Otoño")
        elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
            print("Invierno")
        else:
            print("Primavera")
    else:
        print("Hemisferio inválido")
      
determinar_estacion()
