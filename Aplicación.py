# Aplicación de Operaciones Numéricas en Google Colab

def suma_binaria(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def bin_a_decimal(binario):
    return int(binario, 2)

def complemento_a_dos(binario):
    n = len(binario)
    invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
    suma = int(invertido, 2) + 1
    return bin(suma)[2:].zfill(n)

def decimal_a_ieee754(numero):
    import struct
    binario = bin(struct.unpack('!I', struct.pack('!f', numero))[0])[2:]
    return binario.zfill(32)

# Menú interactivo
while True:
    print("\n📌 MENÚ DE OPERACIONES")
    print("1️⃣ Suma binaria")
    print("2️⃣ Conversión Binario ↔ Decimal")
    print("3️⃣ Complemento a 2")
    print("4️⃣ Representación en IEEE 754 (punto flotante)")
    print("5️⃣ Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        bin1 = input("Ingrese el primer número binario: ")
        bin2 = input("Ingrese el segundo número binario: ")
        print("Resultado:", suma_binaria(bin1, bin2))
    
    elif opcion == "2":
        binario = input("Ingrese un número binario: ")
        print(f"Decimal: {bin_a_decimal(binario)}")
    
    elif opcion == "3":
        binario = input("Ingrese un número binario: ")
        print(f"Complemento a 2: {complemento_a_dos(binario)}")
    
    elif opcion == "4":
        num = float(input("Ingrese un número decimal: "))
        print(f"IEEE 754 (32 bits): {decimal_a_ieee754(num)}")
    
    elif opcion == "5":
        print("Saliendo...")
        break
    
    else:
        print("❌ Opción no válida. Intente de nuevo.")
