# Cálculo del complemento a 2
def complemento_a_dos(binario):
    n = len(binario)  # Longitud del número binario

    # Invertir los bits: cambiar 0 -> 1 y 1 -> 0
    invertido = ''.join('1' if bit == '0' else '0' for bit in binario)

    # Sumar 1 al número invertido
    suma = int(invertido, 2) + 1

    # Convertir de nuevo a binario y asegurarse de que tenga la misma longitud
    return bin(suma)[2:].zfill(n)

# Ejemplo de uso
binario_negativo = '1100'  # Representa -4 en complemento a 2 (4 bits)

# Obtener el complemento a 2
complemento = complemento_a_dos(binario_negativo)

# Imprimir el resultado
print(f'El complemento a 2 de {binario_negativo} es: {complemento}')  # Salida esperada: 0100

