# Función para sumar dos números binarios representados como cadenas
def suma_binaria(bin1, bin2):
    # Convierte los binarios a enteros, los suma y los vuelve a convertir a binario
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

# Ejemplo de uso
binario1 = '1010'  # 10 en decimal
binario2 = '1101'  # 13 en decimal

# Llamada a la función y almacenamiento del resultado
resultado = suma_binaria(binario1, binario2)

# Imprime la suma en binario
print(f'Suma de {binario1} y {binario2} es: {resultado}')  # Salida esperada: 10111
