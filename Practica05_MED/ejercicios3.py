def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error a dividir entre cero!!1")
print(f"Dividir = {dividir(4,2)}")
print(f"Dividir = {dividir(4,0)}")