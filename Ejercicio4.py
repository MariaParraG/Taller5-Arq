import struct

# Convertir un número decimal a punto flotante (IEEE 754)

def decimal_a_punto_flotante(num):

return format(struct.unpack('!I, struct.pack('f', num))[0], '032b')

#Ejemplo de uso

numero_decimal = -10.5

punto_flotante decimal_a_punto_flotante(numero_decimal)

print('El número (numero_decimal) en punto flotante es: (punto_flotante}")
