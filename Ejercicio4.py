# Función para calcular la suma de los primeros n enteros positivos
def calcular_suma(n):
    return n * (n + 1) // 2

# Función principal
def main():
    # Leer un entero positivo del usuario
    while True:
        try:
            n = int(input("Introduce un entero positivo: "))
            if n > 0:
                break
            else:
                print("Por favor, introduce un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero positivo.")

    # Calcular la suma utilizando la fórmula
    suma = calcular_suma(n)

    # Mostrar el resultado
    print(f"La suma de los primeros {n} enteros positivos es: {suma}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
