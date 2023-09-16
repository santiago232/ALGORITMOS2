# Definir la función para calcular el área del rectángulo
def area_rectangulo(lado1, lado2):
    area = lado1 * lado2
    return area

# Cargar los lados de los dos rectángulos
lado1_rectangulo1 = float(input("Ingrese el valor del primer lado del primer rectángulo: "))
lado2_rectangulo1 = float(input("Ingrese el valor del segundo lado del primer rectángulo: "))
lado1_rectangulo2 = float(input("Ingrese el valor del primer lado del segundo rectángulo: "))
lado2_rectangulo2 = float(input("Ingrese el valor del segundo lado del segundo rectángulo: "))

# Calcular las áreas de los dos rectángulos
area_rectangulo1 = area_rectangulo(lado1_rectangulo1, lado2_rectangulo1)
area_rectangulo2 = area_rectangulo(lado1_rectangulo2, lado2_rectangulo2)

# Comparar las áreas de los dos rectángulos y mostrar cuál es mayor
if area_rectangulo1 > area_rectangulo2:
    print("El primer rectángulo tiene una superficie mayor.")
elif area_rectangulo2 > area_rectangulo1:
    print("El segundo rectángulo tiene una superficie mayor.")
else:
    print("Los dos rectángulos tienen la misma superficie.")


