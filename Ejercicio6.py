# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Función principal
def main():
    # Solicitar al usuario la base y la altura del triángulo
    while True:
        try:
            base = float(input("Introduce la base del triángulo: "))
            if base > 0:
                break
            else:
                print("Por favor, introduce un valor positivo para la base.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido para la base.")

    while True:
        try:
            altura = float(input("Introduce la altura del triángulo: "))
            if altura > 0:
                break
            else:
                print("Por favor, introduce un valor positivo para la altura.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido para la altura.")

    # Calcular el área del triángulo
    area = calcular_area_triangulo(base, altura)

    # Mostrar el resultado
    print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
