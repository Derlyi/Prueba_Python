# Función para convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Función principal
def main():
    # Solicitar al usuario la temperatura en grados Fahrenheit
    while True:
        try:
            fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
            break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido para la temperatura.")

    # Convertir la temperatura a grados Celsius
    celsius = fahrenheit_a_celsius(fahrenheit)

    # Mostrar el resultado
    print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
