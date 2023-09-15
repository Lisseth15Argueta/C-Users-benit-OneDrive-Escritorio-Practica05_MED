# 1, Crear una funcion
# Palabra reservada def seguido del nombre de la funcion

def mifuncion():
    print("Este es un mensaje")

mifuncion()
print()

# 2. Funciones con parametros

def mifuncion(nombre, apellido):
    print(f"Hola {nombre} {apellido}!!")
mifuncion("Lisseth", "Argueta")
print()

# 3. Retomar valores a travez de la funcion

def sumar(a,b):
    return a + b
resultado = sumar(4,6)
print(f"El resultado es {resultado}")
print(f"El resultado es {sumar(5,6)}")
print()

# 4. Paramentros (por nombre y por posicion)

def areaTriangulo(base, altura):
    return (base * altura) / 2

alturaTriangulo = 10
baseTriangulo = 20
# - Por posicion
print(areaTriangulo(alturaTriangulo, baseTriangulo))
# - Por Nombre
print(areaTriangulo(altura = alturaTriangulo, base = baseTriangulo))
print()

# 5. Valores por defecto 

def multiplicar(a, b = 1):
    return a * b

print(f"La multiplicacion es: {multiplicar(2,5)}")
print(f"La multiplicacion es: {multiplicar(2)}")
print()

# 6. Argumento indeterminados por posiccion

def multiplicarMuchos(a, *numeros):
    for numero in numeros:
        a *= numero
        return a
print(multiplicarMuchos(2))
print(multiplicarMuchos(2,3))
print(multiplicarMuchos(2,3,4))
print()

# 7. Otra forma de argumentos indeterminados por nombre

def mostrarformacion(**persona):
    informacion = persona.items()
    for clave, valor in informacion:
        print(f"{clave}: {valor}")

mostrarformacion(nombre = " Erika Lisseth")
mostrarformacion(apellido= "Argueta Benitez")
print()

# 8. Retorno de multiple valores

def datos():
    nombre = "Lisseth"
    apellido = "Argueta"
    return "Erika", "Argueta", 26, "Femenino"
    return nombre, apellido, 26, "Femenino"

misDatos = datos()
print(misDatos[0])