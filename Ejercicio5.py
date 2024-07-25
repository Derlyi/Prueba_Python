# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    return lado * lado

# Función principal
def main():
    # Solicitar al usuario la longitud del lado del cuadrado
    while True:
        try:
            lado = float(input("Introduce la longitud del lado del cuadrado: "))
            if lado > 0:
                break
            else:
                print("Por favor, introduce un valor positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")

    # Calcular el área del cuadrado
    area = calcular_area_cuadrado(lado)

    # Mostrar el resultado
    print(f"El área del cuadrado con lado {lado} es: {area}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
