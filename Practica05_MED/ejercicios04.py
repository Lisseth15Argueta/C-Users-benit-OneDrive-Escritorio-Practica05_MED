# a.Ingresar n datos a una lista
def ingresar_datos():
    n = int(input("Ingrese la cantidad de datos: "))
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese el dato {i + 1}: "))
        datos.append(dato)
    return datos

#b. Ordenar una lista de menor a mayor.
def ordenar_lista(lista):
    return sorted(lista)

#c. Calcular la sumatoria de los datos de una lista.
def calcular_sumatoria(lista):
    return sum(lista)

#d. Calcular la media de los datos.
def calcular_media(lista):
    sumatoria = calcular_sumatoria(lista)
    media = sumatoria / len(lista)
    return media

#e. Calcular la mediana.
def calcular_mediana(lista):
    lista_ordenada = ordenar_lista(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana

#f. Calcular la moda.
def calcular_moda(lista):
    from collections import Counter
    contador = Counter(lista)
    moda = [item for item, count in contador.items() if count == max(contador.values())]
    return moda

#g. Calcular la desviación típica o estándar para datos sin agrupar.
def calcular_desviacion_estandar(lista):
    import math
    media = calcular_media(lista)
    sumatoria_de_cuadrados = sum([(x - media) ** 2 for x in lista])
    desviacion_estandar = math.sqrt(sumatoria_de_cuadrados / (len(lista) - 1))
    return desviacion_estandar

# Ejemplo de uso:
datos = ingresar_datos()
print("Lista de datos ingresados:", datos)
print("Lista ordenada:", ordenar_lista(datos))
print("Sumatoria de los datos:", calcular_sumatoria(datos))
print("Media de los datos:", calcular_media(datos))
print("Mediana de los datos:", calcular_mediana(datos))
print("Moda de los datos:", calcular_moda(datos))
print("Desviación estándar de los datos:", calcular_desviacion_estandar(datos))
