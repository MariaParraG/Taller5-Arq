# Conversión de binario a decimal
def bin_a_decimal(binario):
    # Convierte un número binario (como cadena) a decimal
    return int(binario, 2)

# Ejemplo de uso
binario = '1011'  # 11 en decimal

# Llamada a la función y almacenamiento del resultado
decimal = bin_a_decimal(binario)

# Imprime la conversión
print(f'El número binario {binario} es {decimal} en decimal.')  # Salida esperada: 11
