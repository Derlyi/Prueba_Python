# Función para calcular el salario semanal y mensual
def calcular_salario(precio_por_hora):
    horas_por_semana = 40
    semanas_por_mes = 4
    salario_semanal = precio_por_hora * horas_por_semana
    salario_mensual = salario_semanal * semanas_por_mes
    return salario_semanal, salario_mensual

# Función principal
def main():
    # Solicitar al usuario el precio por hora
    while True:
        try:
            precio_por_hora = float(input("Introduce tu tarifa por hora en dólares: "))
            if precio_por_hora > 0:
                break
            else:
                print("Por favor, introduce un valor positivo para la tarifa por hora.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido para la tarifa por hora.")

    # Calcular el salario semanal y mensual
    salario_semanal, salario_mensual = calcular_salario(precio_por_hora)

    # Mostrar los resultados
    print(f"Con una tarifa de ${precio_por_hora:.2f} por hora:")
    print(f"Tu salario semanal será: ${salario_semanal:.2f}")
    print(f"Tu salario mensual será: ${salario_mensual:.2f}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
