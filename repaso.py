"""EN ESTE SCRIPT HAREMOS UN REPASO DE PYTHON
    COMENZAREMOS CON LAS ESTRUCTURAS DE DATOS"""
### HOLA MUNDO
def saludar(nombre):
    return print(f"Hola mundo soy {nombre}")
    # console.log(`Hola mundo soy ${nombre}`);

nombre = "Jesedh"
saludar(nombre)

### TIPOS DE VARIABLES O ESTRUCTURAS DE DATOS MAS BASICAS
texto = "Texto"
numero = 5690
puntoDecimal = 3.1416
booleano = True

### ESTRCUTURAS DE DATOS
tupla = (1,2,3,4,5) # no se puede modificar una ves creada
arregloLista = ["hola", "mundo", 1,2,3, False, [1,2,3]]
print(arregloLista[6][1])
diccionarioObjeto = {
    "uno": 1000,
    "dos": 2000,
    3: "tresmil",
    "listaDentro": [1,2,3]
}
print(diccionarioObjeto["listaDentro"])

### OPERADORES ARITMETICOS
suma = 1+1
resta = 1-1
multiplicacion = 3*3
division = (9/3)
print(10%3) # residuo

### OPERADORES ARITMETICOS
igualdad = (4==4)
desigualdad = 4!=5
mayorque = 5>3
menorigualque = 6<=10

logica = True and False
logica1 = True or False

"""ESTRCUTURAS DE CONTROL"""

### CONDICIONALES PARA CONTROLAR EL FLUJO DE DATOS
### IF
acceso = True
if (acceso):
    print("Puedes acceder")
elif(acceso == False):
    print("No puedes acceder")
else:
    print("Credencial incorrecta")

### MATCH O SWITCH
color = "amarillo"

match color:
    case "verde":
        print("Exito")
    case "amarillo":
        print("Advertencia")
    case _:
        print("Error")

### CICLOS, BUClES O LOOPS
### FOR
animales = ["perro", "gato", "arañas"]
for animal in animales:
    print(animal)

def multiplicar(num1, num2):
    return num1*num2
numeros = [1,2,3]
for numero in numeros:
    print(multiplicar(numero,2))

### WHILE
condicionInicial = 100
condicionFinal = 105
while condicionInicial < condicionFinal:
    print(f"El numero es {condicionInicial}")
    condicionInicial += 1

"""PROGRAMACION ORIENTADA A OBJETOS"""
### OBJETOS SIN POO
lenguaje = {
    "nombre": "javascript",
    "año": 1995
}

def descripcion():
    print("%s fue creado en el año %s" % (lenguaje["nombre"], lenguaje["año"]))

descripcion()

### CLASES
class lenguajes:
    # Propiedades de la clase
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    # Metodos de la clase
    def descripcion(self):
        print("%s fue creado en el año %s" % (self.nombre, self.año))

javascript = lenguajes("javascript", 1995) # creamos el objeto, instancia de la clase
javascript.descripcion()
python = lenguajes("python", 1998) # creamos el objeto, instancia de la clase
python.descripcion()
sql = lenguajes("sql", 1990) # creamos el objeto, instancia de la clase
sql.descripcion()

### MODULOS
import modulo as a

resultado = a.restar(5,3)
print(resultado)