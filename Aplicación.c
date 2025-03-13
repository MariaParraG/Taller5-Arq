#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Función para sumar dos números binarios
void suma_binaria(char bin1[], char bin2[], char resultado[]) {
    int num1 = strtol(bin1, NULL, 2);
    int num2 = strtol(bin2, NULL, 2);
    int suma = num1 + num2;
    sprintf(resultado, "%b", suma);  // Formatear como binario
}

// Función para convertir binario a decimal
int bin_a_decimal(char binario[]) {
    return strtol(binario, NULL, 2);
}

// Función para obtener el complemento a 2
void complemento_a_dos(char binario[], char resultado[]) {
    int n = strlen(binario);
    
    // Invertir bits
    for (int i = 0; i < n; i++) {
        resultado[i] = (binario[i] == '0') ? '1' : '0';
    }
    resultado[n] = '\0';

    // Sumar 1 al número invertido
    int decimal = bin_a_decimal(resultado) + 1;
    itoa(decimal, resultado, 2);  // Convertir de nuevo a binario
}

// Función para convertir un número decimal a IEEE 754 (32 bits)
void decimal_a_ieee754(float num, char resultado[]) {
    union {
        float f;
        unsigned int i;
    } conv;
    
    conv.f = num;
    
    for (int i = 31; i >= 0; i--) {
        resultado[31 - i] = (conv.i & (1 << i)) ? '1' : '0';
    }
    resultado[32] = '\0';
}

// Función principal con menú interactivo
int main() {
    int opcion;
    char bin1[32], bin2[32], resultado[32];
    float num;

    do {
        printf("\n📌 MENÚ DE OPERACIONES\n");
        printf("1️⃣ Suma binaria\n");
        printf("2️⃣ Conversión Binario ↔ Decimal\n");
        printf("3️⃣ Complemento a 2\n");
        printf("4️⃣ Representación en IEEE 754 (punto flotante)\n");
        printf("5️⃣ Salir\n");
        printf("Seleccione una opción: ");
        scanf("%d", &opcion);
        
        switch (opcion) {
            case 1:
                printf("Ingrese el primer número binario: ");
                scanf("%s", bin1);
                printf("Ingrese el segundo número binario: ");
                scanf("%s", bin2);
                suma_binaria(bin1, bin2, resultado);
                printf("Resultado: %s\n", resultado);
                break;

            case 2:
                printf("Ingrese un número binario: ");
                scanf("%s", bin1);
                printf("Decimal: %d\n", bin_a_decimal(bin1));
                break;

            case 3:
                printf("Ingrese un número binario: ");
                scanf("%s", bin1);
                complemento_a_dos(bin1, resultado);
                printf("Complemento a 2: %s\n", resultado);
                break;

            case 4:
                printf("Ingrese un número decimal: ");
                scanf("%f", &num);
                decimal_a_ieee754(num, resultado);
                printf("IEEE 754 (32 bits): %s\n", resultado);
                break;

            case 5:
                printf("Saliendo...\n");
                break;

            default:
                printf("❌ Opción no válida. Intente de nuevo.\n");
        }
    } while (opcion != 5);

    return 0;
}
