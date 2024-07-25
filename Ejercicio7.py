import math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio * radio

# Función principal
def main():
    # Solicitar al usuario el radio del círculo
    while True:
        try:
            radio = float(input("Introduce el radio del círculo: "))
            if radio > 0:
                break
            else:
                print("Por favor, introduce un valor positivo para el radio.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido para el radio.")

    # Calcular el área del círculo
    area = calcular_area_circulo(radio)

    # Mostrar el resultado
    print(f"El área del círculo con radio {radio} es: {area:.2f}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
